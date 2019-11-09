#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    import numpy
    bihua_list={}
    with open(sys.argv[3],'r') as fr:
        for line in fr:
            line_list=line.split()
            if len(line_list) > 1:
                if not line_list[0] in bihua_list:
                    bihua_list[line_list[0]]=line_list[1]
    with open(sys.argv[1],'r') as fr:
        for line in fr:
            line_list = line.split()
            if len(line_list) > 1 and line_list[0] in bihua_list:
                line_list[1] += bihua_list[line_list[0]]
                print('\t'.join(line_list))
    # piyin = numpy.loadtxt(sys.argv[1], dtype=numpy.unicode)
    # bihua = numpy.loadtxt(sys.argv[1], delimiter="\t", dtype=numpy.unicode, usecols=(0, 1))
    # zipin = numpy.loadtxt("target/frequency.dict", delimiter="\t", dtype=numpy.unicode, usecols=(0, 1))
    # wenzi = piyin[:, 0].tolist()
    # bihua_list = bihua[:, 0].tolist()
    # zipin_list = zipin[:, 0].tolist()
    # for i in range(len(piyin)):
    #     j = bihua_list.index(wenzi[i]) if (wenzi[i] in bihua_list) else -1
    #     if j != -1:
    #         print("{}\t{}{}".format(wenzi[i], piyin[i][1], bihua[j][1]), end="")
            # k = zipin_list.index(wenzi[i]) if (wenzi[i] in zipin_list) else -1
            # if k == -1:
            #     print("\t{}".format(0))
            # else:
            #     print("\t{}".format(zipin[k][1]))
