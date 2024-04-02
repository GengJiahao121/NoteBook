# TCM-SD程序运行流程：
1. 程序从**主函数所在的.py文件**开始运行,**从上之下**
2. from和import导入各种**包名**和**类名**和**方法名**并成为**全局变量**；定义**全局变量**；程序只会记得**函数名**和**类名**不会进入到内部直到**遇见__main__函数之前**，遇到__main__函数**后就开始调用函数**
3. \__main__ == "\__main__":main()
   1. 创建参数解析器对象 -> 添加参数（数据路径名、模型名... ...） ->  解析参数
   2. 设置结果输出文件夹outputs
   3. 设置远程debug ptvsd
   4. 设置cuda,如果想使用多个GPU，需要设置local_rank
   5. 设置记录日志
   6. 设置随机种子
   7. 数据、参数、模型、分词器等的加载（如果有多个GPU设备需要进行阻塞其他进程只留下主进程后再进行）
       - 加载config, tokenizer, model并todeivce() 
       - 加载数据 -> 数据的random、batch、tensor化(load_and_cache_examples())
          1. 加载josn类型数据
          2. 数据的处理（_create_examples（lines, kb））
             -  传入**数据列表**，**单个标本为一个词典**（[‘{}’, ‘{}’, ...]）, 传入**知识**（{证型：{证型知识}, ... ... }）
             -  逐条数据进行处理（每条数据为一个‘词典’）
             -  对词典进行拆分，获得key-value（拆之前要将‘词典\n’-> 词典，因为line为字符串）；对**每条数据加入对应证型标签的外部知识**（这个知识从传入的知识中获取）和**指定数量的非标签知识**；形成examples[ , , ...] (每个例子**封装成对象**传入下面的创建特征)
             -  开始创建特征tokens_to_ids（传入examples, 分词器，真是标签列表，最大长度, pad_id, 和一些其他的特殊参数.....），循环遍历每个example
                -  利用tokenizer将字->数字id，得到input_ids, attention_mask, token_type_ids
                - 对齐输入长度，padding
                -  将真实标签->id（为序号就可以，没有固定的词典）
                -  将转换成功的example追加到examples列表中（加到examples之前的example同样也被**转换成为了对象**）
             - 创建完特征后，torch.save(features, cached_features_file）保存特征
             - 将特征转换为tensor并构建batchsize数据集
               - 逐条example进行tecsor向量的转换（`all_input_ids = torch.tensor([f.input_ids for f in features], dtype=torch.long)`）
               - 构建batchsize数据集（这里是将all_input_ids, all_attention_mask, all_token_type_ids, all_labels整合到一起形成一个dataset对象传回去，**并没有进行batchsize操作**）
   8. 开始train(args, train_dataset(并没有batchsize,只到tensor化这一步), model, tokenizer)
   
   **注：这个代码用到了多个GPU进行训练的选项，所以在进行batchsize化时，与单个gpu不太一样，多个gpu需要每个gpu一个batch,也就是一次处理gpu_number * batchsize条数据。**
   
      1. batchsize化(通过以下三行代码进行的batchsize化)
   
         <code> args.train_batch_size = args.per_gpu_train_batch_size * max(1, args.n_gpu) # 多个GPU同时进行训练时，每个gpu每次都可以处理一个batchsize大小的数据

         train_sampler = RandomSampler(train_dataset) if args.local_rank == -1 else DistributedSampler(train_dataset) # 打乱examples的顺序

         \#  具体来说，RandomSampler 是一个随机采样器，它会随机地从数据集中选择样本，用于训练模型。而 DistributedSampler 是一个分布式采样器，它会将数据集分成多个部分，每个部分由不同的进程或设备负责采样，用于分布式训练模型。

         train_dataloader = DataLoader(train_dataset, sampler=train_sampler, batch_size=args.train_batch_size) # 创建一个用于训练的DataLoader对象，随机抽样形式的每个batchsize大小一个batch </code>

         注：steps，是指每个epoch中需要执行多少次反向传播，优化步数; epoch是指数据集被训练几个来回；args.gradient_accumulation_steps 表示梯度累积的步数, 即几步求一次导；

      2. 指定优化器类型；创建学习率调度器
      3. 是否混合精度训练fp16
      4. 是否多个GPU
         1. 是否使用 torch.nn.DataParallel 将模型转换为多 GPU 模式
         2. 使用 torch.nn.parallel.DistributedDataParallel 将模型转换为分布式模式
      5. 定义global_step, tr_loss, logging_loss日志
      6.  model.zero_grad() # 每次更新模型参数之前，我们需要将之前计算的梯度清零
      7.  定义epoch进度条
      8.  设置随机种子
      9.  开始迭代训练epoch
          1.  batch : epoch_iterator; 定义单个epoch进度条，可以通过 epoch_iterator 来迭代训练数据集中的每个batch
              1. model.train()
              2. 将batch中的数据to(args.device)
              3. 确定inputs格式，此时inputs中的数据是可以在device上进行计算的格式
              4. outputs = model(**inputs)
              5. 得到loss
              6. loss.backward()
              7. tr_loss训练总损失 += 单步loss
              8. 梯度裁剪
              9. optimizer.step()
              10. scheduler.step()  # Update learning rate schedule 学习率调度器
              11. model.zero_grad() # 每个step结束后都需要清空模型的梯度信息，以便下一步反向传播。如不，梯度会累加到之前的梯度上，导致训练结果不正确。
              12. global_step += 1

               注：

               1 这里如果是多个gpu，ouputs中的loss要去平均；

               2 如果梯度步数不是1，单步得到的loss需要除以梯度步数；

               3 如果为fp16混合精度，loss.backward()不可用，要用特定的函数反省传播；

               4 梯度裁剪的方法fp16混合进度也不可用，需要特定的方法；

          2. 保存每一epoch的模型和参数，即保存checkpoint
          3. 如果训练步数超过了最大步数那么不再继续训练
      10. 返回总步数和总损失/步数（也就是平均损失）
      11. 保存微调模型和参数
      12. 再重新加载微调模型和参数、tokenizer、并to_device()
      13. 开始进行evaluation/test
          1.  加载tokenizer
          2.  找到checkpoint存放未知,即pytorch_model.bin
          3.  加载模型checkpoint
          4.  model.to(args.device)
          5.  开始evaluate(args, model, tokenizer, prefix=prefix)
              1. 加载评估数据集（load_and_cache_examples()）**同上面的加载训练数据集一样方法**
                 1. get_dev_examples()得到examples列表，列表中为example对象
                 2. convert_examples_to_features()将examples转换为特征（汉字转换为数字id）得到features列表，列表中为feature对象
                 3. 存储特征到cache_features_file
                 4. 将特征转换为tensor类型
                 5. 返回数据集dataset(由all_inputs_ids, all_attention_mask, all_token_type_ids, all_labels组成)
              2. batchsize化
   
                  `args.eval_batch_size = args.per_gpu_eval_batch_size * max(1, args.n_gpu)
                  \# Note that DistributedSampler samples randomly
                  eval_sampler = SequentialSampler(eval_dataset)
                  eval_dataloader = DataLoader(eval_dataset, sampler=eval_sampler, batch_size=args.eval_batch_size)`
              3.  开始eval,定义eval_loss, eval_steps, preds, out_label_ids
              4.  通过tqdm来循环迭代每一个batch
                  1.  model.eval()
                  2.  batch = tuple(t.to(args.device) for t in batch) 加载到设备上
                  3.  torch.no_grad() **评估模式不需要求梯度**
                      1.  确定inputs格式，此时inputs中的数据是可以在device上进行计算的格式
                      2.  outpus = model(**inputs)
                      3.  从outputs中得到loss和**logits**
                      4.  eval_loss += 一个批次的损失，得到总损失
                      5.  eval_steps += 1
                      6.  logits即为最终输出的向量8batchsize x 148类别长度，他会与真实值进行比较,同时也会记录真实值
                      7.  通过函数算出 精确度，召回率， f1值，支持度
                      8.  返回结果
              5. 更新结果
           6. 返回结果



   
