** start of main.py **

import math

class Category:
    def __init__(self,name, ledger=""):
        self.ledger=[]
        self.balance1=0
        self.name=name

    #return balance of the account
    def get_balance(self):
        if len(self.ledger)==0:
            print(0)
            return 0
        else:
            balance=0
            for i in range(0,(len(self.ledger))):
                #print(self.ledger[i])
                balance += self.ledger[i]["amount"]
                #print(balance)
            return balance
    
    #deposit an amount to the account
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance1 += amount
    
    #withdraw an amount
    def withdraw(self,amount,description=""):
        if amount > self.get_balance():
            print("=Insufficient funds")
            return False
        else: 
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance1 -= amount
            return True

    #transfer balance between categories
    def transfer (self,amount,Category):
        if amount > self.get_balance():
            print("=Insufficient funds")
            return False
        else: 
            self.ledger.append({'amount': -amount, 'description': f"Transfer to {Category.name}"})
            self.balance1 -= amount
            Category.ledger.append({'amount': amount, 'description': f"Transfer from {self.name}"})
            return True

    #check for availability of specific amounts
    def check_funds(self, amount):
        return False if amount > self.get_balance() else True
    
    #return the lodger and balance when a category is printed
    def __str__(self):
        string1=f"{'*'*((30-len(self.name))//2)}{self.name}{'*'*((30-len(self.name))//2)}"
        #printing the lines + formatting
        for i in range(len(self.ledger)):
            string1 += ("\n"+self.ledger[i]["description"][0:23])
            if self.ledger[i]["amount"]<0:
                spaces= 30 - (math.floor(math.log10(abs(self.ledger[i]["amount"])))+5) - len(self.ledger[i]["description"][0:23])
                string1 += f"{' '*spaces}" + f"{self.ledger[i]['amount']:.2f}"
            else:
                spaces= 30 - (math.floor(math.log10(self.ledger[i]["amount"]))+4) - len(self.ledger[i]["description"][0:23])
                string1 += f"{' '*spaces}"+f"{self.ledger[i]['amount']:.2f}"
        string1 += f"\nTotal: {self.get_balance()}"
        return string1
        
    
#code for testing
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(30)
print(clothing.get_balance())
print(food)
print(clothing)
auto=Category("Auto")
auto.deposit(200)
auto.withdraw(34)
print(auto)


def create_spend_chart(categories):
    #adding the header
    chart = "Percentage spent by category"
    #calculating the total_spending and the single category spending
    total_spending = 0
    spending_per_category = {}
    for category in categories:
        category_spending = 0
        for transaction in category.ledger:
            if transaction["amount"]<0:
                category_spending += abs(transaction["amount"])
        spending_per_category[f"{category.name}"]=category_spending
    total_spending=round(sum(spending_per_category.values()),2)
    #setting up the scale of numbers to the left of the chart
    for i in range(11):
        if i>0 and i<10:
            chart += "\n "
        elif i==10:
            chart += "\n  "
        else:
            chart += "\n"
        chart +=f"{10*(10-i)}|"
        #adding the categories dots
        for category in categories:
            if (spending_per_category[f"{category.name}"]*10//total_spending) >(10-i-1):
                chart += " o "
            else:
                chart += "   "
        chart += " "
    #making horizontal line
    chart += "\n    "
    for i in range(len(categories)):
        chart += "---"
    chart += "-"
    #print vertical names
    category_names_length={}
    for category in categories:
        category_names_length[f"{category.name}"]=len(category.name)

    for i in range(max(category_names_length.values())):
        chart += "\n    "
        for name,length in category_names_length.items():
            if i <= (length-1):
                chart += f" {name[i]} "
            else:
                chart += "   "
        chart += " "
    return chart

print(create_spend_chart([food,clothing,auto]))



** end of main.py **

