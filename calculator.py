#                                                 calculator
user_inp1 =int(input("Enter your first number:"))
user_inp2 = int(input("Enter your second  number"))
user_op = input("Enter you operator")

def calculate (a, b,op):
 
 if (op =="+"):
   print("Ans", a + b)

 elif(op == "-"):
   print("Ans", a - b)
 
 elif(op == "*"):
    print("Ans",a * b)

 elif(op == "/"):
    if(b != 0):
     print("Ans", a / b)
    else:print("Error: Division by zero not allowed")

 else:
   print("Invald operator")
