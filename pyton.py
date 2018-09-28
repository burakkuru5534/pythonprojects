list1 = ["God","Damn","Pretty.",["List","in","the","list."],1]
print(list1[0],list1[1])
print(list1[1])
print(list1[2])
print(list1[3][0])
print(list1[3][1])
print(list1[3][2])
print(list1[3][3])

index=0
list1.insert(index,"Firstly")
list1[3]="it"
print(list1)
print(list1+[2,3])
list1.append(4)
print("God" in list1)
print("Fuck" in list1)

print(not "fuck" in list1)
print(not "God" in list1)
print(len(list1)," is the count of the array's members. Dont forget to start 0 when you want to count to members of arrays")

print(list1.index("God")," is the value of the God's position")
