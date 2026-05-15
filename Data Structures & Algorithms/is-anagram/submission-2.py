class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_common = {}
        for i in range(len(s)):
            dict_common[s[i]] = dict_common.get(s[i],0) + 1
            dict_common[t[i]] = dict_common.get(t[i],0) - 1

        return all(v == 0 for v in dict_common.values())

        #Above line does same thing as below
        # for v in dict_common.values():
        #     if v != 0:
        #         return False
        # return True


