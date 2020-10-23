#!/usr/bin/env python3

"""
Logic for a 52 card deck.
"""

import math
import collections
import logging
import random
from enum import Enum

logging.basicConfig(level=logging.DEBUG)


class Suits(Enum):
    HEART = 0
    DIAMOND = 1
    SPADE = 2
    CLUB = 3


class CardDeck(object):
    NUM_CARDS = 52
    NUM_PER_SUIT = 13
    VALID_POSITION = {"top", "random", "bottom"}

    CARD = collections.namedtuple("card", "suit num")

    def __init__(self):
        self._LOGGER = logging.getLogger("video_poker.card_deck")
        self._deck = None
        self.reset_deck()

    def reset_deck(self):
        self._deck = list(range(1, self.NUM_CARDS + 1))

    def peek_deck(self):
        """
        Get the existing deck.
        :return [CARD]:
        """
        return self._deck

    def shuffle(self):
        """

        :return:
        """
        random.shuffle(self._deck)
        self._LOGGER.info("Deck is now shuffled. You have {} cards.".format(len(self._deck)))

    def draw(self):
        """

        :return:
        """
        if len(self._deck) < 1:
            raise RuntimeError("Your deck is empty. Cannot draw more cards.")
        card = random.choice(self._deck)
        self._deck.remove(card)
        return self._get_card_from_num(card)

    def remove_card(self, card):
        """
        Remove a specific card from the deck.

        :param card:
        :return:
        """
        card_num = self._convert_card_to_num(card)
        if card_num not in self._deck:
            raise RuntimeError("That card does not exist in your deck.")
        self._deck.remove(card_num)

    @classmethod
    def _get_card_from_num(cls, card_num):
        """
        Get a card object from a card number.
        :return:
        """

        card_code = (card_num - 1)/cls.NUM_PER_SUIT
        suit = math.floor(card_code)
        card = (card_code - suit) * cls.NUM_PER_SUIT + 1

        try:
            return cls.CARD(Suits(suit), round(card))
        except ValueError:
            print("{} - {} - {}".format(card_num, card_code, suit))

    def _convert_card_to_num(self, card):
        card_num = (Suits[card.suit.name].value + (card.num / self.NUM_PER_SUIT)) * self.NUM_PER_SUIT
        return int(card_num)
