import re

pte = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7,
       'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14,
       'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20, 'Sc': 21,
       'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, 'Ni': 28,
       'Cu': 29, 'Zn': 30, 'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35,
       'Kr': 36, 'Rb': 37, 'Sr': 38, 'Y': 39, 'Zr': 40, 'Nb': 41, 'Mo': 42,
       'Tc': 43, 'Ru': 44, 'Rh': 45, 'Pd': 46, 'Ag': 47, 'Cd': 48, 'In': 49,
       'Sn': 50, 'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54, 'Cs': 55, 'Ba': 56,
       'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60, 'Pm': 61, 'Sm': 62, 'Eu': 63,
       'Gd': 64, 'Tb': 65, 'Dy': 66, 'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70,
       'Lu': 71, 'Hf': 72, 'Ta': 73, 'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77,
       'Pt': 78, 'Au': 79, 'Hg': 80, 'Tl': 81, 'Pb': 82, 'Bi': 83, 'Po': 84,
       'At': 85, 'Rn': 86, 'Fr': 87, 'Ra': 88, 'Ac': 89, 'Th': 90, 'Pa': 91,
       'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95, 'Cm': 96, 'Bk': 97, 'Cf': 98,
       'Es': 99, 'Fm': 100, 'Md': 101, 'No': 102, 'Lr': 103, 'Rf': 104,
       'Db': 105, 'Sg': 106, 'Bh': 107, 'Hs': 108, 'Mt': 109, 'Ds': 110,
       'Rg': 111, 'Cn': 112, 'Uut': 113, 'Fl': 114, 'Uup': 115, 'Lv': 116,
       'Uus': 117, 'Uuo': 118}

t = {'s': 2, 'p': 6, 'd': 10, 'f': 14, 'g': 18, 'h': 22, 'i': 26}

un = {'1': '\u00B9', '2': '\u00B2', '3': '\u00B3', '4': '\u2074', '5': '\u2075',
      '6': '\u2076', '7': '\u2077', '8': '\u2078', '9': '\u2079', '0': '\u2070'}

levels = ('1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d',
          '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p', '8s')

etr = {24: ['3d4 4s2', '3d5 4s1'], 29: ['3d9 4s2', '3d10 4s1'],
       41: ['4d3 5s2', '4d4 5s1'], 42: ['4d4 5s2', '4d5 5s1'], 44: ['4d6 5s2', '4d7 5s1'],
       45: ['4d7 5s2', '4d8 5s1'], 46: ['4d8 5s2', '4d10'], 47: ['4d9 5s2', '4d10 5s1'],
       78: ['5d8 6s2', '5d9 6s1'], 79: ['5d9 6s2', '5d10 6s1'], 57: ['4f1 6s2', '5d1 6s2'],
       58: ['4f2 6s2', '4f1 5d1 6s2'], 64: ['4f8 6s2', '4f7 5d1 6s2'],
       89: ['5f1 7s2', '6d1 7s2'], 90: ['5f2 7s2', '6d2 7s2'],
       91: ['5f3 7s2', '5f2 6d1 7s2'], 92: ['5f4 7s2', '5f3 6d1 7s2'],
       93: ['5f5 7s2', '5f4 6d1 7s2'], 96: ['5f8 7s2', '5f7 6d1 7s2'],
       103: ['6d1 7s2', '7s2 7p1']}


def unics(lis):
    return ''.join([un[item] for item in lis])


def exept_to_rule(orbs, els, n):
    l1 = etr[n][0].split()
    l2 = etr[n][1].split()
    regex = f"{' '.join([i[:2]+unics(i[2:]) for i in l1])}$"
    orb = re.sub(regex, ' '.join([i[:2]+unics(i[2:]) for i in l2]), orbs)
    l1 = [lastseq(t[it[1]], int(it[2:]) - t[it[1]]) for it in l1]
    l2 = [lastseq(t[it[1]], int(it[2:]) - t[it[1]]) for it in l2]
    el = els.split()
    for it1, it2 in zip(l1, [l2[0], l2[-1]]):
        for i in reversed(range(len(el))):
            if el[i] == it1:
                el[i] = it2
                break
    if len(l2) == 3:
        el.append(l2[1])
    return orb, ' '.join(el)


def noblegas(s, n):
    if n < 3:
        return s
    s = s.split()
    if n > 86:
        pref = '[Rn] '
        s = s[15:]
    elif n > 54:
        pref = '[Xe] '
        s = s[11:]
    elif n > 36:
        pref = '[Kr] '
        s = s[8:]
    elif n > 18:
        pref = '[Ar] '
        s = s[5:]
    elif n > 10:
        pref = '[Ne] '
        s = s[3:]
    else:
        pref = '[He] '
        s = s[1:]
    return pref + ' '.join(sorted(s, key=lambda x: x[0]))


def lastseq(num, m):
    m = num + m
    l = [0] * (num // 2)
    while m > 0:
        for i in range(num // 2):
            l[i] += 1
            m -= 1
            if m == 0:
                return ''.join([str(item) for item in l])


def checkio(element):
    elnum = pte[element]
    m = elnum
    el = ''
    orb = ''
    for level in levels:
        num = t[level[1]]
        m -= num
        if m == 0:
            el += ' ' + '2' * (num // 2)
            orb += ' ' + level + unics(str(num))
            return [str(elnum), noblegas(orb.strip(), elnum), el.strip()]
        elif m < 0:
            el += ' ' + lastseq(num, m)
            orb += ' ' + level + unics(str(num + m))
            el = el.strip()
            orb = noblegas(orb.strip(), elnum)
            if elnum in etr:
                orb, el = exept_to_rule(orb, el, elnum)
            return [str(elnum), orb, el]
        else:
            el += ' ' + '2' * (num // 2)
            orb += ' ' + level + unics(str(num))


if __name__ == '__main__':
    print(checkio('Gd'))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (checkio('H') == ["1", u"1s¹", "1"]), "First Test - 1s¹"
    assert (checkio('He') == ["2", u"1s²", "2"]), "Second Test - 1s²"
    assert (checkio('Al') == ["13", u"[Ne] 3s² 3p¹", "2 2 222 2 100"]), "Third Test - 1s² 2s² 2p⁶ 3s² 3p¹"
    assert (checkio('O') == ["8", u"[He] 2s² 2p⁴", "2 2 211"]), "Fourth Test - 1s² 2s² 2p⁴"
    assert (checkio('Li') == ["3", u"[He] 2s¹", "2 1"]), "Fifth Test - 1s² 2s¹"

    print('All done!')
