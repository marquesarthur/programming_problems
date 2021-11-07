class Solution:
    
    def _can_add(self, f, subfolders, folder_map):
        k = len(subfolders)
        for i in range(1, k+1):
            test = ''.join(reversed(f)).split("/", i)[-1]
            test = ''.join(reversed(test))
            if test in folder_map:
                return False
        return True
            
    
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        # sorts by folder length and then lexicographically 
        sorted_folder = sorted(folder, key = lambda k: (len(k.split("/")), k) )
        
        folder_map = set()
        for f in sorted_folder:
            subfolders = f.split("/")
            if self._can_add(f, subfolders, folder_map):
                folder_map.add(f)
                
        result = []
        for i in range(len(folder)):
            if folder[i] in folder_map:
                result.append(folder[i])
                
        return result
                
        
        
