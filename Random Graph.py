import matplotlib.pyplot as plt
import random
def graph(x,y):
    plt.scatter(x,y)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Randomly Generated Points")
    plt.show()
def rand():
  X = []
  Y = []
  for _ in range(15):
    x = random.randint(0,20)
    y = random.randint(0,20)
    X.append(x)
    Y.append(y)
  return X, Y
x, y = rand()
graph(x,y)
