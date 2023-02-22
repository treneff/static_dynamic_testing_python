import unittest
from src.card import *
from src.card_game import *


class TestCardGame(unittest.TestCase):
    def setUp(self):
        
        self.card1 = Card("hearts",10)
        self.card2 = Card("spades",5)
        self.card_game = CardGame()
        
        
        
    # @unittest.skip("delete this line to run the test")  
    def test_ace_not_in_the_deck(self):
        result = self.card_game.check_for_ace(self.card1)
        self.assertEqual(False, result)
        
    # @unittest.skip("delete this line to run the test")  
    def test_highest_card(self):
        result = self.card_game.highest_card(self.card1,self.card2)
        self.assertEqual(self.card1, result)
        
    # @unittest.skip("delete this line to run the test")  
    def test_cards_total(self):
        cards = [self.card1,self.card2]
        result = self.card_game.cards_total(cards)
        self.assertEqual(15, result)
        