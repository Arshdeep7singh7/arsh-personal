import random
import string
# 9.1
print("displaying 5 random integers between 1 to 100")
for i in range(5):
    randomNumber=random.randrange(1,100)
    print(randomNumber)

# 9.2


check=True
randomNumber=random.randrange(1,100)
for i in range(2,randomNumber):
    if randomNumber%i==0:
        check=False
if check==True:
    print(f"it is a prime number ({randomNumber})")
else :
    print(f"not a prime number({randomNumber})")

#9.3
print("simulating rolling of die")
die=random.randrange(1,7)
print(die)

#9.4

print("shuffling of list")
numbers=[1,3,5,6,7]
random.shuffle(numbers)
print(numbers)

#9.5
print("random number from a list")
ran=random.choice(numbers)
print(ran)

#9.6

length=int(input("enter the lenght of password"))
characters=string.ascii_letters+string.digits+string.punctuation
password=''.join(random.choice(characters) for i in range(length))
print(f"the password is {password}")

#9.7

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
print("choosing a random number from deck of 52 cards")
result=random.choice(deck)
print(result)