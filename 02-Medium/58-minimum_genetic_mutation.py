from collections import deque
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])
        visited = {startGene}
        choices = ['A', 'C', 'G', 'T']
        
        while queue:
            current_gene, mutations = queue.popleft()
            
            if current_gene == endGene:
                return mutations
            
            # Try changing each character
            for i in range(len(current_gene)):
                for char in choices:
                    if current_gene[i] == char:
                        continue
                    
                    # Construct the mutated gene string
                    next_gene = current_gene[:i] + char + current_gene[i+1:]
                    
                    if next_gene in bank_set and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, mutations + 1))
                        
        return -1