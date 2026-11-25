# Character Counter

s = input("Enter a string: ")
count = 0 

for i in s:
    if i != " ":
        count += 1
    

print(f"Output: {count}")