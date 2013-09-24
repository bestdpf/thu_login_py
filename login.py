import urllib
import urllib2
import hashlib
url = 'http://net.tsinghua.edu.cn/cgi-bin/do_login'

origin_name='dpf13' #put your name here
origin_pass='' #put your passwd here
md5_pass=hashlib.md5(origin_pass).hexdigest()
#print md5_pass
#quit()
values = {'username' : origin_name,
          'password' : md5_pass,
          'drop' : '0' ,
          'type' : '1',
          'n': '100'}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
