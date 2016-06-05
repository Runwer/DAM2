import urllib

page = urllib.urlopen("http://www.dr.dk/nyheder/live/live-amagerbank-direktoer-forklarer-sig-i-retten").read()
print page.find('live-wrapper')

