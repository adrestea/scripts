#!/usr/bin/env python

#from urllib import urlencode
import cookielib, urllib2, urllib
import io, os, sys

url_login = 'http://bugzilla.tcl-ta.com/index.cgi?GoAheadAndLogIn=1'
user_data = {'Bugzilla_login':'jianlin.gao', 'Bugzilla_password':'Th123456','Bugzilla_restrictlogin':'on'}

data_post = urllib.urlencode(user_data)
cookie_name = sys.path[0] + os.sep + "cookie"
cj = cookielib.LWPCookieJar(cookie_name)
#cj.save()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

req = urllib2.Request(url_login, data_post)
response = urllib2.urlopen(req)

html = response.read()
if "Welcome to Bugzilla" in html:
    print "Save cookie!!!"
#    cj.save()

html = urllib2.urlopen("http://bugzilla.tcl-ta.com/show_bug.cgi?id=851149").read()

print "Load Html page is successed!!!"
file = open("/home/user/admin4.html",'w')
file.write(s)
file.close()