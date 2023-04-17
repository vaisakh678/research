# import os
# from os.path import join, isdir

# ROOT = '/Users/vaisakh/research_final_codebase/ASL_Dataset/Train'

# img_paths = []
# for label in os.listdir(ROOT):
#     if not isdir(join(ROOT, label)): continue;
#     img_paths.append(label)

# img_paths.sort()

# print(img_paths)


s = {'A': 0,
 'B': 1,
 'C': 2,
 'D': 3,
 'E': 4,
 'F': 5,
 'G': 6,
 'H': 7,
 'I': 8,
 'J': 9,
 'K': 10,
 'L': 11,
 'M': 12,
 'N': 13,
 'O': 14,
 'P': 15,
 'Q': 16,
 'R': 17,
 'S': 18,
 'Space': 19,
 'T': 20,
 'U': 21,
 'V': 22,
 'W': 23,
 'X': 24,
 'Y': 25,
 'Z': 26}


print(list(s.keys()))