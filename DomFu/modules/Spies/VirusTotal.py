#!/usr/bin/env python3
'''
Copyright (C) 2020, DomFu Contributors.
See the LICENSE.txt file for copying permission.
'''

import requests


def fetchVirusTotal(domain, api):
    '''
    string -> list

    This function queries Virus Total to look for domain names.

    Input  : fetchVirusTotal("tropyl.com")
    Output : ['tropyl.com', 'www.tropyl.com']

    '''
    subdomain = []
    headers = {'x-apikey': api}
    session = requests.Session()
    url = 'https://www.virustotal.com/api/v3/domains/{d}/subdomains'
    formaturl = url.format(d=domain)

    try:
        resp = session.get(
            formaturl, timeout=25, headers=headers).json()
    except:
        return (subdomain)

    if 'error' in resp:
        return (subdomain)

    if 'links' in resp and 'next' in resp['links']:
        formaturl = resp['links']['next']
    else:
        formaturl = ''

    try:
        for i in resp['data']:
            if i['type'] == 'domain':
                subdom = i['id']
                if not subdom.endswith(domain):
                    continue
                else:
                    subdomain.append(subdom)

    except Exception:
        pass

    return (subdomain)