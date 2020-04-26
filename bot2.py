import requests
from time import sleep

#from proxy_requests import ProxyRequests

url = 'https://api.telegram.org/bot1213907579:AAGQkqsS5DGb3CCgeCjPCGGR-nPnpK69jRw/'
#IMPORTANT
# do not use '/' in the end of line - this is not page but FILE!

#Сейчас борюсь с тем чтобы при отказе прокси можно было выбрать следующий
#предполагаю что нужно использовать сессии вместо однократных запросов иначе меня прокси банят

proxy_dict ={
        '183.89.163.237': 8080,
        '134.35.217.232': 8080,
        '180.242.75.124': 8080,
        '36.69.2.160': 8080,
        '192.41.71.221': 3128,
        '172.104.24.182': 3128,
}

def proxy_set(addr,port):
    global proxies
    http_proxy = 'http://' + addr + ':' + str (port)
    https_proxy = 'https://' + addr + ':' + str (port)

    proxies = {
        'http': http_proxy,
        'https': https_proxy,
    }

def proxy_list_print ():
    for ip in proxy_dict:
        print ('Address and port is ' + ip + ':' + str(proxy_dict[ip]))


def proxy_choose ():
    global proxies
    proxy_check_url = 'https://httpbin.org/ip'
    for ip in proxy_dict:
        proxies = {'http:': ip + ':'+str(proxy_dict[ip])}
        print(proxies)
        try:
            response = requests.get(proxy_check_url,proxies=proxies)
            print(response.json())
            proxy_set(ip, proxy_dict[ip])
            print ('I will use a ' + str(proxies))
            break
        except:
            print("Skipping. Connnection error")
    return(proxies)

def get_updates_json(request):
    url_updates = url + 'getUpdates'
    proxy_choose()
#    print ('Will try to get updates for BOt...')
#    print ('Main link is ____________________ ' + url)
#    print ('Triyng to get request from page...' + '\n' + url_updates)
#    print ('The answer is: ' + request.get(url)['ok'])
    try:
        response = requests.get(request + 'getUpdates', proxies = proxies)
        print ('Response is recieved!!!')
    except requests.exceptions.ProxyError as pr_err:
        print ('Proxy is anavailable', pr_err)  # 
        return
    else:
        return response.json()

def last_update (data):
    results = data['result']
    total_updates = len(results)-1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    print('Chat ID is ' + str(chat_id))
    return chat_id

def send_sms (chat, text):
    print ('Send to dialogue' + text)    
    params = {'chat_id': chat, 'text': text}
    response = requests.post (url + 'sendMessage', proxies =proxies, data = params)
    return (response) 
    
def main():
#    proxy_choose()
#    print (proxies)
#    print (get_updates_json(url))
#    sleep(2)
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            sms_text = last_update(get_updates_json(url))['message']['text'] #определяем текст входящего сообщения
            print ('Here is inbound message: ' + sms_text)
            send_sms(get_chat_id(last_update(get_updates_json(url))), sms_text) #отправляем его обратно адресату
            update_id +=1
            print (str(update_id))
        sleep(10)


if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        print ('Program shutdown...')
        exit()