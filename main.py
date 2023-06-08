import requests

def link_verifier(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is not broken")
        else:
            print(f"{url} is broken")
    except:
        print(f"{url} is broken")

link_verifier("demirblinds.com")