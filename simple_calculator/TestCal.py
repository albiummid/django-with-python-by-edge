import SimCal as s
# for printing every answer
def printAns(value):
        print(f"Answer: {value}\n")

while True:
  print("""Enter:
        1 to add,
        2 to subtract,
        3 for multiplication,
        4 for division,
        5 for power,
        6 for modulus,
        0 to exit.
        """)
    

  choice = int(input("Your Choice:"))

  if choice == 0:
     break
    
  if choice==1:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     printAns(s.add(a,b))
  if choice==2:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     printAns(s.sub(a,b))
  if choice==3:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     printAns(s.mul(a,b))
  if choice==4:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     printAns(s.div(a,b))
  if choice==5:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     printAns(s.pow(a,b))
  if choice==6:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     printAns(s.mod(a,b))
   