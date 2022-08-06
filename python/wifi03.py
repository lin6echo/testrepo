import urllib.request



def is_cnx_active():
    
        request = urllib.request.urlopen('https://www.google.com')
        print(request.reason)
        
    
    
       
    
is_cnx_active()
    