import subprocess
from os.path import basename
import os
import getpass

# check for sudo -l
def run_sudo():


    print(f"Checking for SUDO Permissions\n")
    output = subprocess.run(["sudo", "-l"], capture_output=True, text=True)
    print(output.stdout)


run_sudo()


# check for users using passwd file
def passwd():


    print(f"checking for user information\n")
    output = subprocess.run(["cat","/etc/passwd"],capture_output=True, text=True)
    out = output.stdout.split("\n")
    users = [user for user in out if "/bin/bash" in user]
    if users:
        print('\n'.join(users))


passwd()


# check if passwd file is writable 
def passwd_Writable():

    print("\nchecking for writable passwd file\n")
    output = subprocess.run(["ls","-l","/etc/passwd"], capture_output=True, text=True)
    out = output.stdout.split("\n")
    writable = [w for w in out if "-rw-r--rw-" in w]
    if writable:
       print("passwd file is writable\n")


passwd_Writable()

# check for readable shadow file
def shadow_read():
    print("checking for readable shadow file\n")
    output = subprocess.run(["ls","-l","/etc/shadow"], capture_output=True, text=True)
    out = output.stdout.split("\n")
    read = [r for r in out if "-rw-r--r--" in r]
    if read:
       print(f"shadow file is readable\n{out}")

shadow_read()
#check for writable shadow file
def shadow_write():
    print("checking for writable shadow file\n")
    output = subprocess.run(["ls","-l","/etc/shadow"], capture_output=True, text=True)
    out = output.stdout.split("\n")
    writeable = [w for w in out if "-rw-r--rw-" in w]
    if writeable:
       print(f"shadow file is writable\n{out}")


shadow_write()

# check for SUID binaries
def SUID():


    print(f"Checking for SUID Binaries\n")
    output = subprocess.run(["find", "/", "-perm","-u=s", "-type", "f"], capture_output=True, text=True)
    suids = output.stdout.split("\n")
    excluded = ["fusermount","Xorg.wrap","polkit-agent-helper-1","chrome-sandbox","dbus-daemon-launch-helper","vmware-user-suid-wrapper","ssh-keysign","chfn", "chsh", "fusermount3", "gpasswd", "kismet", "mount", "newgrp", "ntfs-3g", "passwd", "pkexec", "su", "sudo", "umount","pppd"]
    binaries = [binary for binary in suids if basename(binary) not in excluded]
    if binaries:
        print('\n'.join(binaries))

    else:
        print("no abnormal suids present")


SUID()

# check for cronjobs
def Cronjobs():


    print(f"Now Checking for cronjobs\n")
    output = subprocess.run(["cat","/etc/crontab"],capture_output=True, text=True)
    out = output.stdout.split("\n")
    jobs = [line for line in out if "*/5 * * * *" in line or "* * * * *" in line]
    if jobs:
        print("looks like theirs some interesting cronjobs\n",'\n'.join(jobs))

    else:
        print("no cronjobs running every minute or 5 minutes")


Cronjobs()

# check for kernel version
def kernel():


    print(f"Now Checking kernel version\n")
    output = subprocess.run(["uname","-a"],capture_output=True, text=True)
    print(output.stdout)


kernel()

# check for .conf files
def conf():
    print("checking for config files")
    with open("excluded_files") as f:
        excluded_files = f.read().splitlines()
    for root, dirs, files in os.walk('/'):
        for file in excluded_files:
            if file in files:
                files.remove(file)
        for file in files:
            if file.endswith('.conf'):
               os.access(file, os.W_OK or os.R_OK) 
               print(file)
    

conf()


# check for directories owned by the current user 

def directories():
    print("checking for directories owned by our user")
    excluded_dirs = ["proc", "run", "user", "dev", "usr", "sys","etc",".cache",".config",".mozilla",".local",".ipython"]

    for root, dirs, files in os.walk('/'):
        for dir in excluded_dirs:
            if dir in dirs:
                dirs.remove(dir)
        for dir in dirs:
            full_path = os.path.join(root,dir)
            if os.stat(full_path).st_uid == os.getuid():
                print(full_path)
directories()

# get all files owned by root we can write to
def files():
    print("checking for files we can write to\n")
    excluded_dirs = ["proc", "run", "user", "dev", "usr", "sys","etc"]
    current_user = getpass.getuser() # get the current user
    for dirpath, dirnames, filenames in os.walk('/'): # for loop to get the dirs
        for directory in excluded_dirs: # remove the directories not wanted , starting here and finishing at next for loop
            if directory in dirnames:
                dirnames.remove(directory)
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if os.stat(full_path).st_uid == 0 and os.access(full_path, os.W_OK):
                print(f'{full_path} (file)')

files() 


# check for nfs no squash


server = input("Please enter the host ip: ")

def No_Squash(server):


    print(f"Cheching for possible nfs no squash")
    output = subprocess.run(["showmount", "-e", server], capture_output=True, text=True)
    out = output.stdout.decode()
    if "no_squash" in out:
        print(f"The nfs server {server} has no squash enabeled") 


No_Squash(server)
