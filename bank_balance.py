'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

balance =0
def main():
    
    print ("zero Balance:", balance)
    deposit(100)
    withdraw(50)
    print ("Balance:", balance)
def deposit(n):
    global balance
    balance +=n
def withdraw(n):
    global balance
    balance -=n
    
    
main()

    

