'''
The process for building the request is as follows:
- Combine all params (except sign_type and sign) into a alphabetically sorted list in the form key=value&
- Attach your AliPay MD5 secret to the signstring
- Calculate the MD5 hash from this combined string
- Attach the sign_type and sign parameter with the above generate MD5 has value
'''

import requests
import hashlib 

SANDBOX_URL = "https://mapi.alipaydev.com/gateway.do"

MERCHANT_ACCOUNT = "forex_???@alitest.com"
MERCHANT_PID = "208??"
MD5_SIGNATURE = "???"

CURRENCY = "USD"

PARAMS = {
    "service" : "alipay.acquire.precreate",
    "partner" : MERCHANT_PID,
    "seller_id" : MERCHANT_PID,
    "seller_email" : MERCHANT_ACCOUNT,
    "_input_charset" : "UTF-8",
    "product_code" : "OVERSEAS_MBARCODE_PAY",
    "currency" : CURRENCY,
    "trans_currency" : CURRENCY,
    "out_trade_no" : "12312323234",
    "subject" : "wolfgangrechnung",
    "total_fee" : "6.38"
}

# now create the pre-sign string
PRE_SIGN_STRING = ""

SIGN_TYPE = "MD5"
SIGN = ""

for key in sorted(PARAMS.keys()):
    PRE_SIGN_STRING = PRE_SIGN_STRING + key + '=' + PARAMS[key] + '&' 

# remove last & sign
PRE_SIGN_STRING = PRE_SIGN_STRING[:-1]
print(PRE_SIGN_STRING)

m = hashlib.md5()
# append the secret MD5 secret key and hash it with MD5
m.update(PRE_SIGN_STRING+MD5_SIGNATURE)
print(m.hexdigest())
SIGN = m.hexdigest()

#print(PRE_SIGN_STRING)
# Create Pre-Sign String (https://global.alipay.com/docs/ac/app/pre_sign)
# https://global.alipay.com/docs/ac/global/precreate_transaction

#r = requests.get(SANDBOX_URL + "?" + PRE_SIGN_STRING + "&sign_type=" + SIGN_TYPE + "&sign=" + SIGN)
print(SANDBOX_URL + "?" + PRE_SIGN_STRING + "&sign_type=" + SIGN_TYPE + "&sign=" + SIGN) 
#print(r.status_code)
#print(r.text)

