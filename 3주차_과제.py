#1330
A,B=input().split()
A=int(A)
B=int(B)
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")

#9498
score = int(input())
if 90<=score<=100:
    print("A")
elif 80<=score<90:
    print("B")
elif 70<=score<80:
    print("C")
elif 60<=score<70:
    print("D")
else:
    print("F")

#2753
year = int(input())
if year%4==0 and year%400==0:
    print("1")
elif year%4==0 and year%100!=0:
    print("1")
else:
    print("0")

#14681
A=int(input())
B=int(input())
if A>0 and B>0:
    print("1")
elif A<0 and B>0:
    print("2")
elif A<0 and B<0:
    print("3")
else:
    print("4")
