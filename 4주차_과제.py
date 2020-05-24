#2884
H, M = input().split()
H=int(H)
M=int(M)
if M >= 45:
    print(H, M-45)
elif M < 45 and H >= 1:
    print(H-1, M+15)
else:
    print(23, M+15)

#1065
N_str=input()
number_of_hansu=0
def f(A):
    if int(A)<100:
        return True
    else:
        A=str(A)
        if 2*int(A[1])==int(A[0])+int(A[2]):
            return True
        else:
            return False

for B in range(1,int(N_str)+1):
    if f(B)==True:
        number_of_hansu+=1

print(number_of_hansu)
