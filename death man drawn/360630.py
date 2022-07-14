from abc import abstractclassmethod
from ast import Break
from dataclasses import field
from operator import inv
import random
import turtle
from unicodedata import name
import numpy as np


# class Card:
#     id = -1
#     num = -1
#     def __init__(self, num) -> None:
#         self.num = num
#     @abstractclassmethod
#     def active_skill(self, activePlayer):
#         pass
# class Cannon(Card):
#     id = 2
#     def active_skill(self, activePlayer):
#         for player in game:
#             if(player.name != activePlayer.name):
#                 print(player.name)
#                 activePlayer.printInv()
#                 chosenName = input('Dat cai ten vao')
#                 chosenCard = input('No la bai de')
#         for player in game:
#             if(player.name == chosenName):
#                 player.inv.remove(chosenCard)
#                 discard.append(chosenCard)
# class Anchor(Card):
#     id = 0
#     def active_Anchor(self, activePlayer):
#         save = []
#         for card in field:
#             save.append(card)
#             if(card == suit[0]):
#                 self.inv.extend(save)
#                 field.clear
# class Hook(Card):
#     id = 1
#     def active_Hook(self, activePlayer):
#         activePlayer.printInv()
#         chosenCard = input('No la bai de')
#         if(chosenCard in activePlayer.inv):
#             activePlayer.remove(chosenCard)
#             field.append(chosenCard)
#             activePlayer.active_Card(chosenCard)


# class Map(Card):
#     id = 5
#     def active_Map(self, activePlayer):
#         mapArr = []
#         for i in range(3):
#             mapArr.append(random.choice(tuple(discard)))
#         print(mapArr)
#         chosenCard = input('No la bai de')
#         discard.remove(chosenCard)
#         field.append(chosenCard)
#         if(activePlayer.checkConcomitance(chosenCard)):
#             activePlayer.active_Card(chosenCard)
# class Mystic(Card):
#     id = 6
#     def active_Mystic(self, activePlayer):
#         seenCard = deck[numDeck[-1]]
#         print(seenCard)
#         n = input('1 <=> lay', '\n', 'cai khac <=> dat vao cho cu')
#         if(n == '1'):
#             field.append(seenCard)
#             deck.remove(seenCard)
#             numDeck.remove(numDeck[-1])
#             activePlayer.active_Card(seenCard)
# class Sword(Card):
#     id = 7
#     def active_Sword(self, activePlayer):
#         for player in game:
#             print(player.name, '\n', player.inv)
#         chosenName = input('Dat cai ten vao')
#         chosenCard = input('No la bai de')
#         if(chosenCard == player.inv.name):
#             for player in game:
#                 if(player.name == chosenName):
#                     player.inv.remove(chosenCard)
#                     field.append(chosenCard)
#                     if(activePlayer.checkConcomitance(chosenCard)):
#                         activePlayer.active_Card(chosenCard)
#                     else:
#                         discard.append(chosenCard)
#         else:print('not found')
# class Karaken(Card):
#     id = 9
#     def active_Karaken(self, activePlayer):
#         for i in range(2):
#             cardDrawn = deck[-1]
#             deck.remove(cardDrawn)
#             activePlayer.active_Card(cardDrawn)
# class Mermaid(Card):
#     id = 8
#     def active_Mermaid(self, activePlayer):
#         pass
# class Player:
#     save = []
#     inv = [[], [], [], [], [], [], [], [], [], []]
#     name = ''

#     def __init__(self, name):
#         self.name = name
#     def printInv(self):
#         for card in inv():
#             print(card.num,suit[card.id])
#     def checkConcomitance(self, id):
#         return id in count

#     def active_Card(self, cardDrawn):
#         if(cardDrawn.split()[1] == suit[0]):
#             self.active_Anchor()
#             return
#         if(cardDrawn.split()[1] == suit[1]):
#             self.active_Hook(self)
#             return
#         if(cardDrawn.split()[1] == suit[2]):
#             self.active_Cannon(self)
#             return
#         if(cardDrawn.split()[1] == suit[5]):
#             self.active_Map(self)
#             return
#         if(cardDrawn.split()[1] == suit[6]):
#             self.active_Mystic()
#             return
#         if(cardDrawn.split()[1] == suit[7]):
#             self.active_Sword(self)
#             return
#         if(cardDrawn.split()[1] == suit[9]):
#             self.active_Kraken()
#             return
#         if(cardDrawn.split()[1] == suit[3 and 4]):
#             self.active_KeyandChest()
#             return

#     def draw(self):
#         n = '1'
#         while n == '1':
#             n = input('1 <=> draw')
#             if(n == '1'):
#                 idCardDrawn = deck[numDeck[-1]].id
#                 print(suit[idCardDrawn])
#             if(self.checkConcomitance(idCardDrawn)):
#                 deck[numDeck[-1]].active_Skill(self)
#             deck.remove(deck[numDeck[-1]])
#             numDeck.remove(numDeck[-1])


def createDeck():
    deck = []
    discard = []
    for i in range (2,8):
        anchor = Anchor(i)
        hook = Hook(i)
        cannon = Cannon(i)
        key = Key(i)
        chest = Chest(i)
        map = Map(i)
        mystic = Mystic(i)
        sword = Sword(i)
        mermaid = Mermaid(i + 2)
        karaken = Karaken(i)
        if(i == 2):
            discard.append(anchor)
            discard.append(hook)
            discard.append(cannon)
            discard.append(key)
            discard.append(chest)
            discard.append(map)
            discard.append(mystic)
            discard.append(sword)
            discard.append(mermaid)
            discard.append(karaken)
        else:
            deck.append(anchor)
            deck.append(hook)
            deck.append(cannon)
            deck.append(key)
            deck.append(chest)
            deck.append(map)
            deck.append(mystic)
            deck.append(sword)
            deck.append(mermaid)
            deck.append(karaken)
    random.shuffle(deck)
    return deck,discard

class Player():
    id = -1
    name = ' '
    inv = [[], [], [], [], [], [], [], [], [], []]

    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def printInv(self):
        for i in range(len(inv)):
            if(len(int[i]) != 0):
                print('{suit}: {num}'.format(num=inv[i], suit=suit[i]))
    def printInfo(self):
        print('id = {id} \n name = {name} \n inv = {inv}'
            .format(id = self.id, name = self.name, inv = self.printInv))
    def addCard(self, card):
        if(card == []):
            for item in card():
                self.inv[item.id].append(item)
        else:
            self.inv[item.id].append(item)
    def draw(self):
        drawnCard = deck[-1]
        field.append(drawnCard)
        if(field.count(drawnCard) == 1):
            drawnCard.active_skill
    def stop(self):
        Player.addCard(field)
        field.clear
class Card():
    id = -1
    num = -1

    def __init__(self, num) -> None:
        self.num = num

    @abstractclassmethod
    def active_skill(self, activePlayer=Player):
        pass


class Anchor(Card):
    id = 0

    def active_skill(self, activePlayer=Player):
        save = []
        for i in range(len(field)):
            save.append(field[i])
            if(field[i].id == 0):
                activePlayer.addCard(save)
                discard.extend(field[i + 1:])
                field.clear


class Hook(Card):
    id = 1

    def active_skill(self, activePlayer = Player):
        activePlayer.printInv()
        chosenCardId = input('No id la bai de')
        chosenCardNum = input('No so la bai de')
        for card in activePlayer.inv[chosenCardId]():
            if(card.num == chosenCardNum):
                chosenCard = card
                break
        activePlayer.inv[chosenCardId].remove(chosenCard)
        field.append(chosenCard)
        


class Cannon(Card):
    id = 2

    def active_skill(self, activePlayer=Player):
        for player in game:
            if(player.name != activePlayer.name):
                print('Name: {name} \n Id: {id}'.format(
                    name=player.name, Id=Player.Id))
                activePlayer.printInv()
                chosenPlayerId = input('Dat cai is vao')
                chosenCardId = input('No id la bai de')
            game[chosenPlayerId].inv.remove(
                max(game[chosenPlayerId].inv[chosenCardId]))
class Key(Card):
    id = 3
    def active_skill(self, activePlayer = Player):
        save = []
        cardToDrawn = len(field)
        for i in range(cardToDrawn):
            if(len(discard) != 0):
                cardToAdd = random.choice(turtle(discard))
                activePlayer.addCard(cardToAdd)
                discard.remove(cardToAdd)
            else:
                break
class Chest(Card):
    id = 4
    def active_skill(self, activePlayer = Player):
        save = []
        cardToDrawn = len(field)
        for i in range(cardToDrawn):
            if(len(discard) != 0):
                cardToAdd = random.choice(turtle(discard))
                activePlayer.addCard(cardToAdd)
                discard.remove(cardToAdd)
            else:
                break
class Map(Card):
    id = 5
    def active_skill(self, activePlayer = Player):
        mapArr = []
        for i in range(3):
            card = random.choice(tuple(discard))
            mapArr.append(card)
            print('index = {index} \n name = {name}'.format(index = i, name = card.name))
        index = int(input('No index de'))
        discard.remove(mapArr[index])
        field.append(mapArr[index])
        mapArr[index].active_skill()
class Mystic(Card):
    id = 6
    def active_skill(self, activePlayer = Player):
        seenCard = deck[-1]
        print(seenCard)
        n = input('1 <=> danh \n khac <=> bo vao deck')
        if(n == '1'):
            activePlayer.draw()
class Sword(Card):
    id = 7
    def active_Sword(self, activePlayer = Player):
        for player in game():
            player.printInfo()
        id = int(input('No id de'))


game = []
deck,discard = createDeck()
field = []
suit = ['Anchor', 'Hook', 'Cannon', 'Key', 'Chest',
        'Map', 'Mystic', 'Sword', 'Mermaid', 'Karaken']
print(len(deck))
