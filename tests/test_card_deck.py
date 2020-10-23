#!/usr/bin/env python3

"""
Tests for card deck logic
"""

import logging
import unittest
import unittest.mock as mock
from video_poker.card_deck import CardDeck, Suits

logger = logging.getLogger('test_card_deck')


class TestCardDeck(unittest.TestCase):

    def test_draw(self):
        """
        Test drawing a card from the deck.
        """
        my_deck = CardDeck()
        with mock.patch('random.choice', lambda x: 10):
            card = my_deck.draw()
        self.assertEqual(card, CardDeck.CARD(Suits(0), 10))

    def test_draw_all_cards(self):
        """
        Test that the draw fails when the deck is depleted.
        """
        my_deck = CardDeck()
        for i in range(CardDeck.NUM_CARDS):
            my_deck.draw()
        with self.assertRaises(RuntimeError):
            my_deck.draw()

    def test_remove_card(self):
        """
        Test that a specific card is properly removed from the deck.
        """
        my_deck = CardDeck()
        card = CardDeck.CARD(Suits(0), 10)
        my_deck.remove_card(card)
        self.assertNotIn(card, my_deck.peek_deck())

    def test_remove_card_twice(self):
        """
        Test that the draw fails when the card is not in the deck.
        """
        my_deck = CardDeck()
        card = CardDeck.CARD(Suits(0), 10)
        my_deck.remove_card(card)

        with self.assertRaises(RuntimeError):
            my_deck.remove_card(card)


if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)
    unittest.main()