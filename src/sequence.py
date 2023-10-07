class Sequence:
  # the sequence of words as a list
  s: list[str] = None
  
  def __init__(self, s: list[str]):
    self.s = s

  def __eq__(self, other):
    return self.s == other.s

