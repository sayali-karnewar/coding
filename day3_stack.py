count = input()
stack = []
print_values = []
print_count = 0
for i in range(count):
    query = list(map(int, input().split()))
    if query[0]==1:
        stack.append(query[1])
    elif query[0]==2:
        stack.pop()
    elif query[0]==3:
        print_count+=1
        print_values.append(max(stack))

if print_count>0:
    i = 0
    while i<print_count:
        print(print_values[i])
        i+=1


        

