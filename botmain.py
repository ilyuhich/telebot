import requests
from time import sleep

url = "https://api.telegram.org/bot1213907579:AAE6CL5YvyfWlFTMzKjNloFozBl665KHt-k/"

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update (data):
    results = data['result']
    total_updates = len(results)-1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_sms (chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post (url + 'sendMessage', data = params)
    return (response)


#print (url)
#print ()
#chatid = get_chat_id(last_update(get_updates_json(url)))
#print ('Here is Bot URL:  ' + url)
#print ('Here is response: ' + str(get_updates_json(url)))
#print ('Here is chat ID:  ' + str(get_chat_id(last_update(get_updates_json(url)))))
#print (last_update(get_updates_json(url)))
#send_mess(chatid,'sms-ka test') #новый комментарий 
#one more

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            #send_sms(get_chat_id(last_update(get_updates_json(url))), 'test') - отправка сообщения test
            sms_text = last_update(get_updates_json(url))['message']['text'] #определяем текст входящего сообщения
            #print = ('Here is inbound message: ' + sms_text)
            send_sms(get_chat_id(last_update(get_updates_json(url))), sms_text) #отправляем его обратно адресату
            update_id +=1
            #print (update_id)
        sleep(1)

if __name__ == '__main__':  
    try:
        main()
        #print (str(last_update(get_updates_json(url))))
        #print (str(last_update(get_updates_json(url)['text'])))
    except KeyboardInterrupt:
        print ('Program shutdown...')
        exit()
