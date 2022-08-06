from socket import timeout
import requests

timeout = 1

try:
    requests.head("http://www.google.com", timeout = timeout)
    print("Internet connection is active")

except requests.ConnectionError:
    print("Internet connection is down")
    