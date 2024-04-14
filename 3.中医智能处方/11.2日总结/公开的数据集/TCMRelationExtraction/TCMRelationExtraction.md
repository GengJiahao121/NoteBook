# TCMRelationExtration

病-证-方-药

方剂-疾病 1-n 一个方剂可以治疗很多种疾病，一个疾病可以由不同的方剂治愈，下面同理

方剂-证型 1-n

草药-疾病 1-n

草药-证型 1-n

证型-疾病 1-n

---

疾病词典

方剂词典

方剂-中药词典

草药词典

证型词典

中医知识集合

---

1. candicate-relation_formula2disease.txt 方剂名-疾病名称

```
ID	FormulaID	FormulaName	DiseaseID	DiseaseName	Label

1	46	一扫光	808	细支气管炎	0
```

2. candicate-relation_formula2syndrome.txt 方剂名-证

```
ID	FormulaID	FormulaName	SyndromeID	SyndromeName	Label

1	25	一加减正气散	870	湿热证	?
```
3. candicate-relation_ herb2disease.txt 草药-疾病

```
ID	HerbID	HerbName	DiseaseID	DiseaseName	Label

1	22	青天葵	205	慢性支气管炎	?
```
 
4. candicate-relation_herb2syndrome.txt 草药-证型

```
ID	HerbID	HerbName	SyndromeID	SyndromeName	Label

1	23	饴糖	710	风寒证	0
```

5. candicate-relation syndrome2disease.txt 证型-疾病

```
ID	SyndromeID	SyndromeName	DiseaseID	DiseaseName	Label

1	14	小儿感冒病	1	流行性腮腺炎	0
```

6. dic_disease.txt 疾病词典

```
ID	Name

1	流行性腮腺炎
```

7. dic_formula.txt 方剂词典

```
ID	Name

1	（山黎）峒丹
```

8.  dic_formula2herb.txt 方剂-中药词典

```
ID	FormulaID	HerbID
1	39937	5461
2	39937	685
3	39937	1633
4	39937	6025
5	39936	1438
6	39936	1594
7	39936	4169
8	39936	4289
9	39936	6025
10	39936	6579
```

9. dic_herb.txt 草药词典

```
ID	Name
1	一匹草
2	化气兰
3	长杆兰
```

10. dic_syndrome.txt 证型词典

```
ID	Name
1	儿科癌病
2	小儿钩虫病
3	小儿蛔虫病
```

11. tcm_literature.txt 中医知识

```
ID	Title	Abstract
987	补肾健脾方药对老年大鼠肝脏衰老有关基因表达的影响	目的:比较补肾、健脾方药对老年大鼠肝脏衰老有关基因表达的调控作用。方法:以自然衰老大鼠为衰老模型,随机分为老年对照组、老年补肾组、老年健脾组,并设青年大鼠对照组。予药物干预4个月后,采用RT-PCR和Western blot方法检测大鼠肝脏抑癌基因p16、抑癌基因p21、细胞周期素D1(Cyclin D1)、增殖细胞核抗原(PCNA)、细胞周期素E(CyclinE) mRNA转录和蛋白的表达。结果:老年大鼠肝脏p16、p21和Cyclin D1 mRNA/蛋白的表达明显增高,而PCNA和Cyclin E mRNA/蛋白的表达明显降低。补肾方药可明显下调肝脏p16和Cyclin  D1,上调PCNA和Cyclin E基因mRNA与蛋白的表达;健脾方药能明显下调肝脏Cyclin D1,上调PCNA和Cyclin E基因mRNA与蛋白表达,但对p16作用不明显。结论:补肾、健脾方药均能不同程度调控肝脏衰老有关基因表达,促进老年大鼠肝细胞增殖,但补肾方药作用似更明显。
988	四妙勇安汤的有效成分对血管内皮细胞增殖的影响	目的:研究四妙勇安汤的有效成分对脐静脉内皮细胞(ECV304)增殖的影响,以探讨其促血管新生的可能机制。方法:体外培养ECV304,单体进行干预,利用MTT及BrdU-ELISA法检测其对ECV304增殖的影响。结果:绿原酸101ng/ml~102ng/ml,阿魏酸102ng/ml~104ng/ml浓度组为促细胞增殖的优选浓度。结论:绿原酸、阿魏酸促内皮细胞增殖能力与血清有协同作用。
```
