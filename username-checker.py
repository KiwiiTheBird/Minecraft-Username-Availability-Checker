# 🚀 this project was made by KiwiiTheBird.
# ⚠️ Any questions or suggestions? Feel free to DM me on Discord: KiwiTheBird#1259
# 🛠 Created on 22/12 2020
# 🖥 Version: 1.0

import requests
import bs4
import time


def main():   
    main.url = 'https://namemc.com/search'

    with open('usernames.txt') as file:
        lines = file.readlines()

        for username in lines:
            payload = {'q' : username}
            response = requests.get(main.url, params=payload)

            soup = bs4.BeautifulSoup(response.content, 'lxml')
            availabilty = soup.findAll('div', class_='col-sm-6 my-1')

            for element in availabilty:
                if 'Unavailable' in element.text:
                    print('Username {} is unavailable.'.format(username[:-1] if username != lines[-1] else username))
                    break

                elif 'Available*' in element.text:
                    print('Username {} is available.'.format(username[:-1] if username != lines[-1] else username))
                    break

                elif 'Available Later*' in element.text:
                    datetime = soup.find('time',class_='text-nowrap').get('datetime')
                    datetime = time.strptime(datetime, r'%Y-%m-%dT%H:%M:%S.000Z')
                    datetime_str = '{}/{} at {}:{}:{}'.format(datetime.tm_mday, datetime.tm_mon, datetime.tm_hour, datetime.tm_min, datetime.tm_sec)
                    print('Username {} will become available at {}.'.format(username[:-1] if username != lines[-1] else username, datetime_str))
                    break


if __name__ == '__main__':
    main()
