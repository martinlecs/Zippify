# BASIC CASE - two playlists with even length and no duplicates

import random

# remove duplicates in two playlists
def remove_dups(A,B):
    seen = {}
    # remove duplicates from longer list
    if len(A) >= len(B):
        for elem in B:
            if elem not in seen.keys():
                seen[elem] = 1
            else:
                B.remove(elem)
        for elem in A:
            if elem not in seen.keys():
                seen[elem] = 1
            else:
                A.remove(elem)


    else:
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
    result = []
    for i in range( max(len(list1), len(list2))):
        if i+1 <= len(list1):
            result += [list1[i]]

        if i+1 <= len(list2):
            result += [list2[i]]
    print result


# go through playlists and add to zipped playlist
def merge_same_length():
    for i in range (0,len(A)):
        zipped.append(A[i])
        zipped.append(B[i])
    print zipped

merge_diff_length(A,B)
