class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through list
        # each string into a sorted string
        # set that in a dict where [sorted] = ['string']
        # works for single and empty

        sets = defaultdict()
        for word in strs: # O(n)
            sort = str(sorted(word)) # sorting O(m log m), m = average lenght of string
            
            # print(f"{sort} - {word}")
            # print(f"if sets.get({sort}): {bool(sets.get(sort))}")
            
            if sort in sets:  # O(1)
                sets[sort].append(word) # access: O(1), writing: O(1)
            else:
                sets.setdefault(sort, [word]) # O(1)

        # big O: n * m log m
        
        return list(sets.values())
