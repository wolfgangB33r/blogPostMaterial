from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
   ret = {
       'path' : 'home'   
   }
   # now call an internal service method
   products()
   # then return
   return json.dumps(ret)


@app.route('/products')
def products():
   ret = {
       'path' : 'products'   
   }
   return json.dumps(ret)