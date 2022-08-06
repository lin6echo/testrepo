import requests

timeout = 1

def is_cnx_active(timeout):
    try:
        requests.head("http://www.google.com", timeout = timeout)
        return True
    except requests.ConnectionError:
        return False
   
if (is_cnx_active(timeout)):
    print(True)
else:
    print(False)