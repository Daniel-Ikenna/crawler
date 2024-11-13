#!/usr/bin/env pyhton
import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "192.168.**.**"

with open("/home/kali/Downloads/common.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url )


# code for Discovering Subdomains
# with open("/home/kali/Downloads/subdomainslist.txt", "r") as wordlist_file:
#     for line in wordlist_file:
#         word = line.strip()
#         test_url = word + "." + target_url
#         response = request(test_url)
#         if response:
#             print("[+] Discovered Subdomain --> " + test_url )