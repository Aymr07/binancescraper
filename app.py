import urllib.request as ureq

url = "https://www.binance.com/en/support/announcement/c-48?navId=48"
 
data = ureq.urlopen(url).read()

