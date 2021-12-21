#!/bin/python3
from os import getcwd as pwd
from sys import path,argv as a
path.append(pwd())
import log_reader as Lr
log=Lr.log
from opt import opt_search,opt_list,opt_show
#-----------------------------------------------------+
try:
    opt=a[1]
except IndexError:
    print("[E] No options choosed ...")
    exit()
#-----------------------------------------------------+
# Name Version URL Comment ReleaseDate OldVersion Type|
#-----------------------------------------------------+
for __ in log:
    N,V,URL,C,Date,Old,T=__.split("\\t")
    N=str(N)
    V=str(V)
    C=str(C)
    Date=str(Date)
    T=str(T)

    if a[1]=="list":
        try:
            search=a[2]
            opt_list(N,T,search)
        except IndexError:
            opt_list(N,T,'')
    elif a[1]=="search":
        try:
            search=a[2]
            opt_search(N,C,T,search)
        except IndexError:
            opt_search(N,C,T,'')
    elif a[1]=="show":
        try:
            search=a[2]
            opt_show(N,V,C,Date,T,search)
        except IndexError:
            opt_show(N,V,C,Date,T,'')
    else:
        print("[E] Unknown options ...")
        exit()
