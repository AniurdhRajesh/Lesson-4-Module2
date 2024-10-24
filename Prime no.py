while True:
 lower=int(input("Enter a lower range : "))
 high=int(input("Enter an upper limit : "))
 print("Prime Numbers between ",lower," And ",high," are : ")
 for num in range(lower,high+1):
     if num>1:
         for i in range(2,num):
             if(num%i)==0:
                 break
             else:
                 print(num)
