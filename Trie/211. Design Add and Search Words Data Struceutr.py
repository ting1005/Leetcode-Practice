class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        加入單詞到 Trie 中
        歷遍每個字元，如果字元不存在於 Trie 中，則新增一個 TrieNode
        最後一個字元的 TrieNode 的 is_end 設為 True
        args:
            word: str, 要加入的單詞
        return: 
            None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        搜尋單詞是否存在於 Trie 中
        args:
            word: str, 要搜尋的單詞
        return:
            bool, 是否存在於 Trie 中
        """
        return self.search_in_node(word, self.root)
    
    def searchInNode(self, word: str, node: TrieNode) -> bool:
        """
        搜尋單詞是否存在於 Trie 中
        歷遍每個字元，如果字元為 '.'，則遍歷所有的子節點
        如果字元不存在於 Trie 中，則返回 False
        最後一個字元的 TrieNode 的 is_end 為 True，則返回 True
        
        args:
            word: str, 要搜尋的單詞
            node: TrieNode, 當前的 TrieNode
        return:
            bool, 是否存在於 Trie 中
        """
        for i, char in enumerate(word):
            if char == '.':
                for child_node in node.children.values():
                    if self.search_in_node(word[i+1:], child_node):
                        return True
                return False
            elif char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_end



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)