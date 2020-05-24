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
