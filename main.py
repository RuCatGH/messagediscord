import requests
import schedule

mes = str(input('Message: '))
# time = str(input('Time: '))
url = 'https://discord.com/api/v9/channels/864553556216119326/messages'

def send(url, mes):
    payload={
        'content': mes,
    }
    header = {
        "authorization": "",
    }

    r = requests.post(url, data=payload, headers=header)



if __name__ == "__main__":
    schedule.every().second.do(send, url, mes)
    while True:
        schedule.run_pending()
