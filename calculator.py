class calculator:
    def add(self,a,b):
        return a+b
    
    def substract(self,a,b):
        return a-b
    
    def multiply(self,a,b):
        return a*b
    
    def division(self,a,b):
        if b==0:
            return "cannot divide by zero!!"
        return a/b
    

def main():
    calc=calculator()

    while True:

        print("Welcome !!")
        print("Choose Operation (1-5):")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiply")
        print("4.Divide")  
        print("5.Exit")

        choice=input("Enter choice:")
        

        if choice=="5":
            print("Program exited succesfully!")
            break
        if choice in ["1","2","3","4"]:
            try:


                num1=float(input("Enter 1st Number:"))
                num2=float(input("Enter 2nd Number:"))  
            except ValueError:
                print("Invalid input")
            if choice=="1":
                print("Result=",calc.add(num1,num2))
            elif choice=='2':
                print("Result=",calc.substract(num1,num2))
            elif choice=="3":
                print("Result=",calc.multiply(num1,num2))
            elif choice=="4":
                print("Result=",calc.division(num1,num2))

        else:
            print("Invalid choice")

main()