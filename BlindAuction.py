from os import system, name
def clear():
  _= system('cls')

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
  highest = 0
  winner = ""
  for bidder in bidding_record:
    amount = bidding_record[bidder]
    if amount > highest:
      highest = amount
      winner = bidder
  print(f"The winner is {winner} with a bid of Rs {highest}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: Rs "))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no':")
  if should_continue == "no":
    bidding_finished = True
    highest_bidder(bids)
  elif should_continue == "yes":
    clear()