#imported outside of the course scope ##subprocess.run('cls',shell=True)##
import subprocess

bid_dict={}

def print_highestbid():
    highestbid=0
    highestbidName=""
    for key in bid_dict:
        if(bid_dict[key]>highestbid):
            highestbidName=key
            highestbid=bid_dict[key]
    print(f"The winner is {highestbidName} with a bid of ${highestbid}")

continueBid=True
while(continueBid):
    print("Welcome to the secret auction program.")
    name=input("What is your name?: ")
    bidMessage=""
    while(not bidMessage.isnumeric()):
        bidMessage=input("What is your bid?: $")
    bid=int(bidMessage)
    bid_dict[name]=bid
    _contBidInput=input("Are there any other bidders: ")
    if(_contBidInput=="" or _contBidInput=="y" or _contBidInput=="Y" or _contBidInput=="yes" or _contBidInput=="Yes"):
        subprocess.run('cls',shell=True)
        continueBid=True
    else:
        continueBid=False
print_highestbid()