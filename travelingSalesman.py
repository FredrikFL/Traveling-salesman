from random import *
import numpy as np

class cities:
  def __init__(self, length):
    self.network = np.random.randint(1, 10, size=(length, length))
    for i in range(1, length):
      #self.network.append([])
      for j in range (0, i):
        #self.network[i].append(randint(1, 10))
        self.network[i][j]
    self.path = []
    self.cost = 0

  def get(self, x, y):
    #++x
    if x < y:
      return self.network[y][x]
    elif x > y:
      return self.network[x][y]
    else:
      print("error")
      return -10

  def random(self):
    l = len(self.network)
    free = []
    for i in range(0, l):
      free.append(i)
    p = randint(0, len(free) - 1)
    prev = free[p]
    first = prev
    free.pop(prev)
    self.path.append(prev)

    while len(free) > 0:
      r = randint(0, len(free) - 1)
      this = free[r]
      self.path.append(this)
      #print self.get(prev, this)
      self.cost += self.get(prev, this)
      prev = this
      free.pop(r)
    #print self.get(first, prev)
    self.cost += self.get(first, prev)

  def iterativeRandom(self, iterations):
    self.random()
    for q in range(1, iterations):
      iPath = []
      iCost = 0
      l = len(self.network)
      free = []
      for i in range(0, l):
        free.append(i)
      p = randint(0, len(free) - 1)
      prev = free[p]
      first = prev
      free.pop(prev)
      iPath.append(prev)

      while len(free) > 0:
        r = randint(0, len(free) - 1)
        this = free[r]
        iPath.append(this)
        #print self.get(prev, this)
        iCost += self.get(prev, this)
        prev = this
        free.pop(r)
      #print self.get(first, prev)
      iCost += self.get(first, prev)
      if iCost < self.cost:
        self.cost = iCost
        self.path = iPath

  def greedy(self):
    l = len(self.network)
    free = []
    for i in range(0, l):
      free.append(i)

    p = randint(0, len(free) - 1)
    prev = free[p]
    free.pop(prev)
    first = prev
    self.path.append(prev)
    for q in range(0, len(free)):
      cheapest = 10
      city = 0
      #for i in range(0, l):
      #  for j in range (0, i):
      #    if i in free and self.get(i, j) < cheapest and j == prev:
      #      city = i
      #      cheapest = self.get(i, j)
      #    elif j in free and self.get(i, j) < cheapest and i == prev:
      #      city = j
      #      cheapest = self.get(i, j)
      for x in free:
        if self.get(x, prev) < cheapest:
          cheapest = self.get(x, prev)
          city = x
          if cheapest == 1:
              break

      self.path.append(city)
      free.remove(city)
      self.cost += cheapest
      prev = city
    #print "P", prev, ",", "F", first
    self.cost += self.get(prev, first)
  def greedyImprove(self):
    i = 0
    while i < 100:
      i = i + 1
      city1 = randint(0, len(self.path) - 1)
      city2 = randint(0, len(self.path) - 1)
      while city1 == city2:
        city2 = randint(0, len(self.path) - 1)

      point1 = self.path.index(city1)
      point2 = self.path.index(city2)
      gPath = list(self.path)
      gPath[point1] = city2
      gPath[point2] = city1

      #for i in range(0, len(gPath) - 1):
      #  gCost += self.get(gPath[i], gPath[i+1])
      oldCost = 0
      newCost = 0
      if point1 == 0:
        oldCost += self.get(self.path[len(self.path)-1], self.path[point1])
        newCost += self.get(gPath[len(gPath)-1], gPath[point1])
      else:
        oldCost += self.get(self.path[point1-1], self.path[point1])
        newCost += self.get(gPath[point1-1], gPath[point1])
      if point2 == 0:
        oldCost += self.get(self.path[len(self.path)-1], self.path[point2])
        newCost += self.get(gPath[len(gPath)-1], gPath[point2])
      else:
        oldCost += self.get(self.path[point2-1], self.path[point2])
        newCost += self.get(gPath[point2-1], gPath[point2])
      if point1 == len(self.path) - 1:
        oldCost += self.get(self.path[0], self.path[point1])
        newCost += self.get(gPath[0], gPath[point1])
      else:
        oldCost += self.get(self.path[point1+1], self.path[point1])
        newCost += self.get(gPath[point1+1], gPath[point1])
      if point2 == len(self.path) - 1:
        oldCost += self.get(self.path[0], self.path[point2])
        newCost += self.get(gPath[0], gPath[point2])
      else:
        oldCost += self.get(self.path[point2+1], self.path[point2])
        newCost += self.get(gPath[point2+1], gPath[point2])


      difCost = newCost - oldCost
      if difCost < 0:
        #print difCost
        #gCost = 0
        #for i in range(0, len(gPath) - 1):
        #  gCost += self.get(gPath[i], gPath[i+1])
        #gCost += self.get(gPath[0], gPath[len(gPath)-1])
        self.cost += difCost
        self.path = list(gPath)
        i = 0

small = cities(500)
small.random()
print("500 cities random:", small.cost)
small.greedyImprove()
print("500 cities random (improved):",small.cost)

small2 = cities(500)
small2.greedy()
print("500 cities greedy", small2.cost)
small2.greedyImprove()
print("500 cities greedy (improved)", small2.cost)

small3 = cities(500)
small3.iterativeRandom(10)
print("500 cities iterative random:", small3.cost)
small3.greedyImprove()
print("500 cities iterative random (improved):", small3.cost)

small = cities(1000)
small.random()
print("1000 cities random:", small.cost)
small.greedyImprove()
print("1000 cities random (improved):",small.cost)

small2 = cities(1000)
small2.greedy()
print("1000 cities greedy", small2.cost)
small2.greedyImprove()
print("1000 cities greedy (improved)", small2.cost)

small3 = cities(1000)
small3.iterativeRandom(10)
print("1000 cities iterative random:", small3.cost)
small3.greedyImprove()
print("1000 cities iterative random (improved):", small3.cost)

small = cities(10000)
small.random()
print("10000 cities random:", small.cost)
small.greedyImprove()
print("10000 cities random (improved):",small.cost)

small2 = cities(10000)
small2.greedy()
print("10000 cities greedy", small2.cost)
small2.greedyImprove()
print("10000 cities greedy (improved)", small2.cost)

small3 = cities(10000)
small3.iterativeRandom(10)
print("10000 cities iterative random:", small3.cost)
small3.greedyImprove()
print("10000 cities iterative random (improved):", small3.cost)
