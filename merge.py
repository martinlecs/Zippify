# BASIC CASE - two playlists with even length and no duplicates

import random

# playlist A
A = ["A1","A2","A3","A4","A5","dup"]
# playlist B
B = ["B1","B2","B3","B4","B5","dup"]

print A
print B

# zipped playlist
zipped = []

# shuffle A
random.shuffle(A)
# shuffle B
random.shuffle(B)

# go through playlists and add to zipped playlist
for i in range (0,len(A)):
    if A[i] not in zipped:
        zipped.append(A[i])
    if B[i] not in zipped:
        zipped.append(B[i])


print zipped
