import requests,re
from bs4 import BeautifulSoup as bs

def get_cf(user):
    r=requests.get(f"https://codeforces.com/profile/{user}").text
    soup=bs(r,'lxml')
    s=soup.find('span',class_='smaller')
    s=s.text
    rating=(re.findall(r'\d+',s)[0])
    col='red'
    y=int(rating)
    if(y<=1199):
    	col='#cec8c1'
    elif(y>1199 and y<=1399):
    	col='#43A217'
    elif(y>1399 and y<=1599):
    	col="#22C4AE"
    elif(y>1599 and y<=1899):
    	col="#1427B2"
    elif(y>1899 and y<=2199):
    	col="#700CB0"
    elif(y>2199 and y<=2399):
    	col="#F9A908"
    else:
    	col="#FF0000"
    return [rating,col]

def get_cc(user):
    url=f'https://www.codechef.com/users/{user}'
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    rating = soup.find_all('small')
    rating=(re.findall(r'\d+',rating[-1].text))
    col='red'
    y=int(rating[0])
    if(y<=1399):
        col='#6A6860'
    elif(y>1399 and y<=1599):
        col='#3D8C0B'
    elif(y>1599 and y<=1799):
        col="#347FBD"
    elif(y>1799 and y<=1999):
        col="#7A4AAF"
    elif(y>1999 and y<=2199):
        col="#FFC300"
    elif(y>2199 and y<=2499):
        col="#FF9E1B"
    else:
        col="#FF1B1B"
    return [rating[0],col]

def get_at(user):
    url=f'https://atcoder.jp/users/{user}'
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    x=soup.find_all('table',class_='dl-table')
    y=x[1].find_all('span')
    y=[i.text for i in y]
    val=y[y.index('―')-1]
    col='red'
    a=int(val)
    if(a<=399):
        col='#8E8E81'
    elif(a>399 and a<=799):
        col='#81501B'
    elif(a>799 and a<=1199):
        col='#5CB01E'
    elif(a>1199 and a<=1599):
        col='#16E5D8'
    elif(a>1599 and a<=1999):
        col='#1642E5'
    elif(a>1999 and a<=2399):
        col='#CFE115'
    elif(a>2399 and a<=2799):
        col='#FF8700'
    else:
        col='#FF0000'
    return [val,col]