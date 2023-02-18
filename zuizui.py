a = ['Ho','Tuan','thanh']
def check_name(name): 
    flag = True         
    for i in name:
        if i == i.capitalize():
            flag = True
        else:
            flag = False
    return flag

print(check_name(a))
