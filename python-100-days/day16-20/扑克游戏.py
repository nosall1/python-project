#-*- coding:utf-8 -*-
import random
from enum import unique, Enum


# 花色
@unique
class Suite(Enum):
    SPADE,HEART,CLUB,DIAMOND=range(4)
    def __lt__(self, other):
        return self.value<other.value

# 牌
class Card():
    def __init__(self,suite,face):
        self.suite=suite
        self.face=face

    def show(self):
        suites = ['♠︎', '♥︎', '♣︎', '♦︎']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __repr__(self):
        return self.show()

# 扑克
class Poker():
    def __init__(self):
        self.index=0
        self.cards=[Card(suite,face) for suite in Suite for face in range(1,14)]

    # 洗牌
    def shuffle(self):
        random.shuffle(self.cards)

    # 发牌
    def deal(self):
        card=self.cards[self.index]
        self.index+=1
        return card

    @property
    def has_more(self):
        return self.index<len(self.cards)

# 玩家
class Player():
    def __init__(self,name):
        self.name=name
        self.cards=[]
    def get_one(self,card):
        self.cards.append(card)
    def sort(self,comp=lambda card:(card.suite,card.face)):
        self.cards.sort(key=comp)

def main():
    poker=Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
            player.get_one(poker.deal())

    for player in players:
        player.sort()
        print(player.name,end=':')
        print(player.cards)

if __name__ == '__main__':
    main()