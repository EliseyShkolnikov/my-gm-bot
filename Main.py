import random
import threading
import time
import datetime

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
night = ['СпОкОйНоЙ ночи', 'Спок ноче', 'Спок ночи']
vk = vk_api.VkApi(token="5e0bf94cc1f1c8d17eb719e552d5a64ccd2ef2a9c64346734b72f6da075578540d9f28ab8df78e3cba975")


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})
while True:
    print(datetime.datetime.today().strftime("%H:%M"))
    time.sleep(1)
    if datetime.datetime.today().strftime("%H:%M") == "13:30":
        write_msg('394801599', night[random.randint(0, 2)])
        write_msg('394801599', night[random.randint(0, 2)])
        write_msg('394801599', night[random.randint(0, 2)])
        #  write_msg('188967783', 'Спок ноче')
        time.sleep(65)
    else:
         pass

    time.sleep(1)
 




