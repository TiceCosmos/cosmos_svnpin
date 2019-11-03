#!/usr/bin/python3


if __name__ == "__main__":
    import numpy as np

    piyin = np.loadtxt("target/pinyin.dict", delimiter="\t", dtype=np.unicode, usecols=(0, 1))
    bihua = np.loadtxt("target/stroke.dict", delimiter="\t", dtype=np.unicode, usecols=(0, 1))
    zipin = np.loadtxt("target/frequency.dict", delimiter="\t", dtype=np.unicode, usecols=(0, 1))

    wenzi = piyin[:, 0].tolist()
    bihua_list = bihua[:, 0].tolist()
    zipin_list = zipin[:, 0].tolist()
    for i in range(len(piyin)):
        j = bihua_list.index(wenzi[i]) if (wenzi[i] in bihua_list) else -1
        if j != -1:
            print("{}\t{}{}".format(wenzi[i], piyin[i][1], bihua[j][1]), end="")
            k = zipin_list.index(wenzi[i]) if (wenzi[i] in zipin_list) else -1
            if k == -1:
                print("\t{}".format(0))
            else:
                print("\t{}".format(zipin[k][1]))
