a =int( input("Enter the row position: "))
b = int(input("Enter the column position: "))
lists = [[3,4,5],[6,3,2],[5,7,8]]
if a > len(lists) or b > len(lists[0]):
    print("invalid input")
    exit()
lists[a-1][b-1] = 'x'
print(lists)
