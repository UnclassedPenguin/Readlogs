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
        self.diagnostics()

        self.read_argparse()
        self.final_Print()

        #Uncomment next line to run test function
        # self.test()

    def diagnostics(self):
        self.read_argparse()
        print("ARGS: {}".format(self.args))
        print("SaveDir: {}".format(self.savedir))
        print("RandoNumber: {}".format(self.randonumber))
        print("Filepath: {}".format(self.filepath))

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
        # path = '/var/log/test-auth.log'
        # FINDSTRING = 'Accepted'
        if self.filepath != None:
            with open(self.filepath,'r') as f:
                targets = [line for line in f if findstr in line]
            return targets
        elif self.filepath == None:
            print("Something Bad Happened...")
            return None

    def parse_Authlogaccepted(self):
         targets = self.read_Authlog("Accepted")
         iplist = []
         if targets != None:
             for line in targets:
                 linesplit = line.split()
                 ip = linesplit[10]
                 user = linesplit[8]
                 iplist.append((user, ip))
             final = Counter(iplist)
             return final
         elif targets == None:
             print("Something else bad happened...")
             return None

    def parse_Authloginvaliduser(self):
        invalidusers = self.read_Authlog("Invalid user")
        users = []
        if invalidusers != None:
            for line in invalidusers:
                linesplit = line.split()
                user = linesplit[7]
                ip = linesplit[9]
                users.append((user, ip))
            usersdict = Counter(users)
            return usersdict
        elif invalidusers == None:
            print("Something else bad happened...")
            return None

    def final_Print(self):
        accepteddict = self.parse_Authlogaccepted()
        failedlogins = self.parse_Authloginvaliduser()
        if accepteddict != None and failedlogins != None:
            print("\n")
            print("#### UnclassedPenguin Readlogs ####")
            print("\n")
            print("/var/log/auth.log")
            print("Accepted logins: (user - number - ip)")
            if len(accepteddict) == 0:
                print("\tNone")
            for ip, number in accepteddict.items():
                print("\t{} - {} - {}".format(ip[0], number, ip[1]))
            print("\n")
            print("Failed logins: (user - number - ip)")
            if len(failedlogins) == 0:
                print("\tNone")
            for ip, number in failedlogins.items():
                print("\t{} - {} - {}".format(ip[0], number, ip[1]))
            print("\n")
            try:
                if self.randonumber == 42:
                    print("YOU WON THE JACKPOT HOP ABOARD THE SPACESHIP")
                    print("\n")
            except:
                pass
        elif accepteddict == None or failedlogins == None:
            print("SOMETHING REALLY BAD HAPPENED")

    def read_argparse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-x', nargs='?', type=int, help = 'Just try it...')
        parser.add_argument('-w', nargs='?', type=str, help = 'File location where to save')
        parser.add_argument('-f', nargs='?', type=str, help = 'location of /var/log/auth.log')
        self.args = parser.parse_args()
        self.savedir = self.args.w
        self.filepath = self.args.f
        self.randonumber = self.args.x

def main():
    Readlogs()

if __name__ == "__main__":
	main()
