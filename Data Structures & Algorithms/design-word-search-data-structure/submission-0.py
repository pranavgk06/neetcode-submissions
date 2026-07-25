class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True

        

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return node.is_end
            
            c = word[i]

            if c != '.':
                child = node.children[ord(c) - ord('a')]
                if not child:
                    return False
                return dfs(child, i+1)
            else:
                for child in node.children:
                    if child and dfs(child, i+1):
                        return True
                return False
        
        return dfs(self.root,0)
        