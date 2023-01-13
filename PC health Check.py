#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    du=shutil.disk_usage(disk)
    dfree=du.free/du.total*100
    return dfree>20

def check_cpu_usage():
    ci=psutil.cpu_percent(1)
    return ci<75

if not check_cpu_usage() or not check_disk_usage("/"):
    print("Error in PC health")
else:
    print("Everything is Okay!")
    
