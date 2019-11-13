import numpy as np
np.set_printoptions(threshold=np.inf)

Song1 = open("Song1_Folsom_Prison.txt", "r+").readlines()
Song2 = open("Song2_Crescent_City_Blues.txt", "r+").readlines()


def decode(index):
    op = ''
    if index == 0:
        op = 'sub'
    if index == 1:
        op = 'ins'
    if index == 2:
        op = 'del'
    return op


def minimizer(i, j, s):
    possible = [s[i-1][j-1], s[i-1][j], s[i][j-1]]
    val = min(possible)
    index = possible.index(val)
    return val, index


# Turn x into y
def extractAlignments(S, x, y, c_ins, c_del, c_sub):
    ''' S: optimal cost matrix
        x, y: strings
        c_...: cost of operations
        returns vector of optimal edits to make x into y
    '''


# driver for dp
def alignStrings(x, y, c_ins, c_del, c_sub):
    '''
        returns optimal cost matrix S
    '''
    shape = (len(x), len(y))
    s = np.zeros(shape, dtype=int)
    p = np.zeros(shape, dtype=int)
    print(shape)

    for i in range(len(x)):
        for j in range(len(y)):
            if i > 0 or j > 0:
                cost, op = minimizer(i, j, s)
                if op == 0:
                    p[i][j] = op
                    s[i][j] = cost + c_sub
                if op == 1:
                    p[i][j] = op
                    s[i][j] = cost + c_ins
                if op == 2:
                    p[i][j] = op
                    s[i][j] = cost + c_del

    return s, p


def commonSubstrings(x, L, a):
    '''
        x: string
        L: integer
        a: optimal sequence of edits to make x into y
    '''


s, p = alignStrings(Song1[0], Song2[0], 1, 1, 1)
# np.savetxt("foo.csv", s, delimiter=",", fmt="%d")


