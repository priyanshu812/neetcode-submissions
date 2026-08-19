class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sot(str):
            return "".join(sorted(str))
            
        
        vocab = {}
        for i in strs:
            if sot(i) in vocab :
                vocab[sot(i)].append(i)
            else:
                vocab[sot(i)] = [i]
        return list(vocab.values())
