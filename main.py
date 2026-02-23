balance = 1000

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient balance"
    balance -= amount
    return balance

def check(amount):
    global balance
    if amount <= 0:
        return "Invalid deposit amount"
    balance += amount
    return balance

def deposits(amount):
    global balance
    print("Processing deposit...")   # temporary debug
    balance += amount
    return balance


print("Balance after deposit:", deposit(500))
print("Balance after withdrawal:", withdraw(200))
print("Balance after check:", check(2))
print("Balance after deposits:", deposits(500))