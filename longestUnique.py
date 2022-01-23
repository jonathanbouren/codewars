# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.


# def longest(a1, a2):
#     res = []
#     res2 = ''
#     word = a1 + a2
#     for i in word:
#         if i in res:
#             pass
#         else:
#             res += i
#     res.sort()
#     for i in res:
#         res2 += i
#     print(res2)

def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))
print(longest("aretheyhere", "yestheyarehere")) #"aehrsty"