from art import logo
import os
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder 
    print(f"The winner is {winner} with the bid of ${highest_bid}")


while not bidding_finished:
    name = input("Enter your name: ")
    bid_price = int(input("Enter the bid price: $"))
    bids[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')