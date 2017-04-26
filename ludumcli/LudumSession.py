# -*- coding: utf-8 -*-
from requests import Session
from bs4 import BeautifulSoup
from datetime import datetime


class LudumSession(object):

    def __init__(self):
        self.session = Session()
        self.base_url = 'http://ludumdare.com/compo/ludumdare/'

    def get_upcoming_ludumdares(self):
        resp = self.session.get(self.base_url)
        
        if resp.status_code != 200:
            return None

        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        
        entry_body = soup.find('div', {'class': 'entry body'})
        rows = entry_body.find_all('tr')
        
        return_data = []

        for row in rows:
            _row = {}

            first_link = row.find('a')

            if first_link is not None:
                if '#' in first_link.text:
                    _row['id'] = first_link.text.replace('#', '')

            if not 'id' in _row:
                continue

            return_data.append(_row)

            tds = row.find_all('td')

            date_td = tds[1]
            
            _row['date'] = datetime.strptime(
                    date_td.text.replace(
                        u'\xa0',
                        ' '
                        ).encode('ascii').decode('ascii')
                    ,'%b %Y'
                    )
        
        return_data.sort(key=lambda x: x['date'], reverse=True)

        return return_data
