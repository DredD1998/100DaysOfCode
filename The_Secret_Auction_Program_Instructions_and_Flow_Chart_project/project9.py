import art
print(art.logo)


def compare_bid(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")






bids = {}

continue_bidding = True

while continue_bidding:
    name = input("What is your name?:\n")
    bid_price = int(input("What is your bid?:\n$"))
    bids[name] = bid_price
    should_continue = input("Are there any other bidders?Type 'Yes' or 'No':\n").lower()
    if should_continue == "no":
        continue_bidding = False
        compare_bid(bids)
    elif should_continue == "yes":
        print("\n" * 50)



