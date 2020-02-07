#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profits = []
  max_profit = 0
  # loop through prices with 2 pointers
  for i in range(0, len(prices)):
    for j in range(i, len(prices)):
      # if price at index j and i are equal, keep looping through prices
      if prices[j] == prices[i]:
        continue
      # if prices at indexes aren't equal, subtract index j from index i
      else:
        profit = prices[j] - prices[i]
        # place the difference in the profit list declared above
        profits.append(profit)

  # return the largest item in the profits list and return
  max_profit = max(profits)
  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))