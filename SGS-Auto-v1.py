"""
    __________   ___     ____    ___  __________  ___    ___  __________  __________   ___   ___  ___      ___
   / _______//  / ||    /   ||  / // / _______// / //   / // / _____  // / _______//  / //  / // / ||     / //
  / //_______  /  ||   / /| || / // / // ____   / //   / // / //   / // / //_______  / //__/ // /  ||    / //
 /_______  // / ` ||  / //| ||/ // / // /_  // / //   / // / //   / // /_______  // / ____  // / ` ||   /_//
 _______/ // / /| || / // | |/ // / //___/ // / //___/ // / //___/ //  _______/ // / //  / // / /| ||  ___
/________// /_//|_||/_//  |___// /________// /________// /________//  /________// /_//  /_// /_//| || /_//
                                SanGuoSha Coding by Saba Tazayoni               /||______________| ||
                    Started: 21/07/2020                                        /___________________||
Current Version: 08/10/2020
Version 1.01

Changelog
 + 06/10/2020 (v0);
 - Basic card-game completed

 + 07/10/2020 (v1.00);
 - Starting a new wave of documentation
 - Version 1.xx will be specifically for playing with the cards, no roles or characters until Version 3.00!
 - Version 1.xx will also largely be based on RANDOMIZATION - all cards will be played/discarded at random, rather than selected
 - New Card-class implemented (removed names of horses for simplicity)
 - New Deck-class implemented (removed strings and redundant methods)
 - New Hand-class implemented (removed strings and redundant methods; draw/discard methods to become "Player-bound")
 - New Player-class started... This might take a while! :D
 - Equipped items now all in one composite list (rather than four separate lists)

 + 08/10/2020 (v1.01);
 - Card Selection done by card objects rather than indexing...
 - Generation of Players now done by input (eg. players = generate_players(num)) <-- Needs modification when adding roles/characters
 - Ported some basic in-game checks (eg. range; which is no longer a Player-bound method)
 - Ported simplified game-phase cycles
 - Ported refined armor (Black Shield & Eight-Trigrams) and weapon checks (Black Pommel & Zhuge Crossbow)
 - Streamlining and creating a uniform naming for any variables called x_index or y_player_index
"""
import random


players = generate_players(6)


# --- Game-Setup
def generate_players(num=10):
    # Num refers to the number of players you want to generate
    players = [Player for player_number in range(num)]
    return players


# --- Loose Functions
def calculate_targets_in_physical_range(self, source_index, modifier=0):
    # 'Source_index' refers to which player the range is being calculated from
    # 'Modifier' refers to any bonuses granted/penalized by abilities/equipment
    output = []
    for item in self.equipment:
        if item.type == "-1 Horse":
            modifier += 1
            break

    for (target_index, target) in enumerate(players):
        if target_index != source_index:
            distance = abs(target_index - source_index)
            target_modifier = 0

            for item in target.equipment:
                if item.type == "+1 Horse":
                    target_modifier += 1
                    break

            if distance > len(players) / 2:
                distance = len(players) - distance
            if distance - (1 + modifier) + (target_modifier) <= 0:
                output.append(target_index)
    return output


def calculate_targets_in_weapon_range(self, source_index, modifier=0, omit=None):
    # 'Source_index' refers to which player the range is being calculated from
    # 'Modifier' refers to any bonuses granted/penalized by abilities/equipment
    # 'Omit' refers to any players that are untargetable during this calculation
    output = []
    for item in self.equipment:
        if item.type == "-1 Horse":
            modifier += 1
            break

    for (target_index, target) in enumerate(players):
        if target_index != source_index:
            distance = abs(target_index - source_index)

            target_modifier = 0
            for item in target.equipment:
                if item.type == "+1 Horse":
                    target_modifier += 1
                    break

            if distance > len(players) / 2:
                distance = len(players) - distance
            if distance - (1 + modifier + (players[source_index].weapon_range)) + (target_modifier) <= 0:
                output.append(target_index)
    if omit != None:
        output.remove(omit)
    return output


# --- A class for handling playing-cards used in-game
# 1. 'Rank' refers to the numerical value of the card, corresponding to below ('Val'), but numbered from 1 to 13 instead of letters (for ease-of-use!)
# 2. 'Val' refers to the value written on card (A, 2, 3 ... J, Q, K)
# 3. 'Suit' refers to card-suit written on card ('Spades' (\u2660), 'Clubs' (\u2663), 'Hearts' (\u2665), 'Diamonds' (\u2666))
# 4. 'CType' refers to card-type (Basic, Tool, Delay-Tool or Equipment (broken down into weapon, armor, -1 horse, +1 horse))
# 5. 'Effect' refers to the effect that the card performs;
# For more details on individual cards and their effects, check the flavour-texts within the deck! (look for all_cards)
# 5a. 'Basic cards': ATTACK (x30), DEFEND (x15), PEACH (x8)
# 5b. 'Tool cards': BARBARIANS (x3), GRANARY (x2), PEACH GARDENS (x1), RAIN OF ARROWS (x1),
#                   COERCE (x2), DISMANTLE (x6), DUEL (x3), GREED (x4), NEGATE (x4), STEAL (x5)
# 5c. 'Delay-Tool cards': ACEDIA (x3), LIGHTNING (x2)
# 5d. 'Equipment cards': WEAPON (x10), ARMOR (x3), -1 HORSE (x3), +1 HORSE (x3)
# 6. 'Flavour_text' refers to the description of what the individual card does
# 7. 'Weapon_range' refers to the range provided by the ten possible weapon-cards (within equipment cards)
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


# The deck! (108 cards total)
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
            discard_deck.add_to_top(self.remove_from_top())
            num -= 1


# A class for handling the cards in a players' hand
class Hand(Deck):
    def __init__(self, hand):
        self.contents = []
        self.contents = hand


# --- A class for individual players and their stats in the game
# 1. 'Character' is a PLACEHOLDER for future versions when character-cards are introduced!
# 2. 'Weapon_range' is defaultly set to 1, and increases by having a -1 horse or a weapon equipped; this determines who you can reach with attacks
# 3. 'Attacks_this_turn' is defaultly set to 0; players can only do 1 ATTACK per turn unless a crossbow is equipped
# 4. 'Current_health' is defaultly set to 4 (this will change in future versions); when a players' health reaches 0, they are on the BRINK OF DEATH!
# 5. 'Max_health' is defaultly set to 4 (this will change in future versions); current_health cannot exceed max_health
# 6. 'Hand' refers to the playing-cards in a players' hand
# 7. 'Equipment' refers to equipped items; only one of each type of equipment can be equipped at one time
# 8. 'Pending_judgements' refers to any Delay-Tool cards that have yet to take effect on a player. These take effect at the start of their turn
# 9. 'Acedia_active' refers to having failed the judgement (above), and this player misses their action-phase of their turn - False by default
# 10. 'Tools_immunity' refers to having had a Tool-card negated for an individual player - False by default
class Player:
    def __init__(self):
        self.character = "Placeholder"
        self.weapon_range = 1
        self.attacks_this_turn = 0
        self.current_health = 4
        self.max_health = 4
        self.hand = Hand([])
        self.equipment = []
        self.pending_judgements = []
        self.acedia_active = False
        self.tools_immunity = False

    def __str__(self):
        equips = "Equipment: "
        pending = "Pending: "
        character_details = f" BLANK // {self.current_health}/{self.max_health} HP remaining // "
        for item in self.equipment:
            if item.ctype == "Weapon":
                equips += (f"W:{item} // ")
            if item.ctype == "Armor":
                equips += (f"A:{item} // ")
            if item.ctype == "-1 Horse":
                equips += (f"H:{item} // ")
            if item.ctype == "+1 Horse":
                equips += (f"H:{item} // ")
        for item in self.pending_judgements:
            if item.effect2 == "Acedia":
                pending += "[A]"
            if item.effect2 == "Lightning":
                pending += "[L]"
            if item.effect2 == "Rations Depleted":
                pending += "[R]"
        if equips != "Equipment: " and pending != "Pending: ":
            return (character_details + equips + pending)
        elif equips != "Equipment: ":
            return (character_details + equips)
        elif pending != "Pending: ":
            return (character_details + pending)
        else:
            return (character_details)

    # Draw/Discard Methods
    def draw(self, deck_drawn=main_deck, num=1):
        while num > 0:
            if deck_drawn == main_deck:
                main_deck.check_if_empty()
            card = deck_drawn.remove_from_top()
            self.hand.add_to_top(card)
            num -= 1

    def discard(self, mode="Hand", num=1):
        if mode == "Hand":
            while num > 0:
                all_cards = self.hand.contents
                card = random.choice(all_cards)
                self.hand.contents.remove(card)
                discard_deck.add_to_top(card)
                num -= 1

        elif mode == "Handquip":
            while num > 0:
                all_cards = self.hand.contents + self.equipment
                card = random.choice(all_cards)
                if card in self.equipment:
                    self.equipment.remove(card)
                    discard_deck.add_to_top(card)
                else:
                    self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                num -= 1
        return card

    def discard_all_cards(self, death=False):
        while len(self.hand.contents) > 0:
            discard_deck.add_to_top(self.hand.contents.pop())

        while len(self.equipment) > 0:
            discard_deck.add_to_top(self.equipment.pop())
        self.weapon_range = 1

        if death:
            while len(self.pending_judgements) > 0:
                discard_deck.add_to_top(self.pending_judgements.pop())

    # In-game General Checks
    def check_break_brink_loop(self, amount_healed):
        if self.current_health + amount_healed > 0:
            return True
        else:
            return False

    def check_brink_of_death_loop(self, dying_index=0, source_index=0):
        # Regular Brink of Death Loop
        for player in players[dying_index:]:
            if players[dying_index].current_health > 0:
                break
            self.current_health += player.use_reaction_effect(
                "Brink Of Death", 1, None, dying_index, reacting_player_index)
            reacting_player_index += 1
            if reacting_player_index >= len(players):
                reacting_player_index -= len(players)
        for player in players[:dying_index]:
            if players[dying_index].current_health > 0:
                break
            self.current_health += player.use_reaction_effect(
                "Brink Of Death", 1, None, dying_index, reacting_player_index)
            reacting_player_index += 1
            if reacting_player_index >= len(players):
                reacting_player_index -= len(players)

            # If player died
            if self.current_health < 1:
                print(f"{self.character} wasn't saved from the brink of death!")
                self.discard_all_cards(death=True)
                players.pop(dying_index)
                return "Break"

            # If player survived
            else:
                print(
                    f"{players[dying_index]} has been successfully healed back to {players[dying_index].current_health}/{players[dying_index].max_health} HP.")

    def check_pending_judgements(self):
        while len(self.pending_judgements) > 0:
            print(" ")
            main_deck.check_if_empty()
            pending_judgement = self.pending_judgements.pop(0)

            # LIGHTNING
            if pending_judgement.effect2 == 'Lightning':
                print(
                    f"{self.character} must face judgement for LIGHTNING; (needs anything but TWO to NINE of \u2660 or else they suffer THREE points of lightning damage)! If no hit, LIGHTNING will pass onto the next player!")
                negated = check_negate_loop(players, pending_judgement)
                if negated:
                    move_lightning = True
                if not negated:
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    print(f"{self.character} flipped a {judgement_card}.")

                    # IF JUDGEMENT OCCURS AND HITS PLAYER!
                    if (judgement_card.suit == "\u2660") and (10 > judgement_card.rank > 1):
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} deals THREE DAMAGE, then gets discarded!")
                        discard_deck.add_to_top(pending_judgement)
                        damage_dealt = 3
                        self.current_health -= damage_dealt
                        if self.current_health < 1:
                            if self.check_brink_of_death_loop(0, "Self") == "Break":
                                return "Break"
                    else:
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} passes on to the next player!")
                        move_lightning = True

                # JUDGEMENT NEGATED OR OCCURS AND DOESN'T HIT!
                if move_lightning:

                    # IF CARD CAN POSSIBLY PASS TO OTHER PLAYERS
                    possible_players = (len(players) - 1)
                    nextp = 1
                    while possible_players > 0:
                        if len(players[nextp].pending_judgements) > 0:
                            for possible_lightning in players[nextp].pending_judgements:
                                if possible_lightning.effect2 == 'Lightning':
                                    nextp += 1
                                    possible_players -= 1
                                else:
                                    players[nextp].pending_judgements.insert(
                                        0, pending_judgement)
                                    print(
                                        f"{self.character}'s {pending_judgement} passes on to {players[nextp]}!")
                                    possible_players = 0
                                    lightning_passed = True
                                    break
                        else:
                            players[nextp].pending_judgements.insert(
                                0, pending_judgement)
                            print(
                                f"{self.character}'s {pending_judgement} passes on to {players[nextp]}!")
                            possible_players = 0
                            lightning_passed = True

                    # OTHERWISE STAYS!
                    if not lightning_passed:
                        print(
                            f"{self.character}: There is no next player; {pending_judgement} stays put!")
                        players[0].pending_judgments.insert(
                            0, pending_judgement)

            # ACEDIA
            if pending_judgement.effect2 == 'Acedia':
                if not check_negate_loop(players, pending_judgement):
                    print(
                        f"{self.character} must face judgement for ACEDIA; (needs \u2665 to pass, or else misses action-phase of turn).")
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    print(f"{self.character} flipped a {judgement_card}.")
                    if judgement_card.suit == "\u2665":
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} has no effect.")
                    else:
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and thus they miss their action-phase of this turn.")
                        self.acedia_active = True
                discard_deck.add_to_top(pending_judgement)

    def reset_once_per_turn(self):
        self.attacks_this_turn = 0
        self.acedia_active = False
        self.tools_immunity = False

    # Equipment Checks
    def armor_black_shield(self, attack_card):
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Black Shield":
                bs_index = item_index
                black_shield = True

        if black_shield:
            if attack_card.suit == "\u2660" or attack_card.suit == "\u2663":
                print(
                    f"  >> {self.character} has {self.equipment[bs_index]} equipped, and therefore CANNOT be affected by black attack cards ({attack_card} discarded as normal).")
                return True
        return False

    def armor_eight_trigrams(self):
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Eight-Trigrams":
                et_index = item_index
                eight_trigrams = True

        if eight_trigrams:
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                main_deck.check_if_empty()
                print(
                    f"  >> {self.character} chose to activate their equipped {self.equipment[et_index]} (armor); needs \u2665 or \u2666 to automatically dodge.")
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(f"{self.character} flipped a {judgement_card}.")
                if judgement_card.suit == "\u2665" or judgement_card.suit == "\u2666":
                    return (True, judgement_card)
                else:
                    return (False, None)
        return (False, None)

    def check_weapon_black_pommel(self):
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Black Pommel":
                print(
                    f"  >> {self.character} has {self.equipment[item_index]} equipped, and therefore ignores any armor when attacking.")
                return True

    def check_weapon_zhuge_crossbow(self):
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Zhuge Crossbow":
                print(
                    f"  >> {self.character} has {self.equipment[item_index]} equipped, and therefore has no limit to the amount of attacks per turn.")
                return True

    # Game-Phase
    def start_beginning_phase(self):
        print(" ")
        self.reset_once_per_turn()
        print(f"{self.character} has started their turn!")
        return self.start_judgement_phase()

    def start_judgement_phase(self):
        print(" ")
        if self.check_pending_judgements() == "Break":
            return "Break"
        elif self.acedia_active:
            return self.start_discard_phase()
        else:
            return self.start_drawing_phase()

    def start_drawing_phase(self):
        print(" ")
        cards_drawn = 2
        self.draw(main_deck, cards_drawn)
        if self.acedia_active:
            return self.start_discard_phase()
        else:
            return self.start_action_phase()

    def start_action_phase(self):
        action_phase_active = True
        while action_phase_active:
            actions = self.hand.contents + ["End Action-Phase"]
            card = random.choice(actions)
            if card != "End Action-Phase":
                card.effect2 = card.effect
                self.use_card_effect(card)
            else:
                return self.start_discard_phase()

    def start_discard_phase(self):
        print(" ")
        difference = 0
        # Discard down to your current health level
        if len(self.hand.contents) > self.current_health:
            difference = (len(self.hand.contents) - self.current_health)
            self.discard("Hand", difference)
        return self.start_end_phase()

    def start_end_phase(self):
        print(" ")


# GAME-STATE
# GAME-STATE
# GAME-STATE
main_deck = Deck(all_cards)
discard_deck = Deck([])
main_deck.shuffle()
print("The deck has been shuffled!")
for player in players:
    player.draw(main_deck, 4)
print("All players have been dealt 4 cards!")
game_started = True

while game_started:
    players[0].start_beginning_phase()
    # If alive at end of turn
    if players[0].current_health > 0:
        players.append(players.pop(0))
    else:
        # If dead at end of turn
        players.pop(0)
