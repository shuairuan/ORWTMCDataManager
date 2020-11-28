import json
from tkinter import *
import tkinter.filedialog

def backupsrc(cfg):
    src = {}
    print("Beginning Backup Source Configuration.")
    print("We have some BuiltIn configurations, would you like to see them?(y/n)")
    o = input(">> ")
    if o == "n":
        pass
    else:
        bisets = open("builtin_sets.json")
        b = json.load(bisets)
        bisets.close()
        print("Name\tSource")
        for k, v in b.items():
            print(k, "\t", v)
        while True:
            name = input("Type the name(enter 'q' to exit): ")
            if name == "q":
                break
            try:
                src[name] = b[name]
            except:
                print("Not found.")
    
    print("Source selection.")
    print("1. Type manually.")
    print("2. Choose via Graphical interface.")
    p = input(">> ")
    while True:
        if p == "1":
            print("Type 'q' in Name to exit.")
            name = input("Name: ")
            if name == "q":
                break
            path = input("Path: ")
            print("Name: ", name, " Path: ", path)
            src[name] = path
            print("Added.")
        elif p == "2":
            print("Type 'q' in Name to exit.")
            name = input("Name: ")
            if name == "q":
                break
            path = tkinter.filedialog.askdirectory()
            print("Name: ", name, " Path: ", path)
            src[name] = path
            print("Added.")
    print("Configuration ended.")
    cfg['backup'] = src
    return cfg

def index():
    print("Settings.index.app loaded.")
    z = {}
    z['config'] = {}
    cfg = z['config']
    print("Config your app.")
    print("\n\n")
    print("Which of the storage medium do you like to use?")
    print("1. Local Disk.")
    print("2. DockerRegisterCloud(thanks to https://github.com/xausky/DockerRegisterCloud, licensed under MIT)")
    o = input(">> ")
    if o == "1":
        print("You selected: local disk.")
        cfg['storage'] = {}
        cfg['storage']['method'] = "local"
        print("Where?")
        print("1. Type the path manually.")
        print("2. Choose via Graphical interface.")
        p = input(">> ")
        if p == "1":
            path = input("Path: ")
        elif p == "2":
            path = tkinter.filedialog.askdirectory()
        else:
            print("Invalid!")
            sys.exit(2)
        cfg['storage']['path'] = path
    elif o == "2":
        print("Please download the executable files and rename it into 'drc', copy it to 'apps' folder. And you MUST config it!(drc login {server ip})")
    else:
        print("Invalid!")
        sys.exit(2)
    fp = open("config.json", 'w')
    print("Sending you to Settings/backupsrc...")
    cfg = backupsrc(cfg)
    json.dump(z, fp)
    fp.close()