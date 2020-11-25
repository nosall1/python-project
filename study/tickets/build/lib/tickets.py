#-*- coding:utf-8 -*-

"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
from prettytable import PrettyTable
import requests
from docopt import docopt

from stations import stations
from colorama import init,Fore





'''
|预订|760000K1180A|K118|PRW|BXP|GXF|BXP|20: 09|05: 10|09: 01|N|%2FpyuLzhjciCzcXzz23FeucX8IKcdxZagNMnpyv8OPfNwPqpPTSLiTm5DAN8%3D|20170704|3|W2|21|28|0|0||||无|||无||无|无|||||10401030|1413
                 |车次|起点|终点|车站起|车站终|时间起|时间终|历时|
'''


init()
class TrainsCollection:
    header='车次 车站 时间 历时 商务 一等 二等 软卧 硬卧 硬座 无座'.split()

    def __init__(self,available_trains,options):
        """查询到的火车班次集合

        :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                 火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...
        """
        self.available_trains=available_trains
        self.options=options

    def _get_duration(self,duration):
        # duration=raw_train.get('lishi').replace(':','小时')+'分'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration

    @property
    def trains(self):
        for raw in self.available_trains:
            raw_train=str(raw).split("|")
            train_no=raw_train[3]
            initial=train_no.lower()
            # if not self.options or initial in self.options:
            train=[
                    train_no,#车次
                    '\n'.join([Fore.GREEN+self.get_key(raw_train[6])+Fore.RESET,
                               Fore.RED+self.get_key(raw_train[7])+Fore.RESET]),#出发站，到达站
                    '\n'.join([Fore.GREEN+raw_train[8]+Fore.RESET,
                               Fore.RED+raw_train[9]+Fore.RESET]),#出发时间，到达时间
                    self._get_duration(raw_train[10]),#历时
                    raw_train[-4],#商务
                    raw_train[-5],#一等
                    raw_train[-6],#二等
                    raw_train[-13],#软卧
                    raw_train[-8],#硬卧
                    raw_train[-7],#硬座
                    raw_train[-10]#无座
                ]
            yield train

    def pretty_print(self):
        pt=PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)

        #根据value获取key
    def get_key(self,value):
        for key,values in stations.items():
            if values==value:
                return key


def cli():
    '''command-line interface'''
    arguments=docopt(__doc__)
    from_station=stations.get(arguments['<from>'])
    to_station=stations.get(arguments['<to>'])
    date=arguments['<date>']

    #构建url
    url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date,from_station,to_station
    )
    options=''.join([key for key,value in arguments.items() if value is True])
    #添加verify=False参数不验证证书
    r=requests.get(url,verify=False)
    available_trains=r.json()['data']['result']
    TrainsCollection(available_trains,options).pretty_print()



if __name__ == '__main__':
    cli()


