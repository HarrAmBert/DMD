from abc import abstractclassmethod
import random
import turtle


def createDeck():
    deck = []
    discard = []
    for i in range(2, 8):
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
    return deck, discard


class Player():
    id = -1
    name = ' '
    inv = [[], [], [], [], [], [], [], [], [], []]

    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def printInv(self):
        for i in range(len(self.inv)):
            for j in range(len(self.inv[i])):
                print('{num} : {suit}'.format(
                    num=self.inv[i].num, suit=suit[self.inv[i].id]))

    def printInfo(self):
        print('id = {id} \n name = {name} \n inv = {inv}'
              .format(id=self.id, name=self.name, inv=self.printInv))

    def addCard(self, card):
        self.inv.extend(card)

    def draw(self):
        drawnCard = deck[-1]
        deck.remove(drawnCard)
        field.append(drawnCard)
        if(drawnCard.id not in field):
            idList.append(drawnCard.id)
            drawnCard.active_skill(activePlayer=self)
        for card in field:
            print('{num} : {suit},'.format(
                num=card.num, suit=suit[card.id]), end=' ')
        print('\n')
            

        
    def stop(self):
        discard.extend(field)
        random.shuffle(discard)
        field.clear
        idList.clear()

    def collect(self):
        haveKey = False
        haveChest = False
        for card in field:
            if(card.id == 4):
                haveChest = True
                continue
            if(card.id == 3):
                haveKey = True
                continue
        if(haveChest and haveKey):
            save = []
            cardToDrawn = len(field)
            for i in range(cardToDrawn):
                if(len(discard) != 0):
                    cardToAdd = random.choice(turtle(discard))
                    save.append(cardToAdd)
                    discard.remove(cardToAdd)
                else:
                    break
            self.addCard(save)
        self.addCard(field)
        field.clear()
        idList.clear()

    def getCardMax(self, id):
        cardMaxIndex = -1
        max = 0
        for i in range((self.inv[id])):
            if(self.inv[id][i].num > max):
                max = self.inv[id][i].num
                cardMaxIndex = i
        return self.inv[id][cardMaxIndex]


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

    def active_skill(self, activePlayer=Player):
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
                    name=player.name, Id=Player.id))
                activePlayer.printInv()
                chosenPlayerId = input('Dat cai id vao')
                chosenCardId = input('No id la bai de')
                chosenCard = game[chosenPlayerId].getCardMax(chosenCardId)
                game[chosenPlayerId].inv.remove(chosenCard)

class Key(Card):
    id = 3

    def active_skill(self, activePlayer=Player):
        pass
        # save = []
        # cardToDrawn = len(field)
        # for i in range(cardToDrawn):
        #     if(len(discard) != 0):
        #         cardToAdd = random.choice(turtle(discard))
        #         activePlayer.addCard(cardToAdd)
        #         discard.remove(cardToAdd)
        #     else:
        #         break


class Chest(Card):
    id = 4

    def active_skill(self, activePlayer=Player):
        pass
        # save = []
        # cardToDrawn = len(field)
        # for i in range(cardToDrawn):
        #     if(len(discard) != 0):
        #         cardToAdd = random.choice(turtle(discard))
        #         activePlayer.addCard(cardToAdd)
        #         discard.remove(cardToAdd)
        #     else:
        #         break


class Map(Card):
    id = 5

    def active_skill(self, activePlayer=Player):
        mapArr = []
        for i in range(3):
            card = random.choice(tuple(discard))
            mapArr.append(card)
            print('index = {index} \n name = {name}'.format(
                index=i, name=card.name))
        index = int(input('No index de'))
        discard.remove(mapArr[index])
        field.append(mapArr[index])
        mapArr[index].active_skill()


class Mystic(Card):
    id = 6

    def active_skill(self, activePlayer=Player):
        seenCard = deck[-1]
        print('{num} : {suit}'
              .format(num=seenCard.num, suit=suit[seenCard.id]))
        n = input('1 <=> danh \n khac <=> bo vao deck')
        if(n == '1'):
            activePlayer.draw()


class Sword(Card):
    id = 7

    def active_Sword(self, activePlayer=Player):
        for player in game():
            player.printInfo()
        isIdentical = True
        idPlayer = int(input('No id player de'))
        idCard = int(input('No id card de'))
        while(isIdentical):
            if(len(activePlayer.inv[idCard]) != 0):
                isIdentical = False
            else:
                print('Chon bai ko trung de')
        chosenCard = game[idPlayer].getCardMax(idCard)
        game[idPlayer].inv.remove(chosenCard)
        field.append(chosenCard)
        if(field.count(chosenCard) == 1):
            chosenCard.active_skill
        else:
            activePlayer.stop()


class Karaken(Card):
    id = 9

    def active_skill(self, activePlayer=Player):
        for i in range(2):
            cardDrawn = deck[-1]
            deck.remove(cardDrawn)
            field.append(cardDrawn)
            if(field.count(cardDrawn) == 1):
                cardDrawn.active_skill
            else:
                activePlayer.stop()


class Mermaid(Card):
    id = 8

    def active_Mermaid(self, activePlayer):
        pass

turn = 0
idList = []
game = []
deck, discard = createDeck()
field = []
suit = ['Anchor', 'Hook', 'Cannon', 'Key', 'Chest',
        'Map', 'Mystic', 'Sword', 'Mermaid', 'Karaken']
n = int(input('Nhap so nguoi choi \n'))
for i in range(n):
    player = Player(input('Nhap ten nguoi choi \n'), i)
    game.append(player)
while(len(deck)):
    inTurn = True
    playerTurn = game[turn % len(game)]
    print(playerTurn.name, 'turn')
    while(inTurn):
        option = input('1 <=> drawn \n cai khac <=> collect \n')
        if(option == '1'):
            playerTurn.draw()
        else:
            playerTurn.collect()
            break
    turn += 1
