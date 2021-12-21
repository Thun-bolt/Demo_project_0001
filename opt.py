#!/bin/python3

def opt_list(N,T,search=''):
    if search=='':
        print(f"\n{N} /{T}")
    else:
        if len(N.split(str(search)))!=1:
            print(f"\n{N} /{T}")
def opt_search(N,C,T,search=''):
    if search=='':
        print("[E] No pckages found")
        exit()
    else:
        if len(N.split(str(search)))!=1:                               print(f"\n{N} /{T}\n  {C}")
def opt_show(N,V,C,Date,T,search=''):
    if str(search)==N:
        print(f"\nName:\t\t{N}\nVersion:\t{V} - {T}\nRelese Date:\t{Date}\nDescription:\t{C}")
    elif search=='':
        print("\n[E] No packages or repo found ...")
        exit()

#opt_show('a','V','c','d','b','a')
