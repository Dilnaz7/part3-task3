my_list = []

for i in range (0, 5):
    my_list.append(int(input()))

shift_num = (int(input()))
while shift_num < 0:
    value = my_list.pop(0)
    my_list.append(value)
    shift_num +=1
    
while shift_num > 0:
    value = my_list.pop()
    my_list.insert(0, value)
    shift_num -=1
print (my_list)
