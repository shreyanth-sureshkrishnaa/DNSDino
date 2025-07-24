import whois
import dns.resolver
import socket
from ipwhois import IPWhois   
import requests

def formatDate(date):
    if isinstance(date, list):
        date = date[0]  # Take the first element
    if hasattr(date, 'strftime'):
        return date.strftime('%Y-%m-%d %H:%M:%S')
    return str(date)


def resolveDNSRecords(domain):
    records = {}

    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            records[rtype] = [str(answer.to_text()) for answer in answers]

        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.exception.Timeout):
            records[rtype] = []

        except Exception as e:
            records[rtype] = [f"Error: {str(e)}"]

    return records


def getWHOISInfo(domain):
    try:
        info = whois.whois(domain)
        return {
            "Domain Name": info.domain_name,
            "Registrar": info.registrar,
            "Creation Date": formatDate(info.creation_date),
            "Expiration Date": formatDate(info.expiration_date),
            "Name Server": info.name_server,
            "Emails": info.emails
        }
    except Exception as e:
        return {"error": str(e)}
    
def getIP(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception as e:
        return f"Error: {e}"
    
def getASNInfo(ip):
    try:
        obj = IPWhois(ip)
        result = obj.lookup_rdap()
        return {
                "asn": result.get("asn"),
                "asn_description": result.get("asn_description"),
                "network_name": result.get("network", {}).get("name")
                }
    except Exception as e:
        return {"error": str(e)}

def getIPGeolocation(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}")
        data = res.json()
        return {
            "country": data.get("country"),
            "region": data.get("regionName"),
            "city": data.get("city"),
            "org": data.get("org"),
            "lat": data.get("lat"),
            "lon": data.get("lon")
        }
    except Exception as e:
        return {"error": str(e)}

def getNetworkInfo(domain):
    ip = getIP(domain)
    asn = getASNInfo(ip) if isinstance(ip, str) and '.' in ip else {}
    geo = getIPGeolocation(ip) if isinstance(ip, str) and '.' in ip else {}
    return {
        "ip": ip,
        "asn": asn,
        "geolocation": geo
    }