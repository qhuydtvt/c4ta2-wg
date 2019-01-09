class Vertex:
  def __init__(self, c, n=None):
    self.content = c
    self.next = n
    self.edge_head = None
  
  def add_edge(self, t, w):
    if self.edge_head is None:
      self.edge_head = Edge(t, w)
    else:
      new_edge = Edge(t, w, self.edge_head)
      self.edge_head = new_edge
  
  def __str__(self):
    ret = str(self.content)
    if self.edge_head is not None:
      ret += "->("
      edge = self.edge_head
      while edge is not None:
        ret += str(edge)
        if edge.next is not None:
          ret += ","
        edge = edge.next  
      ret += ")"
    return ret
    
class Edge:
  def __init__(self, t, w, n=None):
    self.target = t
    self.weight = w
    self.next = n
  
  def __str__(self):
    return f"{self.weight}-{self.target.content}"

class WeightedGraph:
  def __init__(self):
    self.vertex_head = None
  
  def add_vertex(self, c):
    if self.vertex_head is None:
      self.vertex_head = Vertex(c)
    else:
      new_vertex = Vertex(c, self.vertex_head)
      self.vertex_head = new_vertex
  
  def _find(self, c):
    vertex = self.vertex_head
    while vertex is not None:
      if vertex.content == c:
        return vertex
      vertex = vertex.next
    return None

  def add_edge(self, s_content, d_content, w):
    source = self._find(s_content)
    destination = self._find(d_content)
    if source is None or destination is None:
      return None
    source.add_edge(destination, w)

  def __str__(self):
    if self.vertex_head is None:
      return "<<E>>"
    ret = ""
    vertex = self.vertex_head
    while vertex is not None:
      ret += str(vertex)
      if vertex.next is not None:
        ret += "|"
      vertex = vertex.next
    return ret

if __name__ == "__main__":
  w = WeightedGraph()
  print(w)

  w.add_vertex("A")
  print(w)

  w.add_vertex("B")
  print(w)

  w.add_vertex("C")
  print(w)

  w.add_vertex("D")
  print(w)

  w.add_edge("A", "B", 1)
  print(w)

  w.add_vertex("E")
  print(w)

  w.add_edge("A", "D", 8)
  print(w)

  w.add_edge("B", "E", 7)
  print(w)

  w.add_edge("E", "D", 2)
  print(w)

  w.add_edge("D", "C", 1)
  print(w)