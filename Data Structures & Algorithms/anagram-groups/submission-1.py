class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        visited = set()
        if len(strs) == 0 or len(strs) == 1:
            return [strs]
        else:
            for i in range(len(strs)):
                if strs[i] in visited:
                    continue
                seen_list = []
                seen_list.append(strs[i])
                for j in range(i+1, len(strs)):
                    if (''.join(sorted(strs[i])) == ''.join(sorted(strs[j]))) and strs[j] not in result:
                        seen_list.append(strs[j])
                        visited.add(strs[j])
                result.append(seen_list)
        return result
        