class Option:
  data = None
  def __init__(self, data):
    self.data = data

  def bind(self, f):
    '''
    Monadic bind operator
    f returns an Option
    '''
    if self.data is None:
      return self
    else:
      return f(self.data)