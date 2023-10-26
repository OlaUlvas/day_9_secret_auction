from art import logo
print(logo)

bids = {}

game_on = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner.title()} with a bid of {highest_bid}.")


while game_on:
    name = input("What is your name?: ").lower()
    price = int(input("What is your bid?: "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    alternative = ["yes", "no"]
    while should_continue not in alternative:
        print("Answer Yes or No")
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        game_on = False
        find_highest_bidder(bids)

        print("Goodbye!")