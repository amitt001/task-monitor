#!/usr/bin/env python3

import os
import sys
from argparse import ArgumentParser


opsys = list(os.uname())
if "Linux" not in opsys:
    sys.exit(0)

info = {}

def cpuinfo():

    proccount = 0
    sib = cores = 0
    arch = 32
    hypercount = 0
    path = "/proc/cpuinfo"
    
    with open(path) as cpuinfo:
        data = cpuinfo.read()
        full = data.replace('\t','').replace(':','')
        value = full.split("\n")

        for full in value:
 
            if "siblings " in full:
                sib = int(full.lstrip("siblings "))
                sib = int(sib)

            if "cpu cores " in full:
                cores = full.lstrip("cpu cores ")
                info["CPU(s)"] = int(cores)

            if "model name " in full:
                info["Model name"]  = full.lstrip("model name ")

            if "cache size " in full:
                csize = full.lstrip("cache size ")
                info["Cache-Size"] = csize

            if " lm " in full:
                info["Architecture"] = 64 # it also tell about Endiness
            
            if "Intel" in full:
                info["Byte Order"] = "Little Endian"

    
    if sib == (2 * cores):
        info["Hyper-threading"] = "Yes" # checks HyperThreading on CPU or not
    return info


if __name__ == "__main__":
    cpuinfo()
