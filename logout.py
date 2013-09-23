#import urllib
import urllib2
url = 'http://net.tsinghua.edu.cn/cgi-bin/do_logout'
req = urllib2.Request(url, None)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page