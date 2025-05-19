import re
import json
import requests

from bs4 import BeautifulSoup as bs


def get_info(handle, website):
    website = website.lower()
    if website == 'codechef':
        return get_cc(handle)
    elif website == 'codeforces':
        return get_cf(handle)
    elif website == 'atcoder':
        return get_at(handle)
    elif website == 'topcoder':
        return get_top(handle)
    elif website == 'yukicoder':
        return get_yuki(handle)
    elif website == 'leetcode':
        return get_leetcode(handle)
    elif website == 'leetcode-cn':
        return get_leetcode_cn(handle)
    else:
        raise ValueError('wrong platform website name')


def get_cf(user):
    url = f'https://codeforces.com/api/user.info?handles={user}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    user_data = data['result'][0]
    rating = user_data.get('rating', 0)
    
    # Determine color based on rating
    col = 'red'
    if rating <= 1199:
        col = '#cec8c1'
    elif rating <= 1399:
        col = '#43A217'
    elif rating <= 1599:
        col = "#22C4AE"
    elif rating <= 1899:
        col = "#1427B2"
    elif rating <= 2099:
        col = "#700CB0"
    elif rating <= 2299:
        col = "#F9A908"
    elif rating <= 2399:
        col = "#FBB948"
    else:
        col = "#FF0000"
        
    return [rating, col]


def get_cc(user):
    url = f'https://www.codechef.com/users/{user}'
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    rating = soup.find_all('small')
    if(len(rating)==5):
        rating = (re.findall(r'\d+', rating[-2].text))
    else:
        rating = (re.findall(r'\d+', rating[-1].text))
    col = 'red'
    y = int(rating[0])
    if (y <= 1399):
        col = '#6A6860'
    elif (y > 1399 and y <= 1599):
        col = '#3D8C0B'
    elif (y > 1599 and y <= 1799):
        col = "#347FBD"
    elif (y > 1799 and y <= 1999):
        col = "#7A4AAF"
    elif (y > 1999 and y <= 2199):
        col = "#FFC300"
    elif (y > 2199 and y <= 2499):
        col = "#FF9E1B"
    else:
        col = "#FF1B1B"
    return [rating[0], col]


def get_at(user):
    url = f'https://atcoder.jp/users/{user}'
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    x = soup.find_all('table', class_='dl-table')
    y = x[1].find_all('span')
    y = [i.text for i in y]
    val = y[y.index('―') - 1]
    col = 'red'
    a = int(val)
    if (a <= 399):
        col = '#8E8E81'
    elif (a > 399 and a <= 799):
        col = '#81501B'
    elif (a > 799 and a <= 1199):
        col = '#5CB01E'
    elif (a > 1199 and a <= 1599):
        col = '#16E5D8'
    elif (a > 1599 and a <= 1999):
        col = '#1642E5'
    elif (a > 1999 and a <= 2399):
        col = '#CFE115'
    elif (a > 2399 and a <= 2799):
        col = '#FF8700'
    else:
        col = '#FF0000'
    return [val, col]


def get_top(user):
    url = f'https://api.topcoder.com/v5/members/{user}'
    json_data = requests.get(url).json()
    rating = json_data['maxRating']['rating']
    color = json_data['maxRating']['ratingColor']
    return [rating, color]


def get_yuki(user):
    url = f'https://yukicoder.me/api/v1/user/name/{user}'
    json_data = requests.get(url).json()
    level = str(json_data['Level'])
    color = '#2ecc71'
    return [level, color]


def get_leetcode(username):
    url = 'https://leetcode.com/graphql'
    queryString = '''query userContestRankingInfo($username: String!) {
                        userContestRanking(username: $username) {
                            rating
                        }
                    } '''
    variables = {
        "username": username,
    }
    payload = json.dumps({"query": queryString, "variables": variables})
    r = requests.request("POST", url, headers={'Content-Type': 'application/json'}, data=payload)
    json_data = r.json()
    rankings = json_data['data']['userContestRanking']['rating']
    rankings = round(rankings)
    return [rankings, '#FFA116']


def get_leetcode_cn(username):
    url = 'https://leetcode.cn/graphql'
    r = requests.post(
        url,
        json={
            "operationName":
            "userPublicProfile",
            "variables": {
                "userSlug": username
            },
            "query":
            'query userPublicProfile($userSlug: String!) {userProfilePublicProfile(userSlug: $userSlug){profile{ranking{ratingProgress}}}}'
        })
    json_data = r.json()
    rankings = max(d for d in json_data['data']['userProfilePublicProfile']
                   ['profile']['ranking']['ratingProgress'])
    return [rankings, '#FFA116']
