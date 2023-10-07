from sequence import Sequence
from bag import Bag


def clean(data: str) -> str:
  # get rid of anything that's not a letter
  # all letters are converted to lower case
  # all whitespace is replaced with a single space
  return "".join([c.lower() if c.isalpha() or c == "'" else " " for c in data])

def split(data: str) -> list[str]:
  return data.split()

def take(n: int, data: list[str]) -> list[str]:
  return data[:n]

def chunk(n: int, data: list[str]) -> list[list[str]]:
  A = []
  while len(data) >= n:
    A.append(take(n, data))
    data = data[1:]
  return A

def pair (data: list[str]):
  # return a tuple
  # the first element is all elements but the last
  # the second element is just the last element
  return (data[:-1], data[-1])

class Model:
  n: int
  m: dict[list[str], Bag]

  def __init__(self, n: int, data: str):
    self.n = n
    self.m = {}
    chunked = chunk(n, split(clean(data)))
    for words in chunked:
      k, v = pair(words)
      if self.m.get(tuple(k)) is None:
        self.m[tuple(k)] = Bag([v])
      else:
        self.m[tuple(k)].add(v)

  def _add(self, bag: Bag, word: str):
    if self.m is None:
      self.m = {}
    self.m[bag] = word

  def get(self, words: list[str]) -> str:
    bag = Bag(words)
    return self.m[bag]
  
  def predict(self, s) -> list[str]:
    words = split(clean(s))
    # get the last n - 1 words of the input
    # predict the next word that comes in the sequence
    # if the sequence is not in the model, return None
    # if the sequence is in the model, return the most likely word
    try:
      lastNMinusOne = words[-self.n+1:]
      next = self.m[tuple(lastNMinusOne)].get()
      return next
    except KeyError:
      return None
    
  def __repr__(self):
    return f"Model({self.n}, {self.m})"
    

class InterpModel:
  models: list[Model]
  def __init__(self, data: str, lower: int, upper: int):
    # make a model for each n in range(lower, upper)
    self.models = []
    for n in range(lower, upper):
      self.models.append(Model(n, data))

  def predict(self, s: str) -> list[str]:
    # use the highest n possible to predict something
    # if that fails, try the next highest n
    
    # if all n fail, return None

    for model in self.models:
      prediction = model.predict(s)
      if prediction is not None:
        return prediction
      
    return None
  
  def generate(self, s: str, n: int) -> str:
    # generate up to n more words
    # stop when the result is None
    # return the result

    while n > 0:

      prediction = self.predict(s)
      if prediction is None:
        break
      s += " " + prediction
      n -= 1

    return s
  

  def __repr__(self):
    return f"InterpModel({self.models})"

    
