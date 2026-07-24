import requests
from requests import exceptions
import asyncio
import time as Time
async def try_subdomain(subdomain : str):
    subdomain = subdomain.strip()

    url = f"http://{subdomain}.example.com"
    try:
        requests.get(url)
        print(f"[+] Found subdomain: {url}")
    except exceptions.ConnectionError:
        print(f"[-] Could not find subdomain: {url}")



async def try_subdomains():
    st = Time.time()
    with open("subdomainlist.txt", "r") as subdomains:
        for subdomain in subdomains:
            await try_subdomain(subdomain)
    et = Time.time()
    print(f"[+] total time: {et-st}")



def try_sub_sync():
    st = Time.time()
    with open("subdomainlist.txt", "r") as subdomains:
        for subdomain in subdomains:
            url = f"http://{subdomain}.example.com"
            try:
                requests.get(url)
                print(f"[+] Found subdomain: {url}")
            except exceptions.ConnectionError:
                print(f"[-] Could not find subdomain: {url}")

    et = Time.time()
    print(f"[+] total time: {et-st}")



if __name__ == '__main__':
    try_sub_sync()
    asyncio.run(try_subdomains())