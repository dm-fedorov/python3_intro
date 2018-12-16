# intersect.py
def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

if __name__ == '__main__':
    print(intersect([1, 2, 4], [2, 5, 7]))
    print(intersect("AAAAB", "CCCCCBC"))



