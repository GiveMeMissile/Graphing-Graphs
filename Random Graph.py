import matplotlib.pyplot as plt
import random
def graph(x,y):
    plt.scatter(x,y)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Randomlt Generated Points")
    plt.savefig("graph.png")
    plt.show()
x = [random.randint(1,10)]
y = [random.randint(1,10)]
graph(x,y)
