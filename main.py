import requests

def check_if_broken(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'    {url} is not broken')
        else:
            print(f'    {url} is broken')
    except:
        print(f'    {url} is broken')

def check_if_link(link):
    if (link == '') | (type(link) != str):
        print('The entered value is not a valid link, try again: ')
        print('----------------------------')
        return -1
    else:
        check_if_broken(link)

def driver():
    print('This script checks if a given link is broken or not: ')
    link = input('Enter a link to verify: ')
    return link

link = driver()
if check_if_link(link) == -1:
    driver()

# demirblinds.com