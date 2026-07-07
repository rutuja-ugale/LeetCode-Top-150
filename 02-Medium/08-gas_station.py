class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        # if total gas is less than total cost, completion is impossible
        if sum(gas) < sum(cost):
            return -1
        total_tank = 0
        starting_station = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            # if tank drops below 0, current start station is invalid
            if total_tank < 0:
                # reset starting station to the next one
                starting_station = i + 1
                # reset tank for the new start
                total_tank = 0
        return starting_station