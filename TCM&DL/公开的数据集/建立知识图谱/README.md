# 如何建立知识图谱

## 目前有的数据

baseline_all_kg_triples.txt

```
头结点 目标结点 关系

(其中关系类型有：
'药味', 'TS_MS', '部位', '用量', '证候', '注意', '贮藏', 'symmap_chemical', '治法', '中药', '毒性', '归经', '药性', '功能', 'chemical_MM', '用法')

尿痛	Urethral Pain	TS_MS （应该是症中文名-症英文名的关系）

SMIT07367	Cervical Radiculopathy	chemical_MM （化合物-症英文名）

蕤仁	SMIT01248	symmap_chemical（药物-化合物）

奶麻	连翘	中药

鹿角胶	3～6g	用量

瘀血内阻	血瘀气滞证	证候

熟大黄	干燥根	部位

胃热	降逆止呕	治法
```



