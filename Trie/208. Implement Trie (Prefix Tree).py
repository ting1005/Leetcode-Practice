class Trie:
    def __init__(self):
        self.root = {}
        self.end_word = "#"

    def insert(self, word: str) -> None:
        """
        將 word 插入到 Trie 中
      
        迴圈遍歷 word 中的每個字元
        如果字元不在 node 中，則新增一個空的 Dictionary，並將 node 移動到下一個字元
        最後將 node 的 end_word 設為 "#"，表示這是一個完整的單詞
        args:
            word: str: 要插入的單詞
        return:
            None
        """
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_word] = self.end_word    

    def search(self, word: str) -> bool:
        """
        搜尋 Trie 中是否有 word
        迴圈遍歷 word 中的每個字元
        如果字元不在 node 中，則回傳 False，表示 Trie 中沒有這個單詞，並且將 node 移動到下一個字元
        最後檢查 node 是否有 end_word，如果有則回傳 True，表示 Trie 中有這個單詞
        args:
            word: str: 要搜尋的單詞
        return:
            bool: Trie 中是否有這個單詞
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        搜尋 Trie 中是否有以 prefix 開頭的單詞
        迴圈遍歷 prefix 中的每個字元
        如果字元不在 node 中，則回傳 False，表示 Trie 中沒有這個單詞，並且將 node 移動到下一個字元
        最後回傳 True，表示 Trie 中有以 prefix 開頭的單詞
        args:
            prefix: str: 要搜尋的前綴
        return:
            bool: Trie 中是否有以 prefix 開頭的單詞
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)