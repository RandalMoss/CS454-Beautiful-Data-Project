from lxml import html
import requests
class MyClass(object):
    print ""
    #pull down weather data
    #only keep relevant info
    page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    tree = html.fromstring(page.text)
    print(tree)
    #record zip code source (rancho cucamonga only for now)
    #find all zip codes around a radius from the source
    
    #report all information to console