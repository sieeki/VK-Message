import vk_api, time, colorama
from colorama import Fore
import os
import sys
from vk_api.longpoll import VkLongPoll, VkEventType

banner = """
.!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
             """"          """""""
      _____ _____ ______ ______ _  _______
     / ____|_   _|  ____|  ____| |/ /_   _|
    | (___   | | | |__  | |__  | ' /  | |
     \___ \  | | |  __| |  __| |  <   | |
     ____) |_| |_| |____| |____| . \ _| |_
    |_____/|_____|______|______|_|\_\_____|
"""

subscribe = "Подписаться на автора в Telegram? (yes/no)"

print(Fore.CYAN + banner)
print(Fore.CYAN + subscribe)
choose = input('--> ')

if choose == "yes":
    os.system("termux-open-url 'https://t.me/SieekiModding'")
    print("Если вы подписались, перезапустите скрипт и выберите no :)")

else:
    token = input("Введите токен: ")
    users = input("Введите id: ")
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    def main():
        try:
            chats = input('Кол-во бесед: ')
            spot = 0
            while int(spot) < int(chats):
                api.messages.createChat(user_ids=users, title="Sieeki Message")
                spot += 1
                time.sleep(15)
            print(spot)
        except Exception as er:
            print(er)


    main()
