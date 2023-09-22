import bingocard

class BingoGame():
    #_list_cards = []
    #_winning_card = None

    def __init__(self):
        self._list_winning_cards = []
        self._list_cards = []
        return
    
    def addCard(self, bingoCard:bingocard.BingoCard):
        if bingoCard not in self._list_cards:
            self._list_cards.append(bingoCard)

    def getNumberOfCards(self):
        return len(self._list_cards)
    
    def hasWinningCards(self):
        if len(self._list_winning_cards) > 0:
            return True
        return False

    def getWinningCards(self):
        return self._list_winning_cards

    def callNumber(self, number):
        for card in self._list_cards:
            card.isMatchedNumber(number)
            if card.isBingo():
                self._list_winning_cards.append(card)

    def resetWinners(self):
        if False == self.hasWinningCards():
            return
        
        for winner in self._list_winning_cards:
            self._list_cards.remove(winner)        

        self._list_winning_cards = [] # Reset

