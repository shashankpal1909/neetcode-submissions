class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        n = len(people)
        i, j = 0, n - 1
        boats = 0

        while i < j:
            if people[i] + people[j] <= limit:
                # new boat with i, j
                i, j = i + 1, j - 1
            else:
                # new boat with j
                j -= 1

            boats += 1
        
        if i == j:
            # new boat with i
            boats += 1

        return boats
