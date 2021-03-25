from itertools import combinations

from binarytree import build

# values = [7, 3, 2, 6, 9, None, 1, 5, 8]

# values = [4,
#           2, 6,
#           1, 3, 5, 7]

# values = [1,
#           2, 3,
#           4, 5, 6, 7,
#           8, 9, 10, 11, 12, 13, 14, 15]

# values = [8,
#           4, 12,
#           2, 6, 10, 14,
#           1, 3, 5, 7, 9, 11, 13, 15]

values = [3,
          5, 1,
          6, 2, 9, 8,
          None, None, 7, 4]
root = build(values)
print(root)

# arr = [4, 2, 6, 1, 3, 5, 7]
# idxs = list(range(len(arr) - 1))
# print(idxs)
# arrset = set()
# new_arr_arr = []
#
# for r in range(1, len(arr)):
#     for comb in combinations(idxs, r):
#         new_arr = arr.copy()
#         for idx in comb:
#             new_arr[idx + 1] = 0
#         for i in range(len(new_arr)):
#             if new_arr[i] is 0:
#                 l = i * 2 + 1
#                 if l < len(new_arr):
#                     new_arr[l] = 0
#                 r = i * 2 + 2
#                 if r < len(new_arr):
#                     new_arr[r] = 0
#         if new_arr not in new_arr_arr:
#             new_arr_arr.append(new_arr)
#
# # print(len(new_arr_arr))
# xarr = sorted(new_arr_arr)
# for arr in xarr:
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             arr[i] = None
#
# for e in xarr:
#     root = build(e)
#     print(root)

