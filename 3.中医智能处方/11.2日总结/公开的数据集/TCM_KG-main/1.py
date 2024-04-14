
with open("/Users/gjh/workspaces/vscode/python/5.TCM.python/TCM_KG-main/baseline_all_kg_triples.txt", "r", encoding="utf-8") as file:
    empty_set = set()
    for line in file.readlines():
        entity_1, entity_2, relation = line.split("\t")
        empty_set.add(relation.replace('\n', ''))


    print(empty_set)
