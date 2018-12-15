#!/usr/bin/env python3

from collections import Counter

def read_Authlog():
    path = '/var/log/test-auth.log'
    FINDSTRING = 'Accepted'
    with open(path,'r') as f:
        targets = [line for line in f if FINDSTRING in line]
    return targets

def parse_Authlog():
    targets = read_Authlog()
    iplist = []
    ipdict = {}
    for line in targets:
        linesplit = line.split()
        ip = linesplit[10]
        iplist.append(ip)
    final = Counter(iplist)
    print(final)
    return final

def final_Print():
    final = parse_Authlog()
    print("/var/log/auth.log IP Occurences:")
    for ip, number in final.items():
        print("{} - {}".format(ip, number))

def main():
    # parse_Authlog()
    final_Print()

if __name__ == "__main__":
	main()
