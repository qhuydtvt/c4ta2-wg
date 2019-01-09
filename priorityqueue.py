class QueueItem:
  def __init__(self, c, p):
    self.content = c
    self.priority = p
  
  def __str__(self):
    return f"({self.content},{self.priority})"

class PriorityQueue:
  def __init__(self):
    self.items = []
  
  def _swap(self, i, j):
    self.items[i], self.items[j] = self.items[j], self.items[i]

  def _up_perculate(self, i): # internal
    if i <= 0:
      return
    parent_index = (i - 1) // 2
    if self.items[i].priority < self.items[parent_index].priority:
      self._swap(i, parent_index)
      self._up_perculate(parent_index) # non fruitful
    else:
      return
  
  def push(self, c, p):
    self.items.append(QueueItem(c, p)) # insert new item
    self._up_perculate(len(self.items) - 1) # reorganize
  
  def _exists(self, i):
    return i < len(self.items)

  def _down_perculate(self, i):
    left = i * 2 + 1
    right = i * 2 + 2
    smaller_child_index = -1
    if not self._exists(left) and not self._exists(right):
      return
    if self._exists(left):
      if self._exists(right):
        if self.items[left].priority > self.items[right].priority:
          smaller_child_index = right
        else:
          smaller_child_index = left
        if self.items[i].priority > self.items[smaller_child_index].priority:
          self._swap(i, smaller_child_index)
          self._down_perculate(smaller_child_index)
      else:
        if self.items[i].priority > self.items[left].priority:
          self._swap(i, left)
          self._down_perculate(left)

  def remove(self):
    if len(self.items) > 0:
      top = self.items.pop(0)
      if len(self.items) > 0:
        last = self.items.pop()
        self.items.insert(0, last)
        self._down_perculate(0)
      return top
    else:
      return None
  
  def __str__(self):
    return "".join(str(item) for item in self.items)

if __name__ == "__main__":
  pq = PriorityQueue()
  pq.push("A", 1)
  pq.push("B", 2)
  pq.push("B", 4)
  print(pq)

  pq.push("D", 1.5)
  print(pq)
  
  pq.push("E", 6)
  pq.push("F", 7)
  print(pq)

  pq.push("G", -1)
  print(pq)

  x = pq.remove()
  print(x)
  print(pq)

  x = pq.remove()
  print(x)
  print(pq)

  x = pq.remove()
  print(x)
  print(pq)

  x = pq.remove()
  print(x)
  print(pq)