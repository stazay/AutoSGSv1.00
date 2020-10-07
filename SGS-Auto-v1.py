"""
    __________   ___     ____    ___  __________  ___    ___  __________  __________   ___   ___  ___      ___
   / _______//  / ||    /   ||  / // / _______// / //   / // / _____  // / _______//  / //  / // / ||     / //
  / //_______  /  ||   / /| || / // / // ____   / //   / // / //   / // / //_______  / //__/ // /  ||    / //
 /_______  // / ` ||  / //| ||/ // / // /_  // / //   / // / //   / // /_______  // / ____  // / ` ||   /_//
 _______/ // / /| || / // | |/ // / //___/ // / //___/ // / //___/ //  _______/ // / //  / // / /| ||  ___
/________// /_//|_||/_//  |___// /________// /________// /________//  /________// /_//  /_// /_//| || /_//
                                SanGuoSha Coding by Saba Tazayoni               /||______________| ||
                    Started: 21/07/2020                                        /___________________||
Current Version: 07/10/2020 
Version 2.00

 + 06/10/2020 (v1);
 - Basic card-game completed

 + 07/10/2020 (v2.00);
 - Starting a new wave of documentation
 - Version 2.xx will be specifically for playing with the cards, no roles or characters until Version 3.00!
 - New Card-class implemented (removed names of horses for simplicity)
 - New Deck-class implemented (removed strings and redundant methods)
 - New Hand-class implemented (removed strings and redundant methods; draw/discard methods to become "Player-bound")
 - New Player-class started... This might take a while! :D
"""
import random


# A class for handling playing-cards used in-game
# 1. 'Rank' refers to the numerical value of the card, corresponding to below ('Val'), but numbered from 1 to 13 instead of letters (for ease-of-use!)
# 2. 'Val' refers to the value written on card (A, 2, 3 ... J, Q, K)
# 3. 'Suit' refers to card-suit written on card ('Spades' (\u2660), 'Clubs' (\u2663), 'Hearts' (\u2665), 'Diamonds' (\u2666))
# 4. 'CType' refers to card-type (Basic, Tool, Delay-Tool or Equipment (broken down into weapon, armor, -1 horse, +1 horse))
# 5. 'Effect' refers to the effect that the card performs;
# 5a. 'Basic cards': ATTACK (x30), DEFEND (x15), PEACH (x8)
# 5b. 'Tool cards': BARBARIANS (x3), GRANARY (x2), PEACH GARDENS (x1), RAIN OF ARROWS (x1),
#                   COERCE (x2), DISMANTLE (x6), DUEL (x3), GREED (x4), NEGATE (x4), STEAL (x5)
# 5c. 'Delay-Tool cards': ACEDIA (x3), LIGHTNING (x2)
# 5d. 'Equipment cards': WEAPON (x10), ARMOR (x3), -1 HORSE (x3), +1 HORSE (x3)
# 6. 'Flavour_Text' refers to the description of what the individual card does
# 7. 'Weapon_range' refers to the range provided by the ten possible weapon-cards (within equipment cards)
# For more details on individual cards and their effects, check the flavour-texts within the GAME-DECK!
class Card:
    def __init__(self, rank, val, suit, ctype, effect, flavour_text, weapon_range=None):
        self.rank = rank
        self.val = val
        self.suit = suit
        self.ctype = ctype
        self.effect = effect
        self.flavour_text = flavour_text
        self.weapon_range = weapon_range

    def __str__(self):
        if self.ctype == "Weapon":
            return f"[{self.effect} <:{self.weapon_range}:> - {self.val}{self.suit}]"
        else:
            return f"[{self.effect} - {self.val}{self.suit}]"

    def __repr__(self):
        if self.ctype == "Weapon":
            return f"[{self.effect} <:{self.weapon_range}:> - {self.val}{self.suit}]"
        else:
            return f"[{self.effect} - {self.val}{self.suit}]"

    def __gt__(self, other):
        return self.rank > other.rank


# THE GAME-DECK (108 cards total)
all_cards = [
    Card(1, 'A', '\u2660', 'Tool', 'Duel', 'You can target any player for a duel with this card. If the target does not play an ATTACK, they are damaged. If they do ATTACK, then you must play one in response or take damage. Whoever does not attack, takes damage.'),
    Card(1, 'A', '\u2660', 'Delay-Tool', 'Lightning', 'You can place this Delay-Tool on yourself. In your next turn, you will perform a judgement for this card; if it is between two and nine of \u2660 (inclusively), you recieve three units of lightning damage. If not, LIGHTNING passes to the next player.'),
    Card(2, '2', '\u2660', 'Weapon', 'Frost Blade',
         'When equipped, and an ATTACK hits a target, the wielder has a choice; they can either damage the target or force them to discard two cards.', 2),
    Card(2, '2', '\u2660', 'Weapon', 'Gender-Swords',
         'When equipped, and playing an ATTACK on the target, the wielder can force the target to make a choice; to either discard a hand-card or allow the wielder to draw one from the deck.', 2),
    Card(2, '2', '\u2660', 'Armor', 'Eight-Trigrams',
         'When equipped: whenever a DEFEND is needed, the wearer can perform a judgement. If it is red, the DEFEND is considered to be played.'),
    Card(3, '3', '\u2660', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(3, '3', '\u2660', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(4, '4', '\u2660', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(4, '4', '\u2660', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(5, '5', '\u2660', '+1 Horse', '+1 Horse',
         'When equipped, this horse places you further away from players in distance calculations by +1.'),
    Card(5, '5', '\u2660', 'Weapon', 'Green Dragon Halberd',
         "When equipped, and the target of the wielder's ATTACK is DEFENDED against, the wielder may ATTACK again.", 3),
    Card(6, '6', '\u2660', 'Delay-Tool', 'Acedia',
         'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not \u2665, they forfeit their action-phase.'),
    Card(6, '6', '\u2660', 'Weapon', 'Black Pommel',
         'When equipped, the wielder ignores any armor of their targets.', 2),
    Card(7, '7', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(7, '7', '\u2660', 'Tool', 'Barbarians',
         'All other players must play an ATTACK or else suffer one damage.'),
    Card(8, '8', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(8, '8', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, '9', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, '9', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'J', '\u2660', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(11, 'J', '\u2660', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(12, 'Q', '\u2660', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(12, 'Q', '\u2660', 'Weapon', 'Serpent Spear',
         'When equipped, the wielder can discard any two cards to behave as an ATTACK.', 3),
    Card(13, 'K', '\u2660', 'Tool', 'Barbarians',
         'All other players must play an ATTACK or else suffer one damage.'),
    Card(13, 'K', '\u2660', '-1 Horse', '-1 Horse',
         'When equipped, this horse places other players closer to you in distance calculations by -1.'),
    Card(1, 'A', '\u2665', 'Tool', 'Peach Gardens',
         'All damaged players will be healed by one health.'),
    Card(1, 'A', '\u2665', 'Tool', 'Rain of Arrows',
         'All other players must play a DEFEND or else suffer one damage.'),
    Card(2, '2', '\u2665', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(2, '2', '\u2665', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(3, '3', '\u2665', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(3, '3', '\u2665', 'Tool', 'Granary',
         'You can use this card to flip over one card for every living player. Then, starting with the user of this card, each player will select a card and add it to their hand.'),
    Card(4, '4', '\u2665', 'Basic', 'Peach', 'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(4, '4', '\u2665', 'Tool', 'Granary',
         'You can use this card to flip over one card for every living player. Then, starting with the user of this card, each player will select a card and add it to their hand.'),
    Card(5, '5', '\u2665', '-1 Horse', '-1 Horse',
         'When equipped, this horse places other players closer to you in distance calculations by -1.'),
    Card(5, '5', '\u2665', 'Weapon', "Huang's Longbow",
         'When equipped, if the wielder successfully damages another player with an ATTACK, they can discard any horse of the target player.', 5),
    Card(6, '6', '\u2665', 'Basic', 'Peach', 'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(6, '6', '\u2665', 'Delay-Tool', 'Acedia',
         'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not \u2665, they forfeit their action-phase.'),
    Card(7, '7', '\u2665', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(7, '7', '\u2665', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(8, '8', '\u2665', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(8, '8', '\u2665', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(9, '9', '\u2665', 'Basic', 'Peach', 'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(9, '9', '\u2665', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(10, '10', '\u2665', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2665', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'J', '\u2665', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'J', '\u2665', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(12, 'Q', '\u2665', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(12, 'Q', '\u2665', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(12, 'Q', '\u2665', 'Delay-Tool', 'Lightning',
         'You can place this Delay-Tool on yourself. In your next turn, you will perform a judgement for this card; if it is between two and nine of \u2660 (inclusively), you recieve three units of lightning damage. If not, the Lightning passes to the next player.'),
    Card(13, 'K', '\u2665', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(13, 'K', '\u2665', '+1 Horse', '+1 Horse',
         'When equipped, this horse places you further away from players in distance calculations by +1.'),
    Card(1, 'A', '\u2663', 'Tool', 'Duel', 'You can target any player for a duel with this card. If the target does not play an ATTACK, they are damaged. If they do ATTACK, then you must play one in response or take damage. Whoever does not attack, takes damage.'),
    Card(1, 'A', '\u2663', 'Weapon', 'Zhuge Crossbow',
         'When equipped, the wielder has no limit to the number of ATTACKs they can play in their turn.', 1),
    Card(2, '2', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(2, '2', '\u2663', 'Armor', 'Black Shield',
         'When equipped, black ATTACK cards cannot affect the wearer.'),
    Card(2, '2', '\u2663', 'Armor', 'Eight-Trigrams',
         'When equipped: whenever a DEFEND is needed, the wearer can perform a judgement. If it is red, the DEFEND is considered to be played.'),
    Card(3, '3', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(3, '3', '\u2663', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(4, '4', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(4, '4', '\u2663', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(5, '5', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(5, '5', '\u2663', '+1 Horse', '+1 Horse',
         'When equipped, this horse places you further away from players in distance calculations by +1.'),
    Card(6, '6', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(6, '6', '\u2663', 'Delay-Tool', 'Acedia',
         'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not \u2665, they forfeit their action-phase.'),
    Card(7, '7', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(7, '7', '\u2663', 'Tool', 'Barbarians',
         'All other players must play an ATTACK or else suffer one damage.'),
    Card(8, '8', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(8, '8', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, '9', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, '9', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'J', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'J', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(12, 'Q', '\u2663', 'Tool', 'Coerce', 'Use this card to target any other player that possesses a weapon. Afterwards, you can then select any target within their attacking range. Your target can then ATTACK the victim. If they do not, you will take their weapon and add it to your hand.'),
    Card(12, 'Q', '\u2663', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(13, 'K', '\u2663', 'Tool', 'Coerce', 'Use this card to target any other player that possesses a weapon. Afterwards, you can then select any target within their attacking range. Your target can then ATTACK the victim. If they do not, you will take their weapon and add it to your hand.'),
    Card(13, 'K', '\u2663', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(1, 'A', '\u2666', 'Tool', 'Duel', 'You can target any player for a duel with this card. If the target does not play an ATTACK, they are damaged. If they do ATTACK, then you must play one in response or take damage. Whoever does not attack, takes damage.'),
    Card(1, 'A', '\u2666', 'Weapon', 'Zhuge Crossbow',
         'When equipped, the wielder has no limit to the number of ATTACKs they can play in their turn.', 1),
    Card(2, '2', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(2, '2', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(3, '3', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(3, '3', '\u2666', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(4, '4', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(4, '4', '\u2666', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(5, '5', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(5, '5', '\u2666', 'Weapon', 'Axe',
         'When equipped, and the target of the wielder DEFENDs against the ATTACK of the wielder, they can discard two cards to force the damage.', 3),
    Card(6, '6', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(6, '6', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(7, '7', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(7, '7', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(8, '8', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(8, '8', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(9, '9', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, '9', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(10, '10', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(11, 'J', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(11, 'J', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(12, 'Q', '\u2666', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(12, 'Q', '\u2666', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(12, 'Q', '\u2666', 'Weapon', 'Sky Scorcher Halberd',
         'When equipped and using the last on-hand card to ATTACK, the ATTACK can target an additional two players.', 4),
    Card(13, 'K', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(13, 'K', '\u2666', '-1 Horse', '-1 Horse',
         'When equipped, this horse places other players closer to you in distance calculations by -1.')
]


# A class for handling the deck of cards in play
class Deck:
    def __init__(self, main_deck):
        self.contents = []
        self.contents = main_deck

    def list_cards(self):
        return [str(card) for card in self.contents]

    def shuffle(self):
        random.shuffle(self.contents)

    def check_if_empty(self):
        if len(main_deck.contents) <= 0:
            print(
                f"{len(discard_deck.contents)} discarded cards have been shuffled back into the main deck!")
            main_deck.contents, discard_deck.contents = discard_deck.contents, main_deck.contents
            main_deck.shuffle()

    def add_to_top(self, card):
        self.contents.insert(0, card)

    def add_to_bottom(self, card):
        self.contents.append(card)

    def remove_from_top(self):
        card = self.contents[0]
        self.contents.pop(0)
        return card

    def discard_from_deck(self, num=1):
        while num > 0:
            main_deck.check_if_empty()
            card = self.remove_from_top()
            discard_deck.contents.insert(0, card)
            num -= 1


# A class for handling the cards in a players' hand
class Hand(Deck):
    def __init__(self, hand):
        self.contents = []
        self.contents = hand


# A class for individual players and their stats in the game
# 1. Weapon_range is defaultly set to 1, and increases by having a -1 horse or a weapon equipped
# 2. Attacks_this_turn is defaultly set to 0; players can only do 1 ATTACK per turn unless a crossbow is equipped
# 3. Current_health is defaultly set to 4; this will change in future versions, when a players' health reaches 0, they are on the BRINK OF DEATH!
# 4. Max_health is defaultly set to 4; current_health cannot exceed max_health
# 5. Hand refers to the playing-cards in a players' hand
# 6-9. Equipment refers to equipped items; only one of each type of equipment can be equipped at one time
# 10. Pending_judgements refers to any Delay-Tool cards that have yet to take effect on a player. These take effect at the start of their turn
# 11. Acedia_active refers to having failed the judgement (above), and this player misses their action-phase of their turn
# 12. Tools_immunity refers to having had a tool-card negated for an individual player
class Player:
    def __init__(self):
        self.weapon_range = 1
        self.attacks_this_turn = 0
        self.current_health = 4
        self.max_health = 4
        self.hand = Hand([])
        self.equipment_weapon = []
        self.equipment_armor = []
        self.equipment_defensive_horse = []
        self.equipment_offensive_horse = []
        self.pending_judgements = []
        self.acedia_active = False
        self.tools_immunity = False


# GAME-STATE
# GAME-STATE
# GAME-STATE
main_deck = Deck(all_cards)
discard_deck = Deck([])
main_deck.shuffle()
# print("The deck has been shuffled!")
# for player in players:
#     player.hand_cards.draw(main_deck, 4, False)
# print("All players have been dealt 4 cards!")
# game_started = True

# while game_started:
#     players[0].start_beginning_phase()
#     # If alive at end of turn
#     if players[0].current_health > 0:
#         players.append(players.pop(0))
#     else:
#         # If dead at end of turn
#         players.pop(0)
