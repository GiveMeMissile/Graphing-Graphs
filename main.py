import numpy as np
import matplotlib.pyplot as plt
def Numbers():
  def Stuff(H):
      D = H - 10
      E = H + 10
      return D, E
  print("You will be able to make a graph using the quadratic formula (Vertex form). You will give us what A, B, H, and K  are. And then we will give you the graph.")
  t = 0
  while(t == 0):
    try:
      A = float(input("What is A?: "))
      B = float(input("What is B?: "))
      K = float(input("What is K?: "))
      H = float(input("What is H?: "))
      t += 123456
    except:
      print("Please enter a number.")
  D, E = Stuff(H)
  return A, B, K, H, D, E
def Graph(x, y, A, B, K, H):
  plt.plot(x, y)
  plt.title("Quadratic graph")
  plt.xlabel("X-Axis")
  plt.ylabel("Y-Axis")
  plt.grid(True)
  plt.show()
A, B, K, H, D, E = Numbers()
x = np.linspace(D, E, 400)
y = A * (B * (x - H))**2 + K
Graph(x, y, A, B, K, H)