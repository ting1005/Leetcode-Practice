class Solution:
  def isSubsequence(s: str, t: str) -> bool:
      i, j = 0, 0

      # 透過快慢指針，比對 s 和 t 的字元
      # 每當 s[i] 和 t[j] 相同，則 i 往前移動，否則只有 j 往前移動
      while i < len(s) and j < len(t):
          if s[i] == t[j]:
              i += 1
          j += 1

      # 最後檢查 i 是否走完了 s 的長度
      return i == len(s)
