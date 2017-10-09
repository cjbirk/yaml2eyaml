#!/usr/bin/env python
# yaml2eyaml
# Author: Charles Birk
# Year: 2017

import ruamel.yaml as yaml
from ruamel.yaml.comments import CommentedMap
import os
import sys
import subprocess
from glob import glob

def yaml_loader(filepath):
    """ Loads a yaml file"""
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor, Loader=yaml.RoundTripLoader)
    return data

def encrypt_values(hieradict):
    for key in hieradict:
        value = hieradict[key]
        output = value
        if not value:
            output = ""
        elif "%{hiera" not in str(value):
            NULL = open(os.devnull, 'w')
            p = subprocess.Popen(['eyaml', 'encrypt', '-o', 'block', '--stdin'], stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=NULL)
            p.stdin.write(str(value))
            output = p.communicate()[0]
            p.stdin.close()
        else:
            output = '"' + output + '"' + "\n"
        hieradict[key] = output
    return hieradict

if __name__ == "__main__":
    origpath = sys.argv[1]
    finalpath = sys.argv[2]
    # Get a list of all yaml files in specified directory
    result = [y for x in os.walk(origpath) for y in glob(os.path.join(x[0], '*.yaml'))]
    for hierafile in result:
        data = yaml_loader(hierafile)
        # Encrypt data
        encryptyaml = encrypt_values(data)

        newbasepath = hierafile
        if len(sys.argv) == 3:
            newbasepath = hierafile.replace(str(origpath), str(finalpath))
            newfilepath = os.path.dirname(newbasepath)
            if not os.path.exists(newfilepath):
              os.makedirs(newfilepath)

        absfile = newbasepath.replace(".yaml", ".eyaml")
        print "Converted file: " + str(absfile)
        f = open(absfile, 'w')
        for key in encryptyaml:
            value = encryptyaml[key]
            if not str(value):
                f.write(key + ":" + "\n")
            elif "%{hiera" not in str(value):
                f.write(key + ": >" + "\n")
            else:
                f.write(key + ": ")
            f.write(encryptyaml[key])
        f.close
