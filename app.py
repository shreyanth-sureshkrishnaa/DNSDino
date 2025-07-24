from flask import Flask, render_template, request
from intel_tools import getWHOISInfo, resolveDNSRecords
import socket
import whois
import os
from ipwhois import IPWhois
import requests
from intel_tools import getASNInfo, getIP, getIPGeolocation, getNetworkInfo
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/results", methods=["POST"])
def results():
    domain = request.form['domain']
    dns_records = resolveDNSRecords(domain)
    network_info = getNetworkInfo(domain)
    whois_info = getWHOISInfo(domain)


    return render_template(
        "results.html",
        domain=domain,
        whois = whois_info,
        dns = dns_records,
        dns_records=dns_records,
        network_info=network_info
    )

@app.route("/help")
def help():
    return render_template('help.html')

@app.route("/credits")
def credits():
    return render_template('credits.html')

@app.route("/learn")
def learn():
    return render_template('learn.html')

@app.route("/glossary")
def glossary():
    return render_template('glossary.html')







@app.route("/module1", methods=['GET', 'POST'])
def module1():
    return render_template('module1.html')

@app.route("/module2", methods=['GET', 'POST'])
def module2():
    return render_template('module2.html')

@app.route("/module3", methods=['GET', 'POST'])
def module3():
    return render_template('module3.html')

@app.route("/module4", methods=['GET', 'POST'])
def module4():
    return render_template('module4.html')

@app.route("/module5", methods=['GET', 'POST'])
def module5():
    return render_template('module5.html')

@app.route("/module6", methods=['GET', 'POST'])
def module6():
    return render_template('module6.html')

if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
