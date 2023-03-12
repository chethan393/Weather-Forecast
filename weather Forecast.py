import requests
city = input ('name of the city')
print (city)
print ('Displaying whether report for: ' +city )
url='https://wttr.in/ {]'.format (city)
res = requests.get (url)
print (res.text)
