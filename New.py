name = input("Enter your name : ")
print(name)
vol = ['a','e','i','o','u']
output = ''

for i in range(len(name)):
    if name[i] in vol:
        continue
    else:
        output = output+name[i]


print(output)
# ankit = nkt