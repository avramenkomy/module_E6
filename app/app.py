from bottle import route, run, request, HTTPError
from pymemcache.client.base import Client
import json
import os

MEMCACHED_HOST = os.environ.get('MEMCACHED_HOST')

def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2

def json_deserializer(key, value, flags):
    if flags == 1:
        return value.decode("utf-8")
    if flags == 2:
        return json.loads(value.decode("utf-8"))

def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a


@route("/")
def hello():
    return "Hello"

@route("/<num:int>")
def fib_handler(num):
    client = Client((MEMCACHED_HOST, '11211')
        , serializer=json_serializer
        , deserializer=json_deserializer)
    fib_result = client.get(str(num)) 
    if fib_result is None:
        result = fib(num)
        client.set(str(num), result)  
    else: 
        result = fib_result
    print('fib_result=', fib_result)
    return str(result)


if __name__ == "__main__":
    run(host="127.0.0.1", port=8081)