import os
with open("1.txt", encoding='utf-8') as file1, open("2.txt", encoding='utf-8') as file2, open("3.txt", encoding='utf-8') as file3, open("Sorted.txt", "a", encoding='utf-8') as result:
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    lines3 = file3.readlines()
    all= {}
    all[file1] = lines1
    all[file2] = lines2
    all[file3] = lines3
    print(all)
    sorted_all = dict(sorted(all.items(), key=lambda x: x[1], reverse= True))
    print(sorted_all)
    for k, v in sorted_all.items():
        result.write(k.name)
        result.write("\n")
        result.write(str(len(v)))
        result.write("\n")
        result.writelines(v)
        result.write("\n")
with open("Sorted.txt", encoding='utf-8') as final:
    finals = final.read()
    print(finals)