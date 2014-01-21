#!/usr/bin/python

# web application catalog discovery scanner
# @author Rafal 'bl4de' Janicki | 07.01.2014
#

import httplib
import catalogs
import sys


def scan(conn, dirs):
    iterator = 0
    logfile = open("logfile.txt", "a")
    for d in dirs:
        d = d.replace("\n", "")
        _url = "/%s" % (d)
        _output = ""

        print "checking %s" % (_url)

        conn.request("GET", _url)
        response = conn.getresponse()
        response.read()
        iterator += 1
        if ( iterator % 100 == 0):
            print "%d scanned so far, scanning..." % (iterator)

        if (response.status == 200 or response.status == 302 or response.status == 304):
            _output = "HTTP %s %s \t\t\turl is %s" % (response.status, response.reason, _url)
        if (response.status == 401):
            _output = "HTTP %s %s \t\t\t, Unauthorized; url is %s" % (response.status, response.reason, _url)
        if (response.status == 403):
            _output = "HTTP %s %s \t\t\t, Needs authorization; url is %s" % (response.status, response.reason, _url)

        if (_output != ""):
            print _output
            logfile.writelines(_output + "\n")

    logfile.close()



def main():
    dirs = open("catalogs.txt", "r")
    adminpanels = catalogs.adminpanels

    conn = httplib.HTTPConnection(sys.argv[1])

    print "Trying to locate administration panel:"
    scan(conn, adminpanels)

    # print "Trying to find anything else..."
    # scan(conn, dirs)

    dirs.close()
    
if __name__ == '__main__':
    main()