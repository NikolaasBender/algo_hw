import numpy as np
import time
import matplotlib.pyplot as plt
# np.set_printoptions(threshold=np.inf)

Song1 = open("Song1_Folsom_Prison.txt", "r+").readlines()[0]
Song2 = open("Song2_Crescent_City_Blues.txt", "r+").readlines()[0]

# Song1 = "hello"
# Song2 = "bhello"

C_INS = 1
C_DEL = 1
C_SUB = 1




def decode(ops):
    '''
        Decode is to turn the operation codes back into human readable words.
        Its secondary function is as a refrence point to make sure all uses
        of the "code" are consistent. 
    '''
    op = []
    for act in ops:
        if act == 0:
            op.append('sub')
        if act == 1:
            op.append('ins')
        if act == 2:
            op.append('del')
        if act == 3:
            op.append("no-op")
    return op


# Turn x into y
def extractAlignments(S, x, y):
    '''
        This is one of the most hideous pieces of code I have ever produced,
        you're welcome. This goes through the cost matrix S and back solves
        to get from the bottom right corner back to the top left area. 
    '''
    print("extract alignments")
    ops = []
    i = len(x)
    j = len(y)
    while i > 0 and j > 0:
        # print(i, j)
        if x[i - 1] == y[j - 1]:
            ops.append(3)
            i -= 1
            j -= 1
        else:
            sub_val = S[i - 1][j - 1] + C_SUB
            ins_val = S[i][j - 1] + C_INS
            del_val = S[i - 1][j] + C_DEL
            
            if sub_val < ins_val and sub_val < del_val:
                ops.append(0)
                i -= 1
                j -= 1
            elif ins_val < sub_val and ins_val < del_val:
                ops.append(1)
                j -= 1
            elif del_val < ins_val and del_val < sub_val:
                ops.append(2)
                i -= 1
            else:
                if sub_val == ins_val == del_val:
                    randy = np.random.randint(3)
                    if randy == 0:
                        ops.append(0)
                        i -= 1
                        j -= 1
                    elif randy == 1:
                        ops.append(1)
                        j -= 1
                    elif randy == 2:
                        ops.append(2)
                        i -= 1
                elif sub_val == del_val:
                    randy = np.random.randint(2)
                    if randy == 0:
                        ops.append(0)
                        i -= 1
                        j -= 1
                    elif randy == 1:
                        ops.append(2)
                        i -= 1
                elif ins_val == sub_val:
                    randy = np.random.randint(2)
                    if randy == 0:
                        ops.append(0)
                        i -= 1
                        j -= 1
                    elif randy == 1:
                        ops.append(1)
                        j -= 1
                elif ins_val == del_val:
                    randy = np.random.randint(2)
                    if randy == 0:
                        ops.append(1)
                        j -= 1
                    elif randy == 1:
                        ops.append(2)
                        i -= 1
    ops.reverse()
    return ops


# driver for dp
def alignStrings(x, y):
    '''
        returns optimal cost matrix S
        and the p matrix
    '''
    print("align strings")
    shape = (len(x) + 1, len(y) + 1)
    # print(shape)
    s = np.zeros(shape, dtype=int)

    for i in range(0, len(x) + 1):
        s[i][0] = i
        for j in range(1, len(y) + 1):
            s[0][j] = j
            if i > 0 or j > 0:
                if x[i - 1] == y[j - 1]:
                    s[i][j] = s[i - 1][j - 1]
                else:
                    s[i][j] = min(s[i - 1][j - 1] + C_SUB, 
                                  s[i][j - 1] + C_INS, 
                                  s[i - 1][j] + C_DEL)

    return s


def commonSubstrings(x, L, a):
    '''
        x: string
        L: integer
        a: optimal sequence of edits to make x into y
    '''
    print("common substrings")
    sub_strings = []
    possible_str = []
    i = 0
    for j in range(len(a)):
        if i in range(0, len(x)):
            # NO-OP
            if a[j] == 3:
                possible_str.append(x[i])
                i += 1
            # INSERT
            elif a[j] == 1:
                if len(possible_str) >= L:
                    sub_strings.append(''.join(possible_str))
                possible_str = []
            # SUB or DELETE
            else:
                if len(possible_str) >= L:
                    sub_strings.append(''.join(possible_str))
                possible_str = []
                i += 1
    if len(possible_str) > 0:
        sub_strings.append(''.join(possible_str))
    return sub_strings


def wrap(s1, s2, ci, cd, cs, subl):
    '''
        s1: X string
        s2: Y string
        ci: Cost of Insert
        cd: Cost of Delete
        cs: Cost of Substitute
        subl: Length of common substring
    '''
    s1 = " " + s1
    s2 = " " + s2
    # print(s1, s2)
    C_DEL = cd
    C_SUB = cs
    C_INS = ci
    s = alignStrings(s1, s2)
    # print(s, "\n")
    align = extractAlignments(s, s1, s2)
    # print(decode(align))
    com_str = commonSubstrings(s1, subl, align)
    return com_str


_ = wrap("exponential", "polynomial", 2, 1, 2, 2)

# asymptototic analysis
# times = []
# print("testing")
# for i in range(10, len(Song1)):
#     start = time.time()
#     _ = wrap(Song1[:i], Song2, 1, 1, 1, 4)
#     times.append(time.time() - start)

# tests = [i for i in range(len(times))]
# plt.plot(tests, times)
# plt.show()

plagerism = wrap(Song1, Song2, 1, 1, 1, 10)
total = ''
table = []
for string in plagerism:
    table.append([len(string), string])
    total.join(string)

s2_len = len(Song2)
plag_len = len(plagerism)
print(s2_len / plag_len, "% plagerism")
F = open('workfile.txt','w') 
for row in table:
    F.write("[" + str(row[0]) + " | " + row[1] + "]\n")
F.close()
