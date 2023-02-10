# 1233. Remove Sub-Folders from the Filesystem
# 中等

# Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

# If a folder[i] is located within another folder[j], it is called a sub-folder of it.

# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

# For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 

# Example 1:

# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
# Example 2:

# Input: folder = ["/a","/a/b/c","/a/b/d"]
# Output: ["/a"]
# Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
# Example 3:

# Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# Output: ["/a/b/c","/a/b/ca","/a/b/d"]

#  排序

from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        for i in range(1, len(folder)):
            if not ((pre := len(ans[-1])) < len(folder[i]) and ans[-1] == folder[i][:pre] and folder[i][pre] == "/"):
                ans.append(folder[i])
        return ans
