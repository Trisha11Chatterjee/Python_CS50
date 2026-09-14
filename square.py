'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def main():
    x = int (input ("enter x"))
    print ("square of x", square(x))

def square(n):
    return pow(n,2)
main()