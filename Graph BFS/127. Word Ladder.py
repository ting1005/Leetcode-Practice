from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        patterns = defaultdict(set)
        
        # 預處理 wordList
        # 將每個 word 的每個字母都替換成 *，並且將這個字串加入到 patterns 中
        # 例如 word = "hit"，則將 "*it"、"h*t"、"hi*" 加入到 patterns
        for word in wordList:
            for i in range(len(word)):
                form = word[:i] + "*" + word[i+1:]
                patterns[form].add(word)
    
        # 建立圖形結構，生成一個以單詞為key，value 為與 key 相連的單詞的 Dictionary
        graph = defaultdict(list)
        for word in wordList:
            localSet = set()
            for i in range(len(word)):
                form = word[:i] + "*" + word[i+1:]
                localSet |= patterns[form]
            graph[word] = list(localSet)
        
        # 使用 BFS 來尋找最短的步數
        queue = deque([beginWord])
        step = 0
        visited = set([beginWord])
        while queue:
            step += 1
            size = len(queue)
            for _ in range(size):
                choosenWord = queue.popleft()
                if choosenWord == endWord:
                    return step
                for nextWord in graph[choosenWord]:
                    if nextWord in visited:
                        continue
                    visited.add(nextWord)
                    queue.append(nextWord)
        return 0