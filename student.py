name = input("Enter your name: ")

m1 = float(input("Enter marks for python: "))
m2 = float(input("Enter marks for sql: "))
m3 = float(input("Enter marks for excel: "))

total = m1 + m2 + m3
percentage = total / 3 * 100

print(f"student name {name} \n Total marks: {total} \n Percentage: {percentage}")
