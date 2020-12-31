#input the no of rows
rows = int(input())

#initiatize the empty list for holding the matrix
array = []

#for each row
for r in range(rows):
    array.append([int(item) for item in input().split(" ")])   #input the elements till they are entered on each row r

#display the matrix
print(array)    


#update the 3rd item of 2nd row while checking that the elemnt exists
if len(array[1]) ==2:
    array[1].append(0)
    array[1][2] = 23


else:
    array[1][2] = 23

print("updated matrix", array)


#insert the row
array.insert(1, [1,3])
print("row added matrix", array)