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

        #Uncomment next line to run some self tests
        # self.diagnostics()

        self.read_argparse()
        self.final_Print()

        #Uncomment next line to run test function
        # self.test()

    def diagnostics(self):
        self.read_argparse()
        print("ARGS: {}".format(self.args))
        print("SaveDir: {}".format(self.savedir))
        print("RandoNumber: {}".format(self.randonumber))

    def test(self):
        targets = self.read_Authlog("Accepted")
        iplist = []
        for line in targets:
            linesplit = line.split()
            ip = linesplit[10]
            user = linesplit[8]
            iplist.append((user, ip))
        final = Counter(iplist)
        print(final)
        for ip, number in final.items():
            print("{} - {} - {}".format(ip[0], number, ip[1]))


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
             user = linesplit[8]
             iplist.append((user, ip))
         final = Counter(iplist)
         return final

    def parse_Authloginvaliduser(self):
        invalidusers = self.read_Authlog("Invalid user")
        users = []
        for line in invalidusers:
            linesplit = line.split()
            user = linesplit[7]
            ip = linesplit[9]
            users.append((user, ip))
        usersdict = Counter(users)
        return usersdict

    def final_Print(self):
        accepteddict = self.parse_Authlogaccepted()
        failedlogins = self.parse_Authloginvaliduser()
        print("\n")
        print("#### UnclassedPenguin Readlogs ####")
        print("\n")
        print("/var/log/auth.log")
        print("Accepted logins: (user - number - ip)")
        for ip, number in accepteddict.items():
            print("\t{} - {} - {}".format(ip[0], number, ip[1]))
        print("\n")
        print("Failed logins: (user - number - ip)")
        for ip, number in failedlogins.items():
            print("\t{} - {} - {}".format(ip[0], number, ip[1]))
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
        self.args = parser.parse_args()
        self.savedir = self.args.w
        self.randonumber = self.args.x

def main():
    Readlogs()

if __name__ == "__main__":
	main()
