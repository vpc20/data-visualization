from binarytree import build


def gen_tree_lists(arr):
    def genx(arr, idx):
        if idx < len(arr):
            genx(arr, idx + 1)

            temp_arr = list(arr)
            temp_arr[idx] = None
            # print(temp_arr)
            tree_lists.append(temp_arr)

            genx(temp_arr, idx + 1)

    tree_lists = [arr]
    genx(arr, 1)
    return tree_lists


# lst = gen_tree_lists([4,
#                       2, 6])
# lst = gen_tree_lists([4,
#                       2, 6,
#                       1, 3, 5, 7])
lst = gen_tree_lists([8,
                      4, 12,
                      2, 6, 10, 14,
                      1, 3, 5, 7, 9, 11, 13, 15])
# lst = gen_tree_lists([1,
#                       2, 3,
#                       4, 5, 6, 7,
#                       8, 9, 10, 11, 12, 13, 14, 15,
#                       16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
for e in lst:
    for i in range(len(e)):  # update children of None nodes to None
        if e[i] is None:
            l = i * 2 + 1
            if l < len(e):
                e[l] = None
            r = i * 2 + 2
            if r < len(e):
                e[r] = None
# for i, e in enumerate(lst):
#     print(i, e)

unique_lst = []
for e in lst:  # remove dupes
    if e not in unique_lst:
        unique_lst.append(e)


for i, e in enumerate(unique_lst):
    print(f'********** index: {i} **********')
    print(e)
    root = build(e)
    print(root)

print(f'trees count: {len(unique_lst)}')
