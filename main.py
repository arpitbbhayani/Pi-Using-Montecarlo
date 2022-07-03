import math
import random
import matplotlib.pyplot as mpl


def approximate_pi(n):
  """for a particular random selection of `n`
  points in a unit square. Find how many lie
  on the sector
  """
  count = 0
  for i in range(n):
    a = [random.random(), random.random()]
    d = math.sqrt(a[0] * a[0] + a[1] * a[1])
    if d <= 1.0:
      count += 1
  pi = (4 * count) / n
  return pi

# print(approximate_pi(1000000))

def convergence(N):
  all_n, all_pi = [], []

  count = 0
  for n in range(10, N):
    a = [random.random(), random.random()]
    d = math.sqrt(a[0] * a[0] + a[1] * a[1])
    if d <= 1.0:
      count += 1
    pi = (4 * count) / n
    all_n.append(n)
    all_pi.append(pi)

  return all_n, all_pi

all_n, all_pi = convergence(1000000)

print(all_n[-1], all_pi[-1])

mpl.plot(all_n, all_pi)
mpl.show()
