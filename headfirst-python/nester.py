# coding = utf-8

def print_lol(x):
    for name in x:
        if isinstance(name,list):
            print_lol(name)
        else:
            print name
