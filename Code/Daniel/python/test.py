import msvcrt
import copy
import levels


# while True:                         # input commands
#     command = msvcrt.getch()
#     print(command)
#     if command == b'q':
#         break
            
class Test:
    def __init__(self,num):
        self.my_num = num

obj1 = Test(5)
obj2 = Test(2)
obj_list = [obj1, obj2]

def obj_getter(check_num, obj_list):
    return [item for item in obj_list if item.my_num == check_num] 

new_obj = obj_getter(5, obj_list)[0]
print(new_obj.my_num)