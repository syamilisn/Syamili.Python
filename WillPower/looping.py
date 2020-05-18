#for loop 
#for(i=0;i<5;i++)
#loop variable starts from 0
for i in range(5):
    print(i)
#for scope is defined by indentation
sum=0
for i in range(5):
    print(i)
    sum=sum+i
print("Sum is",sum)

#Multiplication Tables
n=input("Enter number whose table is needed ")
n=int(n)
for i in range(10):
    print(n,"x",i+1,"=",n*(i+1))
    
#While Loop to print 10 to 1
i=10
while(i>0):
    print(i)
    i -= 1;
    
#guessing game
secretword="anime"
guess=""
count=0
limit=3
over= False
while guess != secretword and not over:
    if count<limit:
        guess=input("Enter guess: ")
        count +=1
    else:
        over=True
if over:        
    print("you lose!")
else:
    print("You win!")
    
