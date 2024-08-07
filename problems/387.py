"""
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return 
its index. If it does not exist, return -1.
"""

# TIME: O(n^2) Space: O(n)
# def firstUniqChar(s: str) -> int:
#     res = -1
#     repeated_chars = set()
#
#     for i in range(len(s)):
#         if s[i] not in repeated_chars:
#             for j in range(i + 1, len(s)):
#                 if s[j] == s[i]:
#                     repeated_chars.add(s[i])
#                     break
#             if s[i] not in repeated_chars:
#                 return i
#
#     return res

# TIME: O(n^2) Space: O(1)
# def firstUniqChar(s: str) -> int:
#     for i in range(len(s)):
#         isRepeated = False
#         for j in range(len(s)):
#             if i != j and s[i] == s[j]:
#                 isRepeated = True
#                 break
#         if not isRepeated:
#             return i
#     return -1

# TIME: O(n) Space: O(1)
def firstUniqChar(s: str) -> int:
    freq = [-1] * 26

    for i, c in enumerate(s):
        freq[ord(c) - ord('a')] = i if freq[ord(c) - ord('a')] == -1 else -2

    res = 1000001
    for i in freq:
        if i >= 0:
            res = min(res, i)
    return res if res != 1000001 else -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))
