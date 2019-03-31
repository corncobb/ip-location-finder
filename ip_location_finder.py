#!/usr/bin/env python
'''IP Location Finder by Cameron Cobb
This script makes use of the API's on https://tools.keycdn.com/'''

import requests

class IPfinder:
    def __init__(self):
        self.keycdn = "https://tools.keycdn.com/geo.json?host="

    def find_ip_location(self, ipaddr):
        self.keycdn = self.keycdn + ipaddr
        request_webpage = requests.get(self.keycdn)
        data = request_webpage.json()

        if data['status'] == "success":
            print(data['description'])
            for key, val in data['data']['geo'].items():
                print(str(key) + " = " + str(val))

        elif data['status'] == "error":
            print(data['description'])

        else:
            print("Undefined error")

        print('\n' + '*'*20 + '\n')

    def start_app(self, ipaddr):
        if not ipaddr:
            print("Please put a valid IP address")

        else:
            self.find_ip_location(ipaddr)

if __name__ == "__main__":
    try:
        while True:
            IPLOC = IPfinder()
            IP = str(input("Enter the IP address: "))
            IPLOC.start_app(IP)

    except KeyboardInterrupt:
        print("Bye!")
