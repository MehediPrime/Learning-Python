class Parent():
  #Constructor
  def __init__(self):
    self.value = "Inside Parent"

  #Parent Show Method
  def show(self):
    print(self.show)


class Child:
  #Constructor
  def __init__(self):
    self.value = "Inside Child"

  #Parent Show Method
  def show(self):
    print(self.show)


objParent = Parent()
objChild = Child()

objParent.show()
objChild.show()
