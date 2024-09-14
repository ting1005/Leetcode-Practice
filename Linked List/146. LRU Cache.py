from typing import Dict, OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        # 使用 OrderedDict 來記錄 key 和 value
        self.data: Dict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        # 如果 key 不在 data 裡面，回傳 -1
        if key not in self.data:
            return -1
        # 如果 key 在 data 裡面，將 key 移到最後面
        else:
            return self.data.setdefault(key, self.data.pop(key))

    def put(self, key: int, value: int) -> None:
        
        try:
            # 將 key 移到最後面
            self.data.move_to_end(key)
            self.data[key] = value
        except KeyError:
            # 如果 key 不在 data 裡面，將 key 加入 data 裡面
            self.data[key] = value
            if len(self.data) > self.capacity:
                self.data.popitem(last=False)