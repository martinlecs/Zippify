# BASIC CASE - two playlists with even length and no duplicates

import random

# zipped playlist
zipped = []



def merge(A,B):
    # shuffle A
    random.shuffle(A)
    # shuffle B
    random.shuffle(B)
    remove_dups(A,B)
    if (len(A) == len(B)):
        return merge_same_length(A,B)
    else:
        return merge_diff_length(A,B)


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


def merge_diff_length(list1,list2):
    result = []
    for i in range( max(len(list1), len(list2))):
        if i+1 <= len(list1):
            result += [list1[i]]

        if i+1 <= len(list2):
            result += [list2[i]]
    return result


# go through playlists and add to zipped playlist
def merge_same_length(A, B):
    zipped = []
    for i in range (0,len(A)):
        zipped.append(A[i])
        zipped.append(B[i])
    return zipped
