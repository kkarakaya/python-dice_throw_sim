import random     # for rolling dice randomly

N = 2       # number of dice
L = 870     # number of throws

# Rolls N dice randomly and returns their values
def rollDice(N):
    outcomes = []
    for i in range(0,N):
        outcomes.append(random.randint(1,6))
    return outcomes

# Checks is a number even or not. Returns True or False.
def isEven(number):
    return (number % 2) == 0

# Simulates dice rolls by given number of dice and throws. Returns number of even sums
def simulateNumberOfEvenSums(N,L):
    numberOfEvenSums = 0
    # repeat L times
    for i in range(0,L):
        sumOfDice = sum(rollDice(N))    # roll dice and find sum
        if isEven(sumOfDice):           # if the sum is even increase counter
            numberOfEvenSums += 1
    return numberOfEvenSums

############### Main Code ###############
# Calculate the probability of getting an even sum for N dice and L throws
p = simulateNumberOfEvenSums(N,L) / L
print(p)