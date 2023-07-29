from typing import List
from collections import defaultdict

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)
        skill_to_idx = {skill: i for i, skill in enumerate(req_skills)}
        people_bitmask = [0] * n
        for i, skills in enumerate(people):
            for skill in skills:
                if skill in skill_to_idx:
                    people_bitmask[i] |= (1 << skill_to_idx[skill])

        dp = [float('inf')] * (1 << m)
        dp[0] = 0
        parent = [0] * (1 << m)

        for bitmask in range(1, 1 << m):
            count = float('inf')
            last_person = -1

            for i in range(n):
                if bitmask & people_bitmask[i] and dp[bitmask ^ people_bitmask[i]] + 1 < count:
                    count = dp[bitmask ^ people_bitmask[i]] + 1
                    last_person = i

            if count < dp[bitmask]:
                dp[bitmask] = count
                parent[bitmask] = last_person

        current_mask = (1 << m) - 1
        result = []
        while current_mask != 0:
            result.append(parent[current_mask])
            current_mask ^= people_bitmask[parent[current_mask]]

        return result[::-1]
    
    

if __name__ == '__main__':
    req_skills = ["mwobudvo","goczubcwnfze","yspbsez","pf","ey","hkq"]
    people = [[],["mwobudvo"],["hkq"],["pf"],["pf"],["mwobudvo","pf"],[],["yspbsez"],[],["hkq"],[],[],["goczubcwnfze","pf","hkq"],["goczubcwnfze"],["hkq"],["mwobudvo"],[],["mwobudvo","pf"],["pf","ey"],["mwobudvo"],["hkq"],[],["pf"],["mwobudvo","yspbsez"],["mwobudvo","goczubcwnfze"],["goczubcwnfze","pf"],["goczubcwnfze"],["goczubcwnfze"],["mwobudvo"],["mwobudvo","goczubcwnfze"],[],["goczubcwnfze"],[],["goczubcwnfze"],["mwobudvo"],[],["hkq"],["yspbsez"],["mwobudvo"],["goczubcwnfze","ey"]]
    resultExpected = [12,23,39]
    result = Solution().smallestSufficientTeam(req_skills, people)
    print(f"{result} should be {resultExpected}")