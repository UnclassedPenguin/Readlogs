#!/usr/bin/env python3

'''
Copyright © 2018 UnclassedPenguin
App: Read Logs
Author: UnclassedPenguin
Description: An app to check your server log files
'''

import argparse
from collections import Counter

class Readlogs():

    def __init__(self, parent=None):
        self.read_argparse()
        self.final_Print()

    def read_Authlog(self, findstr):
        path = '/var/log/test-auth.log'
        # FINDSTRING = 'Accepted'
        with open(path,'r') as f:
            targets = [line for line in f if findstr in line]
        return targets

    def parse_Authlogaccepted(self):
        targets = self.read_Authlog("Accepted")
        iplist = []
        for line in targets:
            linesplit = line.split()
            ip = linesplit[10]
            iplist.append(ip)
        final = Counter(iplist)
        return final

    def parse_Authloginvaliduser(self):
        invalidusers = self.read_Authlog("Invalid user")
        users = {}
        for line in invalidusers:
            split = line.split()
            users['{}'.format(split[7])] = split[9]
        return users

    def final_Print(self):
        accepteddict = self.parse_Authlogaccepted()
        failedlogins = self.parse_Authloginvaliduser()
        print("\n")
        print("#### UnclassedPenguin Readlogs ####")
        print("\n")
        print("/var/log/auth.log Accepted login IP Occurences: (number - ip)")
        for ip, number in accepteddict.items():
            print("\t{} - {}".format(number, ip))
        print("\n")
        print("Failed login attempts: (user - ip)")
        for user, ip in failedlogins.items():
            print("\t{} - {}".format(user, ip))
        print("\n")
        try:
            if self.randonumber == 42:
                print("YOU WON THE JACKPOT HOP ABOARD THE SPACESHIP")
                print("\n")
        except:
            pass

    def read_argparse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-x', nargs='?', type=int, help = 'Just try it...')
        parser.add_argument('-w', nargs='?', type=str, help = 'File location where to save')
        args = parser.parse_args()
        self.savedir = args.w
        self.randonumber = args.x
        print("ARGS: {}".format(args))
        print("SaveDir: {}".format(self.savedir))
        print("RandoNumber: {}".format(self.randonumber))

def main():
    Readlogs()

if __name__ == "__main__":
	main()
