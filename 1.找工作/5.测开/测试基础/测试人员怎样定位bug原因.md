## 为什么定位问题如此重要？
1. 降低误报
2. 明确制定某个开发，避免开发之间打太极，提高修复速度
3. 让开发人员足够信任你，提升开发对测试的信任度
4. 有助于理解产品内部逻辑，对架构的理解，以及数据流是怎样的走向。可以学到更多的东西。
5. 可以降低缺陷率。在bug系统中，我们会要求开发人员记录bug产生的原因。只有我们自己对bug有一个较全面的认识，才会判别出开发写的是不是真正的原因，也才能有助于我们后续对bug进行分析归类，根据bug分析，有针对性地未雨绸缪，进而提升产品质量，降低缺陷。

## 2 问题定位技巧
这个思路是和数据的走向一致的。大致是这样：
用户层面问题 -> Web页面/软件界面 -> 中间件 -> 后端服务 -> 代码 -> 数据库
以下都以Web页面举例说明。
第一步，用户层面问题指的是**用户自己的环境问题或者操作问题**，比如环境不通，或者操作不正确。这种问题一般不是bug，当然，如果要考虑构建更加健壮的软件，那么可以根据实际情况来决定要不要处理这类问题。
第二步，用户在**Web页面**进行正常操作时，也可能会发现问题。这类问题一般通过观察以及利用一些常识可以发现，比如样式问题一般是css的问题，交互问题一般是js的问题，文本问题一般是html的问题（当然有可能是其他问题，例如js生成html）。
第三步，Web页面操作后，比如发出一个请求，可能会进入中间件这个层面。我这里说的中间件是广义上的，比如**LVS、CDN、各种缓存服务器**等等。我们遇到过一个问题，发现刚刚上传的图片进行读取展示时就读不到，那么可以想到可能是**负载均衡**时将上传照片和读取照片两个请求分配到了不同的服务器导致的，也就是我们常说的**会话保持**。当然，中间件问题有时候是和开发相关的，有时候是公司其他团队负责的，比如360公司就是OPS在负责。当然，中间件也不仅仅会出现在这一步，实际的项目中可能还会用到更多的基础设施，比如消息中间件、数据存取中间件等，如果发现了相应的问题也就需要有对应的思路去排查。
第四步，服务会转发到我们真正的后端服务层，web服务器、应用服务器比如nginx、tomcat会收到请求。如果发现内存溢出，那么就可能会定位到是tomcat配置的问题；如果请求返回**404，也可能是nginx配置不当**。当然，这个时候可能会遇到一些环境问题，比如测试环境没有的问题，到线上就有了，很可能是环境原因，比如jdk版本不同、tomcat版本不同、jar包版本不同等等。
第五步，是数据库。代码没有问题，不代表软件没有问题。数据库层面也可能会有各种各样的问题，比如字段的约束问题等等。假如一个文本框的前端校验和接口校验的文本长度最大是50，但数据表字段设定的是varchar(30)，那么在存数据的时候肯定会报错。再比如之前发现一个数据库的问题，测试环境没有，到线上却有了，那么也可以看下是不是数据库版本不同导致的。
上面我们说的是问题定位的一个大致思路。每一个环节都有可能出现bug，既可能是response的问题，也可能是前端回调处理的问题。有的问题可能会直接暴漏在用户面前，有些则可能需要我们去分析日志。
当然，很多时候我们不需要这样一层一层去定位，经验丰富的开发或者测试根据现象可能马上能定位到究竟哪里出了问题。
## 下面我们就来说说测试人员定位问题的N板斧。


1
让子弹飞一会儿
碰到问题先别忙定位，首先请保存犯罪现场，并且确认能复现。然后排除QA的低级问题 。为什么要保存现场？如果以后复现不了，就证明不了问题的存在。有哪些QA的低级问题？常见的就是**hosts不对，网络不通，以及操作姿势不正确**等等。这个其实就是上文提到的用户层面问题，这里的用户就是QA人员。经常有QA人员发现问题后就赶紧叫开发过来看，开发这时候幽幽地说句“host对吗”，一看不对岂不是很尴尬。
还有一类问题就是**脏数据**，我们有时候会遇到服务端报500错误，查看日志后，报空指针，那么很有可能就是数据库中关联表的数据被人为删掉导致的。还有的问题是由于工具的影响导致的，例如fiddler。所以发现问题您别慌，让子弹飞一会，确认不是自己的问题再说。
2
直观查看页面表现
这个就是上文提到的对Web页面的观察。不再赘述。
3
看状态码
4xx状态码一般表示是**客户端问题**（当然也有可能是服务器端配置问题），比如发生了401，那么要看下是否带了正确的身份验证信息；发生了403则要看下是否有权限访问；404则要看下对应的URL是否真实存在。
而5xx一般表示**服务端问题**。比如发生了500错误，则表明是服务器内部错误，这个时候要配合服务器log进行定位；发生了502则可能是服务器挂了导致的；发生503可能是由于网络过载导致的；发生504则可能是程序执行时间过长导致超时。
4
看服务器日志
如果发生**5xx问题**，或者检查后端接口执行的sql是否正确，我们最常见的排查方法就是去看**服务器日志**比如tomcat日志，开发人员一般会打出关键信息和报错信息，从而找到问题所在。测试人员要养成看日志的习惯。并且，如果将来进行开发，也要养成打日志的习惯，否则发现问题真不知道到哪哭去。
5
接口的请求和返回以及js执行是否有报错
在第3点中我们说了状态码的问题，明确了4xx和5xx的问题所在。那么，如果接口返回了200，就一定正常吗？
假设有这么一种情况，要测试一个翻页控件，翻到第二页的时候，发现内容和第一页完全一样，接口请求返回的是200。**这个时候你会怎么排查？**
这个时候就要看**前端发送的参数正不正常，后端返回的内容正不正常**，即接口的请求和返回。
我们来看翻页控件的问题。我们看接口的请求（F12控制台查看网络请求或者抓包工具），一般根据开发的习惯，会有pn、ps参数，看看传值是否正确。如果请求参数不正确，那么就是前端的问题。如果正确，那么就看response，看看返回的内容对不对，以此就知道到底是前端问题还是服务端问题。如果发现js执行报错了，那就是前端有问题，比如跨域问题。
请求URL不正确，是前端bug，传参不正确，是前端bug，响应内容不正确，则是后端bug。如果是响应内容不正确的后端问题，那就要继续深挖，是接口吐数据的时候出错了，还是数据库中的数据就错了，还是缓存中的数据错了（如果用到了缓存的话）。经常见到后端开发人员有的负责接口，有的负责写入数据库，有的负责维护缓存，所以如果发现是后端的问题，可以更进一步确认下是哪块的问题。
6
看需求文档
有时候，前端和服务端的交互都正确，但是从测试的角度看不合理。这个时候，我们应该翻翻需求文档（如果没有的话，就直接抛出这个问题）。如果和需求文档不符，那么就要看下谁改合理，是前端改，还是服务端改，或者两者都得改。这里有一个原则，就是前端尽可能少地去承担逻辑，只负责渲染展现。当然，不要以为需求文档就全部正确，它也可能会有错误，我们也应该去发现需求文档的bug，然后再去协调PM，敦促FE或者RD进行修改。在这点上，不得不说，有的开发做的比较好，他会有自己的思想，在开发的时候就能发现需求文档的错误，而有的开发则是无条件无脑执行。
7
后端生成页面问题
后端生成页面，最常见的就是类似于jsp、php、python的某些前后端不分离的框架，这种比较特殊，常见于单人开发的项目，这种项目的问题排查和其他项目总的思路也一样，只不过前后端bug的修改可能都是同一个人而已。
8
开发提供可测性支持
有时候，涉及到多方面合作，不太好测试的情况下，需要开发提供可测性支持。比如，要查看接口给另一个接口发的请求是否正确，可以让开发打印出完整的请求log。还有一些逻辑开关、修改页面数据条数等，都属于可测性支持的范畴。
9
配置的问题
很多时候，bug不是代码问题，而是**tomcat配置、nginx配置、jdbc配置**等的问题。在这个层面上，测试人员最好能够了解下它们的各项配置，在发现问题后可能就会想到这方面的问题。
10
经验法则
太阳底下没有新鲜事，有经验的人早就遇到过相同的问题。高手往往能够一眼看穿表面现象内部的问题，然后直奔主题，迅速报告或者解决，留下别人在风中凌乱……
