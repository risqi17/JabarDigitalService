
def unique_names(names1, names2):
    list = []
    for x in names1:
        if x not in list:
            list.append(x)
            
    for x in names2:
        if x not in list:
            list.append(x)
    
    return list

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
