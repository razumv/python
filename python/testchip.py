from bs4 import BeautifulSoup
from random import choice, uniform
from time import sleep
 
 
def get_html(url, useragent=None, proxy=None):
    print('get_html')
    r = requests.get(url, headers=useragent, proxies=proxy)
    return r.text
 
 
def get_ip(html):
    print('get_ip')
    print('New Proxy & User-Agent:')
    soup = BeautifulSoup(html, 'lxml')
    ip = soup.find('span', class_='ip').text.strip()
    ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
    print(ip)
    print(ua)
    print('---------------------------')
 
 
def main():
    url = 'https://sitespy.ru/my-ip'
 
    useragents = open('useragents.txt').read().split('\n')
    proxies = open('proxies.txt').read().split('\n')
 
    for i in range(10):
        # sleep(uniform(3, 6))
 
        proxy = {'http': 'http://' + choice(proxies)}
        useragent = {'User-Agent': choice(useragents)}
        try:
            html = get_html(url, useragent, proxy)
        except:
            continue
        get_ip(html)
 
 
if __name__ == '__main__':
    main()