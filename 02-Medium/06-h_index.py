class Solution(object):
    def hIndex(self, citations):
        # sort in descending order to easily compare citation counts
        # against the number of papers
        citations.sort(reverse = True)
        h = 0
        for i, val in enumerate(citations):
            # i + 1 is the number of papers considered so far
            # if the current paper's citations are >= the rank(i + 1),
            # it contributes to the h-index.
            if val >= i + 1:
                h = i + 1
            else:
                # Once the condition fails, we don't need to check futher
                break
        return h