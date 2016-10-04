from HTMLParser import HTMLParser
import urllib2
count = 0
class myParser(HTMLParser):
    # def __init__(self):
        # self._count = 0
        # pass

    def handle_starttag(self,tag,attrs):
        global count
        if tag == 'a':
            for a in attrs:
                if a[0] == 'href':
                    link = a[1]
                    if link.find('http') >=0:
                        print('{} : {}'.format(count,link.strip()))
                        # print(' {}'.format(link))
                        count = count + 1
                        newParse = myParser()
                        newParse.feed(link)


# url = 'http://www.baidu.com'
url = 'http://www.to8to.com'
request = urllib2.Request(url)
handle = urllib2.urlopen(request)
parser = myParser()
parser.feed(handle.read())
