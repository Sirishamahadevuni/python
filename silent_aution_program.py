""" start-> input name and bid price  into a dictionary-> check if there are more bidders-> if yes clear screen and store the value
-> if no choose the bidder who has  price"""
import os
def find_winner(bidder_details): #siri:10000,shyam:500000,ram:30000
    highest_bid=0 #10000,50000
    winner=""
    for bidder in bidder_details: #siri ,shyam,ram
        bidding_price=bidder_details[bidder] #10000,500000,30000
        if bidding_price > highest_bid:
            highest_bid=bidding_price
            winner=bidder
            
    print(f"The winner is {winner} with highest bid of {highest_bid}")       
bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("\nwhat is your name? ")
    price=int(input("What is your bid? "))
    bidder_data[name]=price
    more_bidders=input("Are there more bidders? Type 'Yes' or 'No':").lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')