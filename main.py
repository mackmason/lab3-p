# Author: Mack Mason mjm8542@psu.edu
# Collaborator: Bakhtiar Reza bmr5782@psu.edu
# Collaborator: Eric Beardslee eab6024@psu.edu
# Collaborator: Tong Chen tmc6117@psu.edu
# Section: 4
# Breakout: 12

def sum_n(n):
  if (n <= 0):
    return 0
  else:
    return n + sum_n(n-1)

def print_n(s, n):
  if (n == 0):
    return
  if (n == 1):
   print(s)
  else:
    print(s)
    print_n(s, n-1)

def run():
  sumFloatNumber = float(input("Enter an int: "))
  sumNumber = int(sum_n(sumFloatNumber))
  print(f"sum is {sumNumber}.")
  printString = input("Enter a string: ")
  print_n(printString,sumFloatNumber)

if __name__ == "__main__":
  run()