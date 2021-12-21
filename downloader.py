#!/bin/python3
# -----Downloader------

import requests
from os import system as shell,getcwd as pwd,mkdir,get_terminal_size as term
pwd()
try:
    mkdir(f"{pwd()}/pkg")
except FileExistsError:
    print("[i] Initialzing sockets •••")
def Internet_(moto=False):
    try:
        if moto:
            print("[i] Connecting to the server ...    ",flush=True)
        requests.get(url="http://google.com")
    except requests.exceptions.ConnectionError:
        return False
    else:
        return True

def wget(url,work="download"):
    if Internet_():
        shell(f"wget {url} || printf '[E] Failed to {work} •••'")
    else:
        print(f"[E] Failed to {work} since ConnectionError •••")


def github(url,to=f"{pwd()}/pkg",work="download"):
    r="Connection Abort"
    a=url.split("/")[-1]
    try:mkdir(f"{to}/{a}")
    except FileExistsError:
        print(f"[W] {a} is already found")
        r="Already installed"
    if Internet_(moto=True):
        shell(f"git clone {url} {to}/{a} || printf '[E] Failed to {work} since {r}  •••\n'")
    else:
        print(f"[E] Failed to {work} since ConnectionError •••")

