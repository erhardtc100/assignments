#Reads name txt into a variable
with open('name.txt') as f:
    my_name = f.read ()

#construct greeting
greeting = 'Hello my name is ' + my_name + '.'
print(greeting)

#write that to a file
with open('hello.txt', 'w') as f:
    f.write(greeting)