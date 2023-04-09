# 1125. Smallest Sufficient Team
# 提示
# 困难

# In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

# Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

# For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
# Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

# It is guaranteed an answer exists.


# Example 1:

# Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
# Output: [0,2]

# Example 2:

# Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], 
# people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# Output: [1,2]

from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        sid = {s: i for i, s in enumerate(req_skills)}  # 字符串映射到下标
        n = len(people)
        u = 1 << len(req_skills)
        # f[i+1][j] 表示从前 i 个集合中选择一些集合，并集等于 j，需要选择的最小集合
        f = [[0] * u for _ in range(n + 1)]
        f[0] = [(1 << n) - 1] * u  # 对应记忆化搜索中的 if i < 0: return (1 << n) - 1
        f[0][0] = 0
        for i, skills in enumerate(people):
            mask = 0
            for s in skills:  # 把 skills 压缩成一个二进制数 mask
                mask |= 1 << sid[s]
            for j in range(1, u):
                res = f[i][j]  # 不选 mask
                res2 = f[i][j & ~mask] | (1 << i)  # 选 mask
                f[i + 1][j] = res if res.bit_count() < res2.bit_count() else res2
        res = f[-1][-1]
        print(f'res: {res}')
        return [i for i in range(n) if (res >> i) & 1]  # 所有在 res 中的下标

req_skills = ["algorithms","math","java","reactjs","csharp","aws"]

people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]

test = Solution()
test.smallestSufficientTeam(req_skills, people)

