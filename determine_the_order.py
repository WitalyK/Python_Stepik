def deldubl(data):
    seen = set()
    for it in data:
        if it in seen:
            data = data.replace(it, '', 1)
        else:
            seen.add(it)
    return data


def position(seq, test, data):
    out = seq
    for i, s in enumerate(seq):
        for item in data:
            if s in item and test in item:
                aa = out.find(s)
                if item.find(s) > item.find(test):
                    if test in out:
                        bb = out.find(test)
                        if aa < bb:
                            out = out[:aa] + out[aa + 1:]
                            out = out[:bb] + s + out[bb:]
                    else:
                        out = out[:aa] + test + out[aa:]
                else:
                    if test in out:
                        bb = out.find(test)
                        if aa > bb:
                            out = out[:bb] + out[bb + 1:]
                            out = out[:aa] + test + out[aa:]
                    else:
                        out = out[:aa + 1] + test + out[aa + 1:]
    return out


def sorting(word, data):
    letters = list(word)
    out = letters.pop(0)
    for _ in range(2):
        while letters:
            test = letters.pop(0)
            out = position(out, test, data)
            if test not in out:
                letters.append(test)
        letters = list(out)
    return out


def checkio(data):
    data = [deldubl(item) for item in data]
    if len(data) == 1:
        return data[0]
    letters = deldubl(''.join([it for item in data for it in item]))
    if sum(len(it) for it in data) == len(letters):
        return ''.join(sorted(data))
    if (out1 := sorting(letters, data)) == (out2 := sorting(letters[::-1], data)):
        return out1
    else:
        i, wd = [], []
        for idx, (w1, w2) in enumerate(zip(out1, out2)):
            if w1 != w2:
                i.append(idx)
                wd.append(w1)
        wd = sorted(wd)
        for idx, w in zip(i, wd):
            out1 = out1[:idx] + w + out1[idx + 1:]
        return out1


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio(["jhgedba", "jihcba", "jigfdca"]))  # "jihgefdcba"
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
