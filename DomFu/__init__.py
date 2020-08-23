#!/usr/bin/env python3
import socket
import validators
import requests


def fetchCrtSh(domain):
    '''
    string -> list

    This function queries crt.sh to look for domain names in SSL cert issued by the organization.

    Input  : fetchCrtSh("tropyl.com")
    Output : ['*.newsletter.tropyl.com\nnewsletter.tropyl.com', ... 'www.tropyl.com\nwww.www.tropyl.com']

    '''
    subdomains = []

    fetchURL = requests.get(
        "https://crt.sh/?q=%.{d}&output=json".format(d=domain))

    if fetchURL.status_code == 200:
        for (key, value) in enumerate(fetchURL.json()):
            if '@' not in value['name_value']:
                subdomains.append(value['name_value'])

        subdomains = sorted(set(subdomains))

        return(subdomains)


def fetchBufferOverRun(domain):
    '''
    string -> list

    This function queries bufferover.run to look for domain names.

    Input  : fetchBufferOverRun("tropyl.com")
    Output : ['tropyl.com', 'www.tropyl.com']

    '''

    subdomain = []

    fetchURL = requests.get(
        "https://dns.bufferover.run/dns?q=.%s" % (domain))

    jsonResponse = fetchURL.json()
    subdomainlst = jsonResponse['FDNS_A']

    if subdomainlst != None:
        for dom in subdomainlst:
            front, mid, end = dom.partition(",")
            subdomain.append(end)

    subdomain = sorted(set(subdomain))

    if subdomain != None:
        return(subdomain)


def fetchHackerTarget(domain):
    '''
    string -> list

    This function queries Hacker Target to look for domain names.

    Input  : fetchHackerTarget("tropyl.com")
    Output : ['tropyl.com', 'www.tropyl.com']

    '''

    subdomainlst = []

    fetchURL = requests.get(
        "https://api.hackertarget.com/hostsearch/?q=%s" % (domain)).text

    if 'error' not in fetchURL:
        subdomains = str(fetchURL)
        subdomains = subdomains.split()

        for dom in subdomains:
            front, mid, end = dom.partition(",")
            subdomainlst.append(front)

        if subdomainlst != None:
            return(subdomainlst)


def fetchThreatCrowd(domain):
    '''
    string -> list

    This function queries Threat Crowd to look for domain names.

    Input  : fetchThreatCrowd("tropyl.com")
    Output : ['tropyl.com', 'www.tropyl.com']

    '''
    fetchURL = requests.get(
        "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=%s" % (domain))
    jsonResponse = fetchURL.json()

    if int(jsonResponse["response_code"]) == 1:
        subdomains = jsonResponse["subdomains"]
        return(subdomains)


def fetchVirusTotal(domain):
    '''
    string -> list

    This function queries Virus Total to look for domain names.

    Input  : fetchThreatCrowd("tropyl.com")
    Output : ['tropyl.com', 'www.tropyl.com']

    '''
    subdomain = []

    fetchURL = requests.get(
        "https://www.virustotal.com/ui/domains/%s/subdomains" % (domain))

    jsonResponse = fetchURL.json()

    for i in jsonResponse["data"]:
        if i["type"] == 'domain':
            subdomain.append(i['id'])

    return(subdomain)


def search(domain):
    '''
    string -> list

    This function queries all API and tools to look for subdomain(s) of your domain name.

    Input  : DomFu.search("tropyl.com")
    Output : ['tropyl.com', 'www.tropyl.com']

    '''
    try:
        socket.gethostbyname(domain)
        dom_valid = True
    except socket.gaierror:
        dom_valid = False

    subdomain = []

    if validators.domain(domain) and dom_valid:
        try:
            subdomain.extend(fetchCrtSh(domain))
        except:
            pass

        try:
            subdomain.extend(fetchBufferOverRun(domain))
        except:
            pass

        try:
            subdomain.extend(fetchHackerTarget(domain))
        except:
            pass

        try:
            subdomain.extend(fetchThreatCrowd(domain))
        except:
            pass

        try:
            subdomain.extend(fetchVirusTotal(domain))
        except:
            pass

        try:
            subdomain = sorted(set(subdomain))
        except:
            pass

        return(subdomain)

    else:
        return("Error (TPYL_DomFu_INVDOM): Enter a valid domain")
