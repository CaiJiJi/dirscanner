#!/usr/bin/python

# web application catalog discovery scanner
# @author Rafal 'bl4de' Janicki | 07.01.2014
#

import httplib

def scan(conn, dirs):
    iterator = 0
    logfile = open("logfile.txt", "w+")
    for d in dirs:
        d = d.replace("\n", "")
        _url = "/cmsmadesimple/%s/" % (d)
        conn.request("GET", _url)
        response = conn.getresponse()
        response.read()
        iterator += 1
        if ( iterator % 1000 == 0):
            print "%d scanned so far, scanning..." % (iterator)

        if (response.status == 200 or response.status == 302):
            _output = "HTTP %s %s \t\t\turl is %s" % (response.status, response.reason, _url)
            print _output
            logfile.write(_output)


def main():
    dirs = open("catalogs.txt", "r")
    conn = httplib.HTTPConnection("localhost")

    scan(conn, dirs)
    
if __name__ == '__main__':
    main()