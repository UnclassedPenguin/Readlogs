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
        self.ask_User()
        if self.option == '1':
            self.ask_Userlogfile()
            self.read_argparse()
            self.final_Print()
        elif self.option == '2':
            print("Option 2")
        elif self.option == '3':
            exit()
        else:
            print("Other option")
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

    def ask_User(self):
        print("\n")
        print("###################################")
        print("#### UnclassedPenguin Readlogs ####")
        print("###################################")
        print("\n")
        print("1. Look at /var/log/auth.log")
        print("2. This is another option")
        print("3. Quit")
        print("\n")
        self.option = input("What would you like to do? (1, 2, 3...) ")
        print("\n")
        return self.option

    def ask_Userlogfile(self):
        print("\n")
        self.authlogfile = input("What auth file in /var/log/ would you like to read? ")
        print("\n")
        return self.authlogfile

    def read_Authlog(self, findstr):
        # path = '/var/log/test-auth.log'
        # FINDSTRING = 'Accepted'
        filepath = '/var/log/' + self.authlogfile
        with open(filepath,'r') as f:
            targets = [line for line in f if findstr in line]
        return targets

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
            print("---- /var/log/auth.log ----")
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
            Readlogs()
        elif accepteddict == None or failedlogins == None:
            print("SOMETHING REALLY BAD HAPPENED")

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
