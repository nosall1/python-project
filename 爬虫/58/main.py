#-*- coding:utf-8 -*-
from multiprocessing.pool import Pool

from channel_extract import get_channel_urls
from page_parsing import get_links_from
from channel_extract import channel_list
def get_all_links_from(channel):
    for num in range(1,101):
        get_links_from(channel,num)

pool=Pool()
pool.map(get_all_links_from,channel_list.split())