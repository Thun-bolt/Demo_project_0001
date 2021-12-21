#!/bin/python3
#
from os import getcwd as pwd
from sys import path as path_lib
path_lib.append(pwd())
import downloader as dl

try:
    log_file=open(f"{pwd()}/pkg/app_log/stable.log",'r')
    log_raw=log_file.read()
except FileNotFoundError:
    try:
        dl.github(url=r"https://github.com/Adless-i/app_log")
        log_file=open(f"{pwd()}/pkg/app_log/stable.log",'r')
        log_raw=log_file.read()
    except FileNotFoundError:
        print("[E] Unable to download the content •••")
        exit()
log_raw=log_raw.split("\n")
log=[]
for _ in log_raw:
    try:
        a=_[0]
        if _[0]==".":pass
        elif _[0]!='.':
            log.append(_)
        else:
            print(f"[E] log file error on [ {_} ]")
    except IndexError:
        print("[w] ignoring log errors •••")

# Name Version URL Comment ReleaseDate OldVersion Type
