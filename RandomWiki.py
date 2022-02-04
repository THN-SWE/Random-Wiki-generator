from  bs4 import BeautifulSoup
import requests as rq
import webbrowser

#getting the wikipedia random wiki url
url = rq.get('https://en.wikipedia.org/wiki/Special:Random')

#parsing the url
soup = BeautifulSoup(url.content,'html.parser')

#gettimg the title
title = soup.find(class_ = "firstHeading").text

#main function
def randwiki():
    
    print(f'{title} \n Do you want to open the page? (y/n)')
    ans = input(':').lower()
    if ans == 'y':
        url = 'https://en.m.wikipedia.org/wiki/%s' %title
        
        webbrowser.open(url)
    
    elif ans == 'n':
        print('try again')
    
    else:
	    print('wrong choice!')
	
randwiki()	

	
		
