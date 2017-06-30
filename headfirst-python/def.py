names = ["zhang","fa","ling",[1,2,3,4],[5,6,"balala"]]



def print_lol(x,level=0):
    for name in x:
        if isinstance(name,list):
            print_lol(name,level+1)
        else:
            print name

print print_lol(names,2)