# BASIC CASE - two playlists with even length and no duplicates

import random

# remove duplicates in two playlists
def remove_dups(A,B):
    seen = {}
    for elem in A:
        if elem not in seen.keys():
            seen[elem] = 1
        else:
            A.remove(elem)
    for elem in B:
        if elem not in seen.keys():
            seen[elem] = 1
        else:
            B.remove(elem)


# playlist A
A = ["A1","A2","A3","A4","A5","dup", "A6"]
# playlist B
B = ["B1","B2","B3","B4","B5","dup"]

remove_dups(A,B)
print A
print B

# zipped playlist
zipped = []

# shuffle A
random.shuffle(A)
# shuffle B
random.shuffle(B)

def merge_diff_length(list1,list2):
    num = min(len(list1), len(list2))
    result = [None]*(num*2)
    result[::2] = list1[:num]
    result[1::2] = list2[:num]
    result.extend(list1[num:])
    result.extend(list2[num:])
    print result


# go through playlists and add to zipped playlist
def merge_same_length():
    for i in range (0,len(A)):
        zipped.append(A[i])
        zipped.append(B[i])
    print zipped

merge_diff_length(A,B)
