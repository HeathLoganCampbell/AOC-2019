import math

with open('input.txt') as f:
    inputData = map(int, f)

# Part 1
def calcMod(mass):
  return (mass // 3) - 2

# Part 2
def calcModTwo(mass):
  solution = 0;
  while mass >= 9:
    mass = calcMod(mass)
    solution += mass
  return solution

#
#
#
print(calcMod(12), "Should be 2");
print(calcMod(14), "Should be 2");
print(calcMod(1969), "Should be 654");
print(calcMod(100756), "Should be 33583");

print("Part 1, Solution")
print(sum(calcMod(x) for x in inputData))

print("Part 2, Solution")
print(sum(calcModTwo(x) for x in inputData))

