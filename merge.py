# BASIC CASE - two playlists with even length and no duplicates

import random

# playlist A
A = ["A1","A2","A3","A4","A5"]
# playlist B
B = ["B1","B2","B3","B4","B5"]

# zipped playlist
zipped = []

# shuffle A
random.shuffle(A)
# shuffle B
random.shuffle(B)

# go through playlists and add to zipped playlist
for i in range (0,len(A)):
    zipped.append(A[i])
    zipped.append(B[i])

print zipped

# shows a user's playlists (need to be authenticated via oauth)
