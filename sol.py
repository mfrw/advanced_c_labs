import sys

def solution(fname):
    test = []
    fs = []

    with open(fname) as f:
        ar = fs
        for line in f.readlines():
            if line.strip() == '':
                ar = test
                continue
            ar.append(line)
    sol = []
    for i in test:
        if not i in fs:
            sol.append("NO  :"+i)
        else:
            sol.append("YES :"+i)
    return sol


if __name__ == '__main__':
    fname = sys.argv[1]
    sol = solution(fname)
    for i in sol:
        print i,

