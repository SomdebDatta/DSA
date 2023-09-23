from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff_list = list()
        diff_list.append(gas[0] - cost[0])
        aggregate = gas[0] - cost[0]

        for i in range(1, n):
            diff_list.append(gas[i] - cost[i])
            aggregate += gas[i] - cost[i]
        if aggregate >= 0:
            start = max(diff_list)
            start = diff_list.index(start)
            return start
        return -1

    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start_pos = 0
        import pdb

        pdb.set_trace()
        while start_pos < n:
            dest = start_pos + 1
            tank = gas[start_pos]
            while dest != start_pos:
                if tank - cost[dest - 1] >= 0:
                    tank = tank - cost[dest - 1] + gas[dest]
                else:
                    start_pos += 1
                    break

    def canCompleteCircuit3(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        start_pos, tank = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start_pos = i + 1
                tank = 0
        return start_pos


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
gas1 = [5, 8, 2, 8]
cost1 = [6, 5, 6, 6]
obj = Solution()
print(obj.canCompleteCircuit3(gas, cost))
# print(obj.canCompleteCircuit(gas1, cost1))
