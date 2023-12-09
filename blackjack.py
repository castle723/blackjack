import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = range(1, 13)
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def calculate_score(self):
        score = sum(card.rank if card.rank <= 10 else 10 for card in self.hand)
        num_aces = sum(1 for card in self.hand if card.rank == 1)
        while num_aces > 0 and score + 10 <= 21:
            score += 10
            num_aces -= 1
        return score

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

    def display_initial_cards(self):
        print(f"{self.player.name}'s hand: {', '.join(str(card) for card in self.player.hand)}")
        print(f"Dealer's hand: {self.dealer.hand[0]}, [Hidden]")

    def play(self):
        self.deal_initial_cards()
        self.display_initial_cards()

        # Player's turn
        while self.player.calculate_score() < 21:
            action = input("Do you want to 'Hit' or 'Stand'? ").lower()
            if action == 'hit':
                self.player.add_card(self.deck.deal())
                print(f"{self.player.name} drew {self.player.hand[-1]}")
                print(f"{self.player.name}'s hand: {', '.join(str(card) for card in self.player.hand)}")
            elif action == 'stand':
                break

        # Dealer's turn
        while self.dealer.calculate_score() < 17:
            self.dealer.add_card(self.deck.deal())

        # Display final hands
        print(f"\n{self.player.name}'s hand: {', '.join(str(card) for card in self.player.hand)}")
        print(f"Dealer's hand: {', '.join(str(card) for card in self.dealer.hand)}")

        # Determine the winner
        player_score = self.player.calculate_score()
        dealer_score = self.dealer.calculate_score()

        if player_score > 21 or (dealer_score <= 21 and dealer_score >= player_score):
            print("Dealer wins!")
        elif player_score == 21 or (dealer_score > 21 or dealer_score < player_score):
            print("Player wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    blackjack_game = BlackjackGame()
    blackjack_game.play()
