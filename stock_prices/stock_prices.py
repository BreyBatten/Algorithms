#!/usr/bin/python

import argparse

def find_max_profit(prices):
  

def bubble_sort(arr):
  for i in range(0, len(arr) - 1):

    for j in range(0, (len(arr) - i - 1)):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
      
  return arr

print(bubble_sort([3, 2, 5, 6, 4]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))