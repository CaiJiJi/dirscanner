#!/usr/bin/python

# web application catalog discovery scanner
# @author Rafal 'bl4de' Janicki | 07.01.2014
#

import httplib
import catalogs

def scan(conn, dirs):
    iterator = 0
    logfile = open("logfile.txt", "w")
    for d in dirs:
        d = d.replace("\n", "")
        _url = "/cmsmadesimple/%s/" % (d)
        conn.request("GET", _url)
        response = conn.getresponse()
        response.read()
        iterator += 1
        if ( iterator % 1000 == 0):
            print "%d scanned so far, scanning..." % (iterator)

        if (response.status == 200 or response.status == 302 or response.status == 304):
            _output = "HTTP %s %s \t\t\turl is %s" % (response.status, response.reason, _url)
            print _output
            logfile.write(_output)
    logfile.close()



def main():
    dirs = open("catalogs.txt", "r")
    adminpanels = catalogs.adminpanels

    conn = httplib.HTTPConnection("localhost")

    print "Trying to locate administration panel:"
    scan(conn, adminpanels)

    print "Trying to find anything else..."
    scan(conn, dirs)

    dirs.close()
    
if __name__ == '__main__':
    main()