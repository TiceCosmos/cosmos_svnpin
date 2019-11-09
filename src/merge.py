#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    import numpy

    bihua_list = {}
    with open(sys.argv[3], "r") as fr:
        for line in fr:
            line_list = line.strip("\n").split("\t")
            if len(line_list) > 1 and (not line_list[0] in bihua_list):
                bihua_list[line_list[0]] = line_list[1]
    data_list = {}
    with open(sys.argv[1], "r") as fr:
        for line in fr:
            line_list = line.strip("\n").split("\t")
            if len(line_list) > 1 and line_list[0] in bihua_list:
                tmp = line_list[1] + bihua_list[line_list[0]]
                data_list[line_list[0] + line_list[1]] = tmp
                line_list[1] = tmp
                print("\t".join(line_list))
    with open(sys.argv[2], "r") as fr:
        for line in fr:
            line_list = line.strip("\n").split("\t")
            if len(line_list) < 2:
                continue
            word_list = list(line_list[0])
            code_list = line_list[1].split()
            if len(word_list) != len(code_list):
                continue
            keys_list = [word_list[i] + code_list[i] for i in range(0, len(word_list))]
            tmp_stat = True
            tmp_list = []
            for key in keys_list:
                if not key in data_list:
                    tmp_stat = False
                    break
                tmp_list.append(data_list[key])
            if tmp_stat:
                print("{}\t{}".format(line_list[0], " ".join(tmp_list)))
