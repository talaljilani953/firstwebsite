print("\tBank Management")
print("---------------------------------------------------------")
balance=10000000
oc=0
dp=0
ac=0
def openaccount():
    print("account is open")
    oc=int(input("Enter Open Cash to add in account"))
    print(oc,"is added to your account")
    print("Total Balance",balance+oc) 
def withdraw():
    amount=int(input("Enter Withdraw Amount"))
    if balance<amount:
        print("Insufficient Money")
    if balance>amount:
        print("Withdraw Cash:",amount)
        print("Remaining Balance",balance-amount)
    if balance==amount:
        print("Withdraw Cash",amount)
        print("Remaining Balance",balance-amount)
def deposit():
    dp=int(input("Enter Deposit Amount"))
    print("Deposit Amount:",dp) 
    print("Total Balance",balance+dp+oc)
def Bankstatement():
    ac=oc+balance+dp 
    print("your balance is:",ac)
print("Choose Your Command\n-----------------\n1.Withdraw \t2.Deposit \n3.Open account \t4.Bank Statement")
choose=int(input(""))
if choose == 1:print(withdraw())
if choose == 2:print(deposit())
if choose == 3:print(openaccount())
if choose == 4:print(Bankstatement()) 


