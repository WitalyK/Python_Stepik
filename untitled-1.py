lst = []
for i in range(3):
    lst.append(input("������� "))
print(lst)
lst.append(lst.pop(0))
print(lst)
