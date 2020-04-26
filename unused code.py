#        proxies = {'http:' + ip + ':'+str(proxy_dict[ip])}
#        response = requests.get('http://ya.ru', proxies = proxies)
#        response = requests.get(url)
#        parser = fromstring(response.text)
#        proxies = set()
#        print (ip + ':' + str(proxy_dict[ip]) + ' -- DEAD proxy!') # do it if proxy connect is failed
#
#            print (ip + ':' + str(proxy_dict[ip]) + ' -- LIVE proxy!') # do it if all ok


#    for ip, ipport in proxy:
#        r = 
#        print (r)
#        if (requests.get(url)).json['ok'] !='True' then:
#            print ('Proxy addr ' + ip + ' port ' + ipport + ' is DEAD. ')
#            print ('Continue checking list.')                
#        else:
#            print ('Proxy addr ' + ip + ' port ' + ipport + ' is GOOG. ')
#            print ('Will use it!')
#            proxy_det (ip,ipport)
#            break            

##print ('Will use my request thru the SSL proxy...')
#print ('Trying to fetch freedom...')
#print ('Get data from URL: ' + url)

#r = requests.get(url, proxies = proxies)
#r = requests.get(url)
#print(r.json()['ok'])



def proxycheck(url,ip,port):
    print ('Now I will check ' + proxy_ip + ' port ')
    r = request.get (url)
    if r.json()['ok'] == ok:
        print ('is working now')
    else:
        print ('Dead....Will look better...')