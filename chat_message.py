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
        http_index_list = [m.start() for m in re.finditer('http://', self.string)]
        https_index_list = [m.start() for m in re.finditer('https://', self.string)]
        temp_lists = [[], [], []]
        emoticon_stack = []
        mention_flag = False
        link_flag = False
        position = 0
        last_index = len(self.string) - 1
        for c in self.string:
            last_position = position == last_index
            # mentions
            mention_sc = re.match('[\w]', c)
            if mention_flag and mention_sc:
                temp_lists[0].append(c)
            if mention_flag and not mention_sc or mention_flag and last_position:
                self.mentions_master_list.append(''.join(temp_lists[0]))
                mention_flag = False
                temp_lists[0] = []
            if c == '@':
                mention_flag = True
             # links
            link_sc = re.match('[/:.\w]', c)
            if position in http_index_list or position in https_index_list:
                link_flag = True
            if link_flag and link_sc:
                temp_lists[1].append(c)
            if link_flag and not link_sc or link_flag and last_position:
                self.links_master_list.append(''.join( temp_lists[1]))
                link_flag = False
                temp_lists[1] = []
            # emoticons
            if c == ')' and len(emoticon_stack):
                emoticon_stack.pop()
                self.emoticons_master_list.append(''.join(temp_lists[2]))
                temp_lists[2]
            if len(emoticon_stack):
                temp_lists[2].append(c)
            if c == '(':
                emoticon_stack.append('(')
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