#!/usr/bin/python

import os
import sys

r_args = []
args = sys.argv
args.reverse()
args.pop()


if len(sys.argv) == 0:
    args.append("help")

def register_arg(name: str, params_count: int, s_desc: str, desc: str, func):
    r_args.append({"name": name, "params_count": params_count, "func": func, "s_desc": s_desc, "desc": desc})


def help_callback(d):
    if d[0] != "":
        finded = False
        for r_arg in r_args:
            if r_arg['name'] == d[0]:
                print(r_arg['desc'])
                finded = True
                break
        if not finded:
            print("Invalid command!")
    else:
        for r_arg in r_args:
            print(f"{r_arg['name']}: {r_arg['s_desc']}")
    exit(0)

register_arg("help", 1, "Help command, type `help help` to see more info", "Allows you to see other commands\n type `help {command}` to see more help", help_callback)


def git_remote_add(remote: str, name: str, path: str, profile_url: str):
    last = os.getcwd()
    os.chdir(path)
    os.system(f"git remote add {remote} {profile_url}/{name}")
    os.chdir(last)

def setup_origin_callback(args):
    if args[0] != "":
        if len(args[1]) == 0 and len(args[2]) == 0:
            git_remote_add("origin", "muzzman-lib", "muzzman-lib", args[0])
            git_remote_add("origin", "muzzman-egui", "muzzman-egui", args[0])
            git_remote_add("origin", "muzzman-http", "modules/http", args[0])
            git_remote_add("origin", "muzzman-transport", "modules/transport", args[0])
        else:
           git_remote_add("origin", args[1], args[2], args[0]) 
    else:
        print("Need github profile link")
        exit(1)

register_arg("setup_origin", 3, "Will setup the git remote origins", "First argument should me your github profile like: `git@github.com:konkitoman`\nShould not be any command after this", setup_origin_callback)

def setup_upstream_callback(_):
    g = "https://github.com/ManStudio" 
    git_remote_add("upstream", "muzzman-lib", "muzzman-lib", g)
    git_remote_add("upstream", "muzzman-egui", "muzzman-egui", g)
    git_remote_add("upstream", "muzzman-http", "modules/http", g)
    git_remote_add("upstream", "muzzman-transport", "modules/transport", g)

register_arg("setup_upstream", 0, "Will setup the upstream", "", setup_upstream_callback)

while len(args) != 0:
    arg = args.pop()
    finded = False
    for r_arg in r_args:
        if r_arg['name'] == arg:
            params = []
            for _ in range(0, r_arg['params_count']):
                try:
                    params.append(args.pop())
                except:
                    params.append("")
            r_arg['func'](params)
            finded = True
            break
    if not finded:
        print(f"Invalid argument: {arg}")
        exit(1)
