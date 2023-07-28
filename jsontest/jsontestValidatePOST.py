#!/usr/bin/env python3

import requests
import json


POSTURL= "http://validate.jsontest.com/"

def main():
    mydata = {"json":"{'fruit':['apple', 'pear'], 'vegetable': ['carrot']}"}

    resp = requests.post(POSTURL, data =mydata)

    respjson = resp.json()

    print(respjson)

    print(f"is your json valid? {respjson['validate']}")

if __name__ == "__main__":
    main()

