#!/usr/bin/python

# web application catalog discovery scanner
# @author Rafal 'bl4de' Janicki | 07.01.2014
#

import httplib

def scan(conn):
    for d in dirs:
        d = d.replace("\n", "")
        _url = "/cmsmadesimple/%s/" % (d)
        conn.request("GET", _url)
        response = conn.getresponse()
        response.read()
        if (response.status == 200 or response.status == 302):
            print "HTTP %s %s \t\t\turl is %s" % (response.status, response.reason, _url)


dirs = open("folders.txt", "r")
conn = httplib.HTTPConnection("localhost")

scan(conn)