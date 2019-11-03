#!/usr/bin/python3


if __name__ == "__main__":
    import numpy as np

    piyin = np.loadtxt("拼音.txt", delimiter="\t", dtype=np.unicode)
    bihua = np.loadtxt("笔画.txt", delimiter="\t", dtype=np.unicode)
    zipin = np.loadtxt("频率.txt", delimiter="\t", dtype=np.unicode)

    wenzi = piyin[:, 0].tolist()
    bihua_list = bihua[:, 0].tolist()
    zipin_list = zipin[:, 0].tolist()
    for i in range(len(piyin)):
        j = bihua_list.index(wenzi[i]) if (wenzi[i] in bihua_list) else -1
        k = zipin_list.index(wenzi[i]) if (wenzi[i] in zipin_list) else -1
        print("{}\t{}".format(wenzi[i], piyin[i][1]), end="")
        if j != -1:
            print("{}".format(bihua[j][1]), end="")
        if k == -1:
            print("\t{}".format(0))
        else:
            print("\t{}".format(zipin[k][1]))
