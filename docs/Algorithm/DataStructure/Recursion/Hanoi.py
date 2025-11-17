def hanoi(n,a,b,c):
  if (n==1):
    print(f"Move disk1 {a} to {c}")
  else:
    hanoi(n-1,a, c, b)
    print(f"Move disk{n} {a} to {c}")
    hanoi(n-1,b, a, c)

# n is tower depth
hanoi(3,"A","B","C")

class Car:
  detail = "Foxbagan"

  def __init__(self, color) :
    self.color = color

  def speedUp(self):
    temp = "not red"
    self.color = "red"