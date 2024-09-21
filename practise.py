A= [] #Marks>70
B= [] #Marks>31-<69
C= [] #Marks<30

for i in range(20):
    marks= int(input("Enter your marks:"))

    if marks>70:
        A.append(marks)
    if marks>31 and marks<69:
        B.append(marks)
    if marks <30:
        C.append(marks)
    
print(A)
print(B)
print(C)

