import urllib2
import re

def disallowed():
    content = urllib2.urlopen('https://www.pinterest.com/robots.txt')
    matches = []
    for row in content.readlines():
        match = re.match('^Disallow: (.*)\n', row)
        if match:
            matches.append(match.group(1))
    return matches

if __name__ == '__main__':
    things = disallowed()
    for thing in things:
        print(thing) 
