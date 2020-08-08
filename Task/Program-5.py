/* n=10 */
n= int(input("Enter a no :"))
fact = 1
if(n<0):
    print("nothing")
elif n ==0:
    print("fact is",1)
else:
    for a in range(1,n+1):
        fact=fact*a
    print("fact is",fact)
