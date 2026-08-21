class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        n = len(people)
        boat = 0

        l,r = 0,n-1

        while l<=r:
            if(people[l]+people[r]>limit):
                boat+=1
                r-=1
            else:
                l+=1
                r-=1
                boat+=1
        return boat