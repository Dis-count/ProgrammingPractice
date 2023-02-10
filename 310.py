# -*- coding: utf-8 -*-

# 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period
# 中等

# LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

# You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

# Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

# Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

# Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.

# Example 1:
# Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
# Output: ["daniel"]
# Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").

# Example 2:
# Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
# Output: ["bob"]
# Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").

# 获得每个员工的全部使用员工卡的时间列表之后，再对每个员工分别判断是否收到系统警告。具体做法是，对于每个员工，从哈希表中获得该员工的全部使用员工卡的时间列表，并将列表排序，然后遍历排序后的列表。如果发现列表中存在三个连续元素中的最大元素与最小元素之差不超过 60，即意味着这三次使用员工卡是在一小时之内发生的，因此因此该员工会收到系统警告。由于只需要知道每个员工是否收到系统警告，因此一旦可以确认某个员工会收到系统警告，即可停止遍历该员工的剩余的使用员工卡的时间

# 使用一个列表存储收到系统警告的员工名字。在得到所有的收到系统警告的员工名字之后，对该列表进行排序，然后返回。

from typing import List
from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        timeMap = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour, minute = int(time[:2]), int(time[3:])
            timeMap[name].append(hour * 60 + minute)
        
        print(timeMap)

        ans = []
        for name, times in timeMap.items():
            times.sort()
            print(f'times: {times}')
            if any(t2 - t1 <= 60 for t1, t2 in zip(times, times[2:])):
                ans.append(name)
        ans.sort()
        return ans

tes = Solution()

keyName = ["alice", "alice", "alice", "bob", "bob", "bob", "bob"] 
keyTime = ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]

tes.alertNames(keyName, keyTime)
