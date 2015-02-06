import re
from bs4 import BeautifulSoup
import urllib2
import json


class ChatMessage():
    def __init__(self, string):
        self.string = string
        self.emoticons_master_list = []
        self.mentions_master_list = []
        self.links_master_list = []
        self.link_title_list = []

    def get_string_data(self):
        temp_list = []
        http_index_list = [m.start() for m in re.finditer('http://', self.string)]
        https_index_list = [m.start() for m in re.finditer('https://', self.string)]
        mention_flag = False
        emoticon_flag = False
        link_flag = False
        link = ""
        position = 0
        for c in self.string:
            last_position = position == len(self.string) - 1
            # mentions
            mention_sc = re.match('[\w]', c)
            if mention_flag and mention_sc:
                temp_list.append(c)
            if mention_flag and not mention_sc or mention_flag and last_position:
                self.mentions_master_list.append(''.join(temp_list))
                mention_flag = False
                temp_list = []
            if c == '@':
                mention_flag = True
            # emoticons
            if c == ')':
                if len(temp_list) <= 15:
                    self.emoticons_master_list.append(''.join(temp_list))
                emoticon_flag = False
                temp_list = []
            if emoticon_flag:
                temp_list.append(c)
            if c == '(':
                emoticon_flag = True
             # links
            link_sc = re.match('[/:.\w]', c)
            if position in http_index_list or position in https_index_list:
                link_flag = True
                link += c
            if link_flag:
                temp_list.append(c)
            if link_flag and c == ' ' or link_flag and last_position:
                self.links_master_list.append(''.join(temp_list))
                link_flag = False
                temp_list = []
            position +=1

    def get_link_titles(self):
        for url in self.links_master_list:
            try:
                html = urllib2.urlopen(url)
                soup = BeautifulSoup(html)
                self.link_title_list.append(soup.title.text)
            except:
                self.link_title_list.append(None)

    def get_json(self):
        self.get_string_data()
        self.get_link_titles()
        data = {}
        if self.mentions_master_list:
            data['mentions'] = [l for l in self.mentions_master_list]
        if self.emoticons_master_list:
            data['emoticons'] = [l for l in self.emoticons_master_list]
        if self.links_master_list:
            links_list = []
            for i in range(len(self.links_master_list)):
                links_list.append({'url': self.links_master_list[i], 'title': self.link_title_list[i]})
            data['links'] = links_list
        json_data = json.dumps(data)
        return json_data

cm = ChatMessage('@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016')
print cm.get_json()