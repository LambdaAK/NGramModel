from random import choice
class Bag:
  items = []
  def __init__(self, items):
    self.items = items

  def __repr__(self):
    return f"Bag({self.items})"
  
  def add(self, item):
    self.items.append(item)

  def get(self):
    # randomly get an item
    return choice(self.items)