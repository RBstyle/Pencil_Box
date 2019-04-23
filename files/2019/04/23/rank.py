'''Есть следующая далее структура классов. Надо при помощи класса Deck получить 7
карт и определить лучшую комбинацию, которая выпала.

Определитель лучшей комбинации оформить все как функцию, которая принимает
список карт и выдает результат типа CombType.

'''

class Rank(object):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def elements(self):
        """Returns list of all elements of enum Rank"""
        return [x for x in range(2, 15)]

class Suit(object):
    SPADES = 'spades'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'
    CLUBS = 'clubs'

    def elements(self):
        """Returns list of all elements of enum Suit"""
        return [x for x in range(1, 5)]

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        rank = self.rank
        if self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        elif self.rank == 14:
            rank = 'Ace'
        return '%r of %r' % (rank, self.suit)

from random import randint
class Deck(object):
    '''Класс колоды с возможностью вытягивать карты'''
    def __init__(self, cards_count = 52):
        self.deck = []
        self.cards_count = cards_count
        for i in range(1, cards_count + 1):
            self.deck.append(i)

    def pop_card(self):
        """Returns Card object taken randomly from a Deck"""
        card_no = randint(1, self.cards_count)
        card = self.deck.pop(card_no - 1)
        self.cards_count -= 1
        rank = card % 13 + 2
        suit = int((card - 1) / 13 + 1) #поправил вывод целого
        if suit == 1:
            suit = Suit.SPADES
        elif suit == 2:
            suit = Suit.HEARTS
        elif suit == 3:
            suit = Suit.DIAMONDS
        elif suit == 4:
            suit = Suit.CLUBS
        else:
            print ('Suit is not as expected')
        return Card(rank, suit)

class CombType(object):
    '''Комбинации карт, которые доступны для определения'''
    HIGH_CARD = 1 # старшая карта
    PAIR = 2 # пара
    TWO_PAIR = 3 # две пары
    THREE_OF_KIND = 4 # тройка
    STRAIGHT = 5 # пять последовательных по рангу карт
    FLUSH = 6 # пять карт одной масти
    FULL_HOUSE = 7 # три карты одного ранга и две другого
    FOUR_OF_KIND = 8 # четыре карты одного ранга
    STRAIGHT_FLUSH = 9 # пять последовательных карт одной масти

def main():
    game_deck = Deck()
    set_of_cards = []
    for x in range(7):
        set_of_cards.append(game_deck.pop_card())
    print ('Cards on hand: %s' % set_of_cards)

    



if __name__ == "__main__":
    main()
