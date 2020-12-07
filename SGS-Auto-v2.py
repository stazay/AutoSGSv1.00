"""
    __________   ___     ____    ___  _________   ___    ___  __________  __________   ___   ___  ___      ___
   / _______//  / ||    /   ||  / // / ______//  / //   / // / _____  // / _______//  / //  / // / ||     / //
  / //_______  /  ||   / /| || / // / // ____   / //   / // / //   / // / //_______  / //__/ // /  ||    / //
 /_______  // / ` ||  / //| ||/ // / // /_  // / //   / // / //   / // /_______  // / ____  // / ` ||   /_//
 _______/ // / /| || / // | |/ // / //___/ // / //___/ // / //___/ //  _______/ // / //  / // / /| ||  ___
/________// /_//|_||/_//  |___// /________// /________// /________//  /________// /_//  /_// /_//| || /_//
                                SanGuoSha Coding by Saba Tazayoni               /||______________| ||
                    Started: 21/07/2020                                        /___________________||
Current Version: 07/12/2020
Version 2.09

 + 07/12/2020 (v2.09);
 - Code cleanup for Axe

 TO DO:
 - Test individual abilities~
 - Ability to play vs CPU (random moves)
 - Ability to connect and play vs other players
"""
import random


# --- Game-Setup
def generate_character_cards():
    all_emperors = [
        Character("Liu Bei", "Shu", 4, "Male",
                  ["Benevolence", "Rouse (Ruler Ability)"]),
        Character("Cao Cao", "Wei", 4, "Male",
                  ["Evil Hero", "Escort (Ruler Ability)"]),
        Character("Sun Quan", "Wu", 4, "Male",
                  ["Reconsider", "Rescued (Ruler Ability)"]),
        Character("Yuan Shao", "Heroes", 4, "Male",
                  ["Random Strike", "Bloodline (Ruler Ability)"])
    ]

    shu_characters = [
        Character("Guan Yu", "Shu", 4, "Male",
                  ["Horsemanship", "Warrior Saint"]),
        Character("Huang Yue Ying", "Shu", 3, "Female",
                  ["Wisdom", "Talent"]),
        Character("Huang Zhong", "Shu", 4, "Male",
                  ["Fearsome Archer"]),
        Character("Ma Chao", "Shu", 4, "Male",
                  ["Horsemanship", "Iron Cavalry"]),
        Character("Zhang Fei", "Shu", 4, "Male",
                  ["Berserk"]),
        Character("Zhao Yun", "Shu", 4, "Male",
                  ["Dragon Heart"]),
        Character("Zhuge Liang", "Shu", 3, "Male",
                  ["Astrology", "Empty City"])
    ]

    wei_characters = [
        Character("Dian Wei", "Wei", 4, "Male",
                  ["Ferocious Assault"]),
        Character("Guo Jia", "Wei", 3, "Male",
                  ["Envy of Heaven",
                   "Bequeathed Strategy"]),
        Character("Sima Yi", "Wei", 3, "Male",
                  ["Retaliation", "Devil"]),
        Character("Xiahou Dun", "Wei", 4, "Male",
                  ["Eye for an Eye"]),
        Character("Xu Chu", "Wei", 4, "Male",
                  ["Bare the Chest"]),
        Character("Zhang Liao", "Wei", 4, "Male",
                  ["Raid"]),
        Character("Zhen Ji", "Wei", 3, "Female",
                  ["Impetus", "Goddess Luo"]),
    ]

    wu_characters = [
        Character("Da Qiao", "Wu", 3, "Female",
                  ["National Colours", "Displacement"]),
        Character("Gan Ning", "Wu", 4, "Male",
                  ["Surprise"]),
        Character("Huang Gai", "Wu", 4, "Male",
                  ["Trojan Flesh"]),
        Character("Lu Meng", "Wu", 4, "Male",
                  ["Restraint"]),
        Character("Lu Xun", "Wu", 3, "Male",
                  ["Humility", "One After Another"]),
        Character("Sun Shang Xiang", "Wu", 3, "Female",
                  ["Marriage", "Warrior Woman"]),
        Character("Zhou Yu", "Wu", 3, "Male",
                  ["Dashing Hero", "Sow Dissension"])
    ]

    hero_characters = [
        Character("Diao Chan", "Heroes", 3, "Female",
                  ["Seed of Animosity", "Eclipse the Moon"]),
        Character("Hua Tuo", "Heroes", 3, "Male",
                  ["First Aid", "Green Salve"]),
        Character("Hua Xiong", "Heroes", 6, "Male",
                  ["Reckless"]),
        Character("Lu Bu", "Heroes", 4, "Male",
                  ["Without Equal"]),
        Character("Pang De", "Heroes", 4, "Male",
                  ["Horsemanship", "Fearsome Advance"]),
        Character("Yan Liang & Wen Chou", "Heroes", 4, "Male",
                  ["Dual Heroes"]),
        Character("Yuan Shu", "Heroes", 4, "Male",
                  ["Mediocrity", "False Ruler"])
    ]

    all_characters = shu_characters + wei_characters + wu_characters + hero_characters

    return (all_emperors, all_characters)


def generate_deck():
    # The deck! (108 cards total)
    global main_deck
    global serp_spear
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
    serp_spear = all_cards[25]
    main_deck = Deck(all_cards)
    return main_deck


def generate_roles(num):
    # 'num' refers to the number of players you want to generate
    if num == 3:
        roles_dict = {"Emperor": 1, "Advisor": 0, "Rebel": 1, "Spy": 1}
    elif num == 4:
        roles_dict = {"Emperor": 1, "Advisor": 1, "Rebel": 1, "Spy": 1}
    elif num == 5:
        roles_dict = {"Emperor": 1, "Advisor": 1, "Rebel": 2, "Spy": 1}
    elif num == 6:
        if roles == 1:
            roles_dict = {"Emperor": 1, "Advisor": 1, "Rebel": 3, "Spy": 1}
        elif roles == 2:
            roles_dict = {"Emperor": 1, "Advisor": 1, "Rebel": 2, "Spy": 2}
    elif num == 7:
        roles_dict = {"Emperor": 1, "Advisor": 2, "Rebel": 3, "Spy": 1}
    elif num == 8:
        if roles == 1:
            roles_dict = {"Emperor": 1, "Advisor": 2, "Rebel": 4, "Spy": 1}
        elif roles == 2:
            roles_dict = {"Emperor": 1, "Advisor": 2, "Rebel": 3, "Spy": 2}
    elif num == 9:
        roles_dict = {"Emperor": 1, "Advisor": 3, "Rebel": 4, "Spy": 1}
    else:
        roles_dict = {"Emperor": 1, "Advisor": 3, "Rebel": 4, "Spy": 2}

    return roles_dict


def generate_players(num, chars):
    # 'num' refers to the number of players you want to generate
    # 'chars' refers to if character-cards are being used
    global roles_dict
    if num > 10:
        num = 10
    if 3 > num:
        num = 3

    if chars:
        (all_emperors, all_characters) = generate_character_cards()

        if roles != 0:
            roles_dict = generate_roles(num)
            roles_list = []
            for key in roles_dict.keys():
                for i in range(0, roles_dict[key]):
                    roles_list.append(key)

            random.shuffle(roles_list)
            roles_list.append(roles_list.pop(roles_list.index("Emperor")))

            players = [Player((None), roles_list.pop())
                       for player_number in range(num)]

        else:
            players = [Player() for player_number in range(num)]

        for player in players:
            if player.role == "Emperor":
                char = random.choice(all_emperors)
                all_emperors.remove(char)
            else:
                char = random.choice(all_characters)
                all_characters.remove(char)
            player.character = char.character
            player.allegiance = char.allegiance
            player.current_health = char.health
            player.max_health = char.health
            player.gender = char.gender
            player.char_abils = char.char_abils
            if (num > 4) and (player.role == "Emperor"):
                player.current_health += 1
                player.max_health += 1

    else:
        char_names = ["p0", "p1", "p2", "p3",
                      "p4", "p5", "p6", "p7", "p8", "p9"]
        genders = ["Male", "Male", "Male", "Male", "Male",
                   "Female", "Female", "Female", "Female", "Female"]
        random.shuffle(genders)

        if roles != 0:
            roles_dict = generate_roles(num)
            roles_list = []
            for key in roles_dict.keys():
                for i in range(0, roles_dict[key]):
                    roles_list.append(key)

            random.shuffle(roles_list)
            roles_list.append(roles_list.pop(roles_list.index("Emperor")))

            players = [Player(genders.pop(0), roles_list.pop())
                       for player_number in range(num)]

        else:
            players = [Player(genders.pop(0)) for player_number in range(num)]

        for player in players:
            player.character = char_names.pop(0)
            if (num > 4) and (player.role == "Emperor"):
                player.current_health += 1
                player.max_health += 1

    return players


def check_win_conditions():
    if roles_dict["Emperor"] == 1 and roles_dict["Rebel"] == 0 and roles_dict["Spy"] == 0:
        return True

    elif roles_dict["Spy"] == 1 and roles_dict["Emperor"] == 0 and roles_dict["Advisor"] == 0 and roles_dict["Rebel"] == 0:
        return True

    elif roles_dict["Emperor"] == 0:
        return True

    else:
        return False


def play_games(num_players, num_iterations, lightning_dmg=3, mode=1, chars=True):
    # 'num_players' refers to the number of players
    # 'iterations' refers to the number of iterations that the game will run
    # 'lightning_dmg' refers to the amount of damage a player takes when hit by lightning // 3 by default
    # 'mode' refers to whether there are any player roles in-game // 0 = all rebels, 1 = normal roles, 2 = more spies
    # 'chars' refers to whether character cards will be used in game // True by default
    emp_and_co_wins = 0
    spy_wins = 0
    rebel_wins = 0
    cao_cao_wins = 0
    cao_cao_loss = 0
    liu_bei_wins = 0
    liu_bei_loss = 0
    sun_quan_wins = 0
    sun_quan_loss = 0
    yuan_shao_wins = 0
    yuan_shao_loss = 0

    for i in range(num_iterations):
        global lightning_damage
        global roles
        global players
        global main_deck
        global discard_deck

        if lightning_dmg > 3:
            lightning_dmg = 3
        if lightning_dmg < 0:
            lightning_dmg = 0
        lightning_damage = lightning_dmg
        if mode > 2:
            mode = 0
        if mode < 0:
            mode = 0
        roles = mode

        players = generate_players(num_players, chars)
        players_at_start = []
        for player in players:
            players_at_start.append(player)

        main_deck = generate_deck()
        discard_deck = Deck([])
        main_deck.shuffle()

        print(
            f"----------------------------------------<Game {i}: The deck has been shuffled!>----------------------------------------")
        for player in players:
            player.draw(main_deck, 4, False)
            player.check_false_ruler()
            player.reset_once_per_turn()
        print("All players have been dealt 4 cards!")
        game_started = True
        while game_started:
            if (roles != 0) and check_win_conditions():
                game_started = False

                if roles_dict["Emperor"] == 1 and roles_dict["Rebel"] == 0 and roles_dict["Spy"] == 0:
                    emp_and_co_wins += 1
                    print(
                        "----------------------------<Emperor and Advisor(s) win!>-----------------------------")
                    for player in players_at_start:
                        if player.role == "Emperor" or player.role == "Advisor":
                            print(f"{player.role} - {player}")
                            if player.character == "Cao Cao":
                                cao_cao_wins += 1
                            elif player.character == "Liu Bei":
                                liu_bei_wins += 1
                            elif player.character == "Sun Quan":
                                sun_quan_wins += 1
                            elif player.character == "Yuan Shao":
                                yuan_shao_wins += 1

                elif roles_dict["Spy"] == 1 and roles_dict["Emperor"] == 0 and roles_dict["Advisor"] == 0 and roles_dict["Rebel"] == 0:
                    spy_wins += 1
                    print(
                        "-------------------------------------<Spy wins!>--------------------------------------")
                    for player in players:
                        if player.role == "Spy":
                            print(f"{player.role} - {player}")
                    for player in players_at_start:
                        if player.role == "Emperor":
                            if player.character == "Cao Cao":
                                cao_cao_loss += 1
                            elif player.character == "Liu Bei":
                                liu_bei_loss += 1
                            elif player.character == "Sun Quan":
                                sun_quan_loss += 1
                            elif player.character == "Yuan Shao":
                                yuan_shao_loss += 1

                elif roles_dict["Emperor"] == 0:
                    rebel_wins += 1
                    print(
                        "------------------------------------<Rebels win!>-------------------------------------")
                    for player in players_at_start:
                        if player.role == "Rebel":
                            print(f"{player.role} - {player}")
                    for player in players_at_start:
                        if player.role == "Emperor":
                            if player.character == "Cao Cao":
                                cao_cao_loss += 1
                            elif player.character == "Liu Bei":
                                liu_bei_loss += 1
                            elif player.character == "Sun Quan":
                                sun_quan_loss += 1
                            elif player.character == "Yuan Shao":
                                yuan_shao_loss += 1

                print(f"Turn number: {players[0].turn_number}!")

            elif len(players) == 1:
                game_started = False
                print(
                    "-------------------------------------<Game Over!>-------------------------------------")
                print(f"{players[0]} has won the game!!!")
                print(f"Turn number: {players[0].turn_number}!")

            else:
                players[0].start_beginning_phase()
                players[0].turn_number += 1
                # If alive at end of turn
                if players[0].current_health > 0:
                    players.append(players.pop(0))
                else:
                    # If dead at end of turn
                    players.pop(0)

    # Final win-results tally
    if roles != 0:
        print("----------------------------------------------------------------------------------------------------")
        print(f"Final win-tally:")
        print(f"{emp_and_co_wins} - Emperor and Advisor(s) won this many games")
        print(f"{spy_wins} - Spy won this many games")
        print(f"{rebel_wins} - Rebel(s) won this many games")
        print("----------------------------------------------------------------------------------------------------")
        if chars:
            if (cao_cao_wins + cao_cao_loss) > 0:
                print(
                    f"{(cao_cao_wins/(cao_cao_wins+cao_cao_loss))*100}% - Cao Cao won this percentage of games")
            if (liu_bei_wins + liu_bei_loss) > 0:
                print(
                    f"{(liu_bei_wins/(liu_bei_wins+liu_bei_loss))*100}% - Liu Bei won this percentage of games")
            if (sun_quan_wins + sun_quan_loss) > 0:
                print(
                    f"{(sun_quan_wins/(sun_quan_wins+sun_quan_loss))*100}% - Sun Quan won this percentage of games")
            if (yuan_shao_wins + yuan_shao_loss) > 0:
                print(
                    f"{(yuan_shao_wins/(yuan_shao_wins+yuan_shao_loss))*100}% - Yuan Shao won this percentage of games")


# --- Loose Functions
def get_player_index(target):
    for player_index, player in enumerate(players):
        if target == player:
            target_index = player_index
            return target_index


def check_allegiances_in_play():
    allegiances = []
    for player in players:
        allegiances.append(player.allegiance)
    return len(set(allegiances))


def check_judgement_tinkering(judgement_card, target):
    # 'judgement_card' refers to the original judgement card taking place
    # 'target' refers to the player who flipped the judgement
    target_index = get_player_index(target)
    for player in players[target_index:]:
        judgement_card = player.check_devil(judgement_card)
    for player in players[:target_index]:
        judgement_card = player.check_devil(judgement_card)
    return judgement_card


def check_negate_loop(given_list, card, source, reacting, og_card=None):
    # 'given_list' refers to the list of players included in the negate-loop (for purposes of where it starts from)
    # 'card' refers to the card played, being potentially negated
    # 'source' refers to the player of the card played
    # 'reacting' refers to the player reacting in this negate-loop
    # 'OG_card' refers to the FIRST card played (so Card can become negates being negated, this is the original card)
    x = 1 - len(players)
    given_list = given_list[(0 + x):] + given_list[:(0 + x)]
    for player_index, player in enumerate(given_list):
        response1 = player.use_reaction_effect(
            "Negate", card, source)
        if type(response1) == Card:
            given_list = given_list[(player_index + x):] + \
                given_list[:(player_index + x)]

            for player_index2, player2 in enumerate(given_list):
                response2 = player2.use_reaction_effect(
                    "Negate", response1, players[(player_index + x)], card)
                if type(response2) == Card:
                    given_list = given_list[(player_index2 + x):] + \
                        given_list[:(player_index2 + x)]
                    return check_negate_loop(given_list, card, source, reacting, og_card)
            else:
                print(f"{card} was negated!")
                return True
    else:
        return False


def check_aoe_negate_loop(given_list, card, source, reacting, og_card=None):
    # 'given_list' refers to the list of players included in the negate-loop (for purposes of where it starts from)
    # 'card' refers to the card played, being potentially negated
    # 'source' refers to the player of the card played
    # 'reacting' refers to the player reacting in this negate-loop
    # 'OG_card' refers to the FIRST card played (so Card can become negates being negated, this is the original card)
    x = 1 - len(players)
    given_list = given_list[(0 + x):] + given_list[:(0 + x)]
    for player_index, player in enumerate(given_list):
        response1 = player.use_reaction_effect(
            "AoE Negate", card, source)
        if response1[0]:
            given_list = given_list[(player_index + x):] + \
                given_list[:(player_index + x)]
            if not check_negate_loop(given_list, response1[1], players[(player_index + x)], response1[2], card):
                response1[2].tools_immunity = True
                print(
                    f"{response1[2].character} will be unaffected by {og_card} - negated by {response1[3].character}!")


# --- Character Cards; a class for handling individual playable characters in-game
# 1. 'Character' refers to the name of the character in question
# 2. 'Allegiance' refers to the 'allegiance' that the character belongs to (Shu, Wei, Wu or Heroes), relevant for certain effects
# 3. 'Health' refers to the amount of health that this character starts with
# 4. 'Gender' refers to the sex of the character being played
# 5. 'Char_abils' refers to the unique abilities usable by this character
class Character:
    def __init__(self, character, allegiance, health, gender, char_abils):
        self.character = character
        self.allegiance = allegiance
        self.health = health
        self.gender = gender
        self.char_abils = char_abils

    def __repr__(self):
        character_details = f"[{self.character} of {self.allegiance.upper()}, {self.gender} // {self.health} max-health.]"
        return character_details

    def __str__(self):
        character_details = f"[{self.character} of {self.allegiance.upper()}, {self.gender} // {self.health} max-health.]"
        return character_details


# --- A class for handling playing-cards used in-game
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
# 6. 'Flavour_text' refers to the description of what the individual card does (for more details, search for all_cards within generate_deck())
# 7. 'Weapon_range' refers to the range provided by the ten possible weapon-cards (within equipment cards)
# 8. 'Effect2' refers to the effect that the card will perform (typically after being modified by a character/weapon ability)
class Card:
    def __init__(self, rank, val, suit, ctype, effect, flavour_text, weapon_range=None, effect2=None):
        self.rank = rank
        self.val = val
        self.suit = suit
        self.ctype = ctype
        self.effect = effect
        self.flavour_text = flavour_text
        self.weapon_range = weapon_range
        self.effect2 = effect2

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
        if self == main_deck:
            main_deck.check_if_empty()
        return self.contents.pop(0)

    def discard_from_deck(self, num=1):
        while num > 0:
            card = main_deck.remove_from_top()
            discard_deck.add_to_top(card)
            num -= 1


# A class for handling the cards in a players' hand
class Hand(Deck):
    def __init__(self, hand):
        self.contents = []
        self.contents = hand


# --- A class for individual players and their stats in the game
# 1. 'Turn_number' is a counter that will return how many turns this player has had at the end of the game
# 2. 'Gender' refers to the sex of the character being played
# 3. 'Role' is the secret win-condition assigned to each player: Emperor, Advisor, Rebel, Spy
# 4. 'Character' refers to the players' selected character/abilities
# 5. 'Attacks_this_turn' is defaultly set to 0; players can only do 1 ATTACK per turn unless a Zhuge Crossbow is equipped
# 6. 'Current_health' is defaultly set to 4 (this will change in future versions); when a players' health reaches 0, they are on the BRINK OF DEATH!
# 7. 'Max_health' is defaultly set to 4 (this will change in future versions); current_health cannot exceed max_health
# 8. 'Hand' refers to the playing-cards in a players' hand
# 9. 'Equipment' refers to equipped is; only one of each type of equipment can be equipped at one time
# 10. 'Pending_judgements' refers to any Delay-Tool cards that have yet to take effect on a player. These take effect at the start of their turn
# 11. 'Char_abils' refers to the unique abilities usable by their character
# 12. 'Acedia_active' refers to having failed the judgement (above), and missing the action-phase of this turn - False by default
# 13. 'Lightning_immunity' applies when you have already faced judgement (above) for Lightning in this turn - False by default
# 14. 'Tools_immunity' refers to having had a Tool-card negated for an individual player - False by default
# 15. 'Used_trigrams' refers to having used Eight-Trigrams to automatically produce a defend in that single action already - False by default
class Player:
    def __init__(self, gender=None, role="Rebel", character=None):
        self.turn_number = 1
        self.gender = gender
        self.role = role
        self.character = character
        self.attacks_this_turn = 0
        self.current_health = 4
        self.max_health = 4
        self.char_abils = []
        self.hand = Hand([])
        self.equipment = []
        self.pending_judgements = []
        self.char_abils = []
        self.acedia_active = False
        self.lightning_immunity = False
        self.tools_immunity = False
        self.used_trigrams = False

    def __str__(self):
        if self.role == "Emperor":
            rolecard = "[E] "
        else:
            rolecard = ""
        equips = ""
        pending = " // Pending: "
        character_details = f"{rolecard}{self.character} // {self.current_health}/{self.max_health} HP remaining"
        for i in self.equipment:
            if i.ctype == "Weapon":
                equips += (f" // W:{i}")
            if i.ctype == "Armor":
                equips += (f" // A:{i}")
            if i.ctype == "-1 Horse":
                equips += (f" // H:{i}")
            if i.ctype == "+1 Horse":
                equips += (f" // H:{i}")
        for i in self.pending_judgements:
            if i.effect2 == "Acedia":
                pending += "[A]"
            if i.effect2 == "Lightning":
                pending += "[L]"
            if i.effect2 == "Rations Depleted":
                pending += "[R]"
        if equips != "" and pending != " // Pending: ":
            return (character_details + equips + pending)
        elif equips != "":
            return (character_details + equips)
        elif pending != " // Pending: ":
            return (character_details + pending)
        else:
            return (character_details)

    # Draw/Discard Methods
    def draw(self, deck, num=1, message=True):
        # 'deck' refers to which pile the cards are drawn from (eg. main_deck, discard_deck)
        # 'num' refers to how many cards are being drawn
        # 'message' refers to whether the game announces how many cards are being drawn
        if message:
            if num == 1:
                print(
                    f"{num} card has been added to {self.character}'s hand! ({len(self.hand.contents) + num} cards total in-hand)")
            else:
                print(
                    f"{num} cards have been added to {self.character}'s hand! ({len(self.hand.contents) + num} cards total in-hand)")
        while num > 0:
            if deck == main_deck:
                main_deck.check_if_empty()
            card = deck.remove_from_top()
            self.hand.add_to_top(card)
            num -= 1

    def discard(self, mode="Hand", num=1):
        # 'mode' refers to which cards are permitted to be discarded (eg. only 'hand', or, 'hand + equipment')
        # 'num' refers to how many cards are being discarded
        if mode == "Hand":
            if num > len(self.hand.contents):
                return self.discard_all_cards()
            while num > 0:
                total_cards = self.hand.contents
                card = random.choice(total_cards)
                self.hand.contents.remove(card)
                discard_deck.add_to_top(card)
                num -= 1

        elif mode == "Handquip":
            if num > len(self.hand.contents) + len(self.equipment):
                return self.discard_all_cards()
            while num > 0:
                total_cards = self.hand.contents + self.equipment
                card = random.choice(total_cards)
                if card in self.equipment:
                    self.equipment.remove(card)
                    discard_deck.add_to_top(card)
                    self.check_warrior_woman()
                else:
                    self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                num -= 1

        self.check_one_after_another()
        return card

    def discard_all_cards(self, death=False):
        # 'death' refers to if a player is discarding all cards upon dying, or just discarding all of their own cards (and not pending_judgements)
        cards_discarded = len(self.hand.contents) + len(self.equipment)

        while len(self.hand.contents) > 0:
            discard_deck.add_to_top(self.hand.contents.pop())

        while len(self.equipment) > 0:
            discard_deck.add_to_top(self.equipment.pop())

        if death:
            print(
                f"{self.character} discarded {cards_discarded} card(s) upon their death.")

            while len(self.pending_judgements) > 0:
                discard_deck.add_to_top(self.pending_judgements.pop())
        else:
            self.check_one_after_another()

    # Using Cards/Effects
    def use_card_effect(self, card, card2=None):
        # "Special Attack types":
        if card.effect2 == "Black Attack":
            if (self.attacks_this_turn == 0) or (self.check_weapon_zhuge_crossbow()) or (self.check_berserk()):
                targets = self.calculate_targets_in_weapon_range()
                for target in targets:
                    if target.check_empty_city():
                        targets.remove(target)
                        break

                if len(targets) < 1:
                    print(
                        f"{card}/{card2} were returned to the {self.character} due to no possible targets.")
                    return False
                else:
                    target = random.choice(targets)
                    if (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card)
                        discard_deck.add_to_top(card)
                    if (card2 != None) and (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card2)
                        discard_deck.add_to_top(card2)
                    print(
                        f"{self.character} has played a BLACK ATTACK against {target.character}.")
                    self.check_one_after_another()
                    self.activate_attack(card, target, card2)
                    return True
            else:
                return False

        elif card.effect2 == "Red Attack":
            if (self.attacks_this_turn == 0) or (self.check_weapon_zhuge_crossbow()) or (self.check_berserk()):
                targets = self.calculate_targets_in_weapon_range()
                for target in targets:
                    if target.check_empty_city():
                        targets.remove(target)
                        break

                if len(targets) < 1:
                    print(
                        f"{card}/{card2} were returned to the {self.character} due to no possible targets.")
                    return False
                else:
                    target = random.choice(targets)
                    if (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card)
                        discard_deck.add_to_top(card)
                    if (card2 != None) and (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card2)
                        discard_deck.add_to_top(card2)
                    print(
                        f"{self.character} has played a RED ATTACK against {target.character}.")
                    self.check_one_after_another()
                    self.activate_attack(card, target, card2)
                    return True
            else:
                return False

        elif card.effect2 == "Colourless Attack":
            if (self.attacks_this_turn == 0) or (self.check_weapon_zhuge_crossbow()) or (self.check_berserk()):
                targets = self.calculate_targets_in_weapon_range()
                for target in targets:
                    if target.check_empty_city():
                        targets.remove(target)
                        break

                if len(targets) < 1:
                    print(
                        f"{card}/{card2} were returned to the {self.character} due to no possible targets.")
                    return False
                else:
                    target = random.choice(targets)
                    if (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card)
                        discard_deck.add_to_top(card)
                    if (card2 != None) and (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card2)
                        discard_deck.add_to_top(card2)
                    print(
                        f"{self.character} has played a COLOURLESS ATTACK against {target.character}.")
                    self.check_one_after_another()
                    self.activate_attack(card, target, card2)
                    return True
            else:
                return False

        # card.ctype == 'Basic':
        elif card.effect2 == "Attack":
            if (self.attacks_this_turn == 0) or (self.check_weapon_zhuge_crossbow()) or (self.check_berserk()):
                targets = self.calculate_targets_in_weapon_range()
                for target in targets:
                    if target.check_empty_city():
                        targets.remove(target)
                        break

                if len(targets) < 1:
                    return False
                else:
                    target = random.choice(targets)
                    if card in self.equipment:
                        self.equipment.remove(card)
                    elif card in self.hand.contents:
                        self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                    self.check_one_after_another()
                    print(
                        f"{self.character} has played {card} to ATTACK {target.character}.")
                    extra_targets = self.check_weapon_sky_scorcher_halberd(
                        target)
                    if (extra_targets == 0):
                        self.activate_attack(card, target)
                    elif (extra_targets[0] == 1):
                        self.activate_attack(card, target)
                        self.activate_attack(card, extra_targets[1])
                    elif (extra_targets[0] == 2):
                        self.activate_attack(card, target)
                        self.activate_attack(card, extra_targets[1])
                        self.activate_attack(card, extra_targets[2])
                    return True
            else:
                return False

        elif card.effect2 == "Defend":
            if ("Dragon Heart" in self.char_abils) and ((self.attacks_this_turn == 0) or (self.check_weapon_zhuge_crossbow())):
                self.check_dragon_heart_def_to_atk(card)
                return self.use_card_effect(card)
            else:
                return False

        elif card.effect2 == "Peach":
            if self.max_health > self.current_health:
                self.hand.contents.remove(card)
                discard_deck.add_to_top(card)
                self.current_health += 1
                print(
                    f"{self.character} has used a PEACH to heal by one from {self.current_health -1} to {self.current_health}/{self.max_health}.")
                self.check_one_after_another()
                return True
            else:
                return False

        # card.ctype == 'Tool':
        elif card.effect2 == "Barbarians":
            self.hand.contents.remove(card)
            print(
                f"{self.character} has activated {card}. All players will take one damage (unless playing ATTACK or tool-card negated).")
            self.check_one_after_another()
            self.check_wisdom()

            check_aoe_negate_loop(players, card, self, self, card)

            for player in players:
                if (player != players[0]) and (player.current_health > 0) and (not player.tools_immunity):
                    barb_response = player.use_reaction_effect(
                        "Attack", card, self)
                    if type(barb_response) == Card:
                        if (barb_response.effect == "Attack") or (barb_response.effect2 == "Attack"):
                            print(
                                f"{player.character} successfully defended against BARBARIANS with {barb_response}.")
                        if (barb_response.effect2 == "Black Attack") or (barb_response.effect2 == "Red Attack") or (barb_response.effect2 == "Colourless Attack"):
                            print(
                                f"{player.character} successfully defended against BARBARIANS with a {barb_response.effect2.upper()} via SERPENT SPEAR!")
                    else:
                        print(
                            f"{player.character} failed to defend from BARBARIANS!")
                        damage_dealt = 1
                        player.current_health -= damage_dealt
                        print(
                            f"{player.character} takes {damage_dealt} damage ({player.current_health}/{player.max_health} HP remaining).")
                        for i in players:
                            if i.current_health < 1:
                                i.check_brink_of_death_loop(self)
                        player.check_bequeathed_strategy(damage_dealt)
                        player.check_evil_hero(card)
                        player.check_eye_for_an_eye(self)
                        player.check_retaliation(self, damage_dealt)

                    for i in players:
                        i.rouse_requested = False

            discard_deck.add_to_top(card)
            return True

        elif card.effect2 == "Granary":
            self.hand.contents.remove(card)
            print(f"{self.character} has activated {card}. {len(players)} cards have been flipped from the deck. Everyone (unless negated) takes a card; {self.character} goes first!")
            self.check_one_after_another()
            self.check_wisdom()

            check_aoe_negate_loop(players, card, self, self, card)

            granary = Player()
            granary.draw(main_deck, len(players), False)
            for player in players:
                if not player.tools_immunity:
                    drawn = random.choice(granary.hand.contents)
                    granary.hand.contents.remove(drawn)
                    player.hand.add_to_top(drawn)
                    print(f"{player.character} has taken {drawn} via GRANARY!")

            for i in granary.hand.contents:
                discard = granary.hand.remove_from_top()
                discard_deck.add_to_top(discard)

            discard_deck.add_to_top(card)
            return True

        elif card.effect2 == "Peach Gardens":
            self.hand.contents.remove(card)
            print(
                f"{self.character} has activated {card}. All damaged players will be healed by one health (unless negated).")
            self.check_one_after_another()
            self.check_wisdom()

            check_aoe_negate_loop(players, card, self, self, card)

            for player in players:
                if not player.tools_immunity:
                    if player.max_health > player.current_health:
                        player.current_health += 1
                        print(
                            f"{player.character} has been healed by one. ({player.current_health}/{player.max_health} HP remaining).")

            discard_deck.add_to_top(card)
            return True

        elif card.effect2 == "Rain of Arrows":
            self.hand.contents.remove(card)
            if card2 != None:
                self.hand.contents.remove(card2)
                print(
                    f"{self.character} has activated RAIN OF ARROWS using {card}/{card2}. All players will take one damage (unless playing DEFEND or tool-card negated).")
            else:
                print(
                    f"{self.character} has activated {card}. All players will take one damage (unless playing DEFEND or tool-card negated).")
            self.check_one_after_another()
            self.check_wisdom()

            check_aoe_negate_loop(players, card, self, self, card)

            for player in players:
                if (player != players[0]) and (player.current_health > 0) and (not player.tools_immunity):
                    roa_response = player.use_reaction_effect(
                        "Defend", card, self)
                    if type(roa_response) == Card:
                        if (roa_response.effect == "Defend") or (roa_response.effect2 == "Defend"):
                            print(
                                f"{player.character} successfully defended against RAIN OF ARROWS with {roa_response}.")
                    else:
                        print(
                            f"{player.character} failed to defend from RAIN OF ARROWS.")
                        damage_dealt = 1
                        player.current_health -= damage_dealt
                        print(
                            f"{player.character} takes {damage_dealt} damage ({player.current_health}/{player.max_health} HP remaining).")

                        for i in players:
                            if i.current_health < 1:
                                i.check_brink_of_death_loop(self)
                        player.check_bequeathed_strategy(damage_dealt)
                        player.check_evil_hero(card, card2)
                        player.check_eye_for_an_eye(self)
                        player.check_retaliation(self, damage_dealt)

                    for i in players:
                        i.escort_requested = False

            discard_deck.add_to_top(card)
            if card2 != None:
                discard_deck.add_to_top(card2)
            return True

        elif card.effect2 == "Coerce":
            possible_targets = 0
            for player in players[1:]:
                if len(player.equipment) > 0:
                    for i in player.equipment:
                        if i.ctype == "Weapon":
                            possible_targets += 1

            if possible_targets == 0:
                return False

            elif possible_targets > 0:
                targets = []
                for player in players[1:]:
                    for i in player.equipment:
                        if i.ctype == "Weapon":
                            targets.append(player)

                coerced = random.choice(targets)
                targets = coerced.calculate_targets_in_weapon_range()
                for player in targets:
                    if player.check_empty_city():
                        targets.remove(player)
                        break

                if len(targets) < 1:
                    return False
                else:
                    self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                    attacked = random.choice(targets)
                    print(
                        f"{coerced.character} is being coerced into attacking {attacked.character}!")
                    self.check_one_after_another()
                    self.check_wisdom()
                    if not check_negate_loop(players, card, self, coerced):
                        coerced.activate_coerce(attacked)
                    return True

        elif card.effect2 == "Dismantle":
            target = random.choice(players[1:])

            if (len(target.hand.contents) + len(target.equipment) + len(target.pending_judgements)) < 1:
                return False
            else:
                if card in self.hand.contents:
                    self.hand.contents.remove(card)
                else:
                    self.equipment.remove(card)
                discard_deck.add_to_top(card)
                print(
                    f"{self.character} has played {card} as DISMANTLE against {target.character}.")
                self.check_one_after_another()
                self.check_wisdom()
                if not check_negate_loop(players, card, self, target):
                    self.activate_dismantle(card, target)
                return True

        elif card.effect2 == "Duel":
            targets = players[1:]
            for player in targets:
                if player.check_empty_city():
                    targets.remove(player)
                    break

            if len(targets) < 1:
                return False

            target = random.choice(targets)
            self.hand.contents.remove(card)
            discard_deck.add_to_top(card)
            print(
                f"{self.character} has played {card} as DUEL against {target.character}.")
            self.check_one_after_another()
            self.check_wisdom()
            if not check_negate_loop(players, card, self, target):
                self.activate_duel(card, target)
            return True

        elif card.effect2 == "Greed":
            self.hand.contents.remove(card)
            discard_deck.add_to_top(card)
            print(f"{self.character} has played {card}.")
            self.check_one_after_another()
            self.check_wisdom()
            if not check_negate_loop(players, card, self, self):
                self.draw(main_deck, 2)
            return True

        elif card.effect2 == "Negate":
            return False

        elif card.effect2 == "Steal":
            if self.check_wisdom():
                targets = players[1:]
            else:
                targets = self.calculate_targets_in_physical_range()

            for player in targets:
                if player.check_humility():
                    targets.remove(player)
                    break

            if len(targets) < 1:
                return False
            target = random.choice(targets)

            if (len(target.hand.contents) + len(target.equipment) + len(target.pending_judgements)) < 1:
                return False
            else:
                self.hand.contents.remove(card)
                discard_deck.add_to_top(card)
                self.check_wisdom()
                print(
                    f"{self.character} has played {card} as STEAL against {target.character}.")
                self.check_one_after_another()
                self.check_wisdom()
                if not check_negate_loop(players, card, self, target):
                    self.activate_steal(card, target)
                return True

        # card.ctype == 'Delay-Tool':
        elif card.effect2 == "Acedia":
            targets = players[1:]
            for player in targets:
                if player.check_humility():
                    targets.remove(player)
                    break

            if len(targets) < 1:
                return False
            target = random.choice(targets)
            for i in target.pending_judgements:
                if i.effect2 == 'Acedia':
                    return False

            else:
                if card in self.hand.contents:
                    self.hand.contents.remove(card)
                else:
                    self.equipment.remove(card)
                target.pending_judgements.insert(0, card)
                print(
                    f"{self.character} has placed {card} as ACEDIA on {target.character}!")
                self.check_one_after_another()
                self.check_wisdom()
                return True

        elif card.effect2 == "Lightning":
            for i in self.pending_judgements:
                if i.effect2 == 'Lightning':
                    return False
            else:
                self.hand.contents.remove(card)
                self.pending_judgements.insert(0, card)
                print(f"{self.character} has called {card}.")
                self.check_one_after_another()
                self.check_wisdom()
                return True

        elif card.effect2 == "Rations Depleted":
            return False

        # card.ctype == 'Equipment':
        elif card.ctype == "Weapon":
            weapon_index = None
            for i_index, i in enumerate(self.equipment):
                if i.ctype == "Weapon":
                    weapon_index = i_index
                    break

            if weapon_index != None:
                discard_deck.add_to_top(self.equipment.pop(weapon_index))
            self.hand.contents.remove(card)
            self.equipment.append(card)
            print(f"{self.character} has equipped {card}.")
            self.check_one_after_another()
            return True

        elif card.ctype == "Armor":
            armor_index = None
            for i_index, i in enumerate(self.equipment):
                if i.ctype == "Armor":
                    armor_index = i_index
                    break

            if armor_index != None:
                discard_deck.add_to_top(self.equipment.pop(armor_index))
            self.hand.contents.remove(card)
            self.equipment.append(card)
            print(f"{self.character} has equipped {card}.")
            self.check_one_after_another()
            return True

        elif card.ctype == "-1 Horse":
            horse_index = None
            for i_index, i in enumerate(self.equipment):
                if i.ctype == "-1 Horse":
                    horse_index = i_index
                    break

            if horse_index != None:
                discard_deck.add_to_top(self.equipment.pop(horse_index))
            self.hand.contents.remove(card)
            self.equipment.append(card)
            print(f"{self.character} has equipped {card}.")
            self.check_one_after_another()
            return True

        elif card.ctype == "+1 Horse":
            horse_index = None
            for i_index, i in enumerate(self.equipment):
                if i.ctype == "+1 Horse":
                    horse_index = i_index
                    break

            if horse_index != None:
                discard_deck.add_to_top(self.equipment.pop(horse_index))
            self.hand.contents.remove(card)
            self.equipment.append(card)
            print(f"{self.character} has equipped {card}.")
            self.check_one_after_another()
            return True

    def use_reaction_effect(self, response_required, card, source, other_card=None):
        # 'response_required' refers to what sort of reaction-effect needed, eg. ATTACK, DEFEND, PEACH, NEGATE?
        # 'card' refers to the card played that is being 'reacted' against
        # 'source' refers to the person who played the 'card'
        # 'other_card' refers to the original card used, typically required in reactions to reactions to reactions etc...
        output_value = 0
        for i in self.hand.contents:
            i.effect2 = None
        for i in self.equipment:
            i.effect2 = None
        reactions_possible = True
        while reactions_possible:
            if response_required == "Brink Of Death":
                possible_cards = []

                # Check all possible cards
                if ("First Aid" in self.char_abils):
                    for i in self.hand.contents:
                        if i.effect == "Peach":
                            possible_cards.append(i)
                        elif (i.suit == "\u2665" or i.suit == "\u2666") and (self != players[0]):
                            possible_cards.append(i)
                    for i in self.equipment:
                        possible_cards.append(i)

                else:
                    for i in self.hand.contents:
                        if i.effect == "Peach":
                            possible_cards.append(i)

                # Choice of activation of response, and subsequent choice of card
                if len(possible_cards) > 0:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        peach = random.choice(possible_cards)
                        if peach in self.equipment:
                            self.check_first_aid(peach)
                            self.equipment.remove(peach)
                        else:
                            self.check_first_aid(peach)
                            self.hand.contents.remove(peach)
                        discard_deck.add_to_top(peach)
                        output_value += 1
                        output_value += source.check_rescued(self)

                        if self == source:
                            print(
                                f"{self.character} has healed themselves using a {peach}! ({self.current_health + output_value}/{self.max_health} HP remaining!)")
                            self.check_one_after_another()
                        else:
                            print(
                                f"{self.character} has healed {source.character} using a {peach}. ({source.current_health + output_value}/{source.max_health} HP remaining!)")
                            self.check_one_after_another()
                            if source.check_break_brink_loop(output_value):
                                return output_value
                    else:
                        reactions_possible = False
                        return output_value
                else:
                    reactions_possible = False
                    return output_value

            elif response_required == "Negate":
                possible_cards = []
                for i in self.hand.contents:
                    if i.effect == "Negate":
                        possible_cards.append(i)

                if len(possible_cards) > 0:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        negate = random.choice(possible_cards)
                        self.hand.contents.remove(negate)
                        discard_deck.add_to_top(negate)

                        if card.ctype == "Delay-Tool":
                            print(
                                f"{self.character} has played a {negate} against the pending {card} on {source.character}!")
                            self.check_one_after_another()
                            self.check_wisdom()
                        else:
                            print(
                                f"{self.character} has played a {negate} against the {card} of {source.character}!")
                            self.check_one_after_another()
                            self.check_wisdom()
                        return negate
                return False

            elif response_required == "AoE Negate":
                possible_cards = []
                for i in self.hand.contents:
                    if i.effect == "Negate":
                        possible_cards.append(i)

                if len(possible_cards) > 0:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        targets = []
                        for player in players:
                            if (card.effect2 == "Barbarians" or card.effect2 == "Rain of Arrows") and (player != players[0]):
                                targets.append(player)
                            elif (card.effect2 == "Granary"):
                                targets.append(player)
                            elif (card.effect2 == "Peach Gardens") and (player.max_health > player.current_health):
                                targets.append(player)

                        if len(targets) > 0:
                            negated_for = random.choice(targets)
                            negate = random.choice(possible_cards)
                            self.hand.contents.remove(negate)
                            discard_deck.add_to_top(negate)
                            self.check_wisdom()
                            print(
                                f"{self.character} played a {negate} against the effects of {card.effect2.upper()} on {negated_for.character}!")
                            self.check_one_after_another()
                            self.check_wisdom()
                            return [True, negate, negated_for, self]
                return [False, None, None, None]

            elif response_required == "Rouse Attack":
                attack = 0
                attack2 = 0
                possible_cards = []

                # Check all possible cards
                if ("Dragon Heart" in self.char_abils):
                    for i in self.hand.contents:
                        if (i.effect == "Attack") or (i.effect == "Defend"):
                            possible_cards.append(i)

                elif ("Warrior Saint" in self.char_abils):
                    for i in self.hand.contents:
                        if (i.effect == "Attack") or (i.suit == "\u2665") or (i.suit == "\u2666"):
                            possible_cards.append(i)
                    for i in self.equipment:
                        if (i.suit == "\u2665") or (i.suit == "\u2666"):
                            possible_cards.append(i)

                else:
                    for i in self.hand.contents:
                        if i.effect == "Attack":
                            possible_cards.append(i)

                # Check for Serpent Spear
                if (serp_spear in self.equipment) and (len(self.hand.contents) > 1):
                    possible_cards.append(serp_spear)

                # Choice of activation of response, and subsequent choice of card
                if len(possible_cards) > 0:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        attack = random.choice(possible_cards)
                        if attack == serp_spear:
                            attack, attack2 = self.check_weapon_serpent_spear()
                        elif attack in self.equipment:
                            self.check_warrior_saint(attack)
                            self.equipment.remove(attack)
                            discard_deck.add_to_top(attack)
                        else:
                            self.check_dragon_heart_def_to_atk(attack)
                            self.check_warrior_saint(attack)
                            self.hand.contents.remove(attack)
                            discard_deck.add_to_top(attack)
                        attack.effect2 = "Attack"
                        for player in players:
                            player.rouse_requested = False

                return attack, attack2

            elif response_required == "Escort Defend":
                defend = 0
                possible_cards = []

                # Check for Eight Trigrams
                armor = False
                for eight_trigrams in self.equipment:
                    if eight_trigrams.effect == "Eight-Trigrams":
                        armor = True
                        break
                if armor:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        defend = self.check_armor_eight_trigrams()
                        if type(defend) == Card:
                            return defend

                # Check all possible cards
                if ("Dragon Heart" in self.char_abils):
                    for i in self.hand.contents:
                        if (i.effect == "Defend") or (i.effect == "Attack"):
                            possible_cards.append(i)

                elif ("Impetus" in self.char_abils):
                    for i in self.hand.contents:
                        if (i.effect == "Defend") or (i.suit == "\u2660") or (i.suit == "\u2663"):
                            possible_cards.append(i)

                else:
                    for i in self.hand.contents:
                        if i.effect == "Defend":
                            possible_cards.append(i)

                # Choice of activation of response, and subsequent choice of card
                if len(possible_cards) > 0:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        defend = random.choice(possible_cards)
                        self.check_dragon_heart_atk_to_def(defend)
                        self.check_impetus(defend)
                        self.hand.contents.remove(defend)
                        discard_deck.add_to_top(defend)
                        self.check_one_after_another()
                        defend.effect2 = "Defend"
                        for player in players:
                            player.escort_requested = False

                return defend

            elif response_required == "Attack" and card.effect2 == "Barbarians":
                attack = 0
                possible_cards = []

                # Check all possible cards
                if ("Dragon Heart" in self.char_abils):
                    for i in self.hand.contents:
                        if (i.effect == "Attack") or (i.effect == "Defend"):
                            possible_cards.append(i)

                elif ("Rouse (Ruler Ability)" in self.char_abils) and ((self.role == "Emperor") or ("False Ruler" in self.char_abils)):
                    for i in self.hand.contents:
                        if i.effect == "Attack":
                            possible_cards.append(i)
                    targets = []
                    for player in players:
                        if (player != self) and (player.allegiance == "Shu"):
                            if (player.rouse_requested == False):
                                targets.append(player)
                    if len(targets) > 0:
                        possible_cards.append("Rouse")

                elif ("Warrior Saint" in self.char_abils):
                    for i in self.hand.contents:
                        if (i.effect == "Attack") or (i.suit == "\u2665") or (i.suit == "\u2666"):
                            possible_cards.append(i)
                    for i in self.equipment:
                        if (i.suit == "\u2665") or (i.suit == "\u2666"):
                            possible_cards.append(i)

                else:
                    for i in self.hand.contents:
                        if i.effect == "Attack":
                            possible_cards.append(i)

                # Check for Serpent Spear
                if (serp_spear in self.equipment) and (len(self.hand.contents) > 1):
                    possible_cards.append(serp_spear)

                # Choice of activation of response, and subsequent choice of card
                if len(possible_cards) > 0:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        attack = random.choice(possible_cards)

                        if attack == "Rouse":
                            attack = self.check_rouse()
                            if type(attack) == tuple:
                                (attack, attack2) = attack
                            if attack != "Repeat":
                                for player in players:
                                    player.rouse_requested = False

                        elif attack == serp_spear:
                            attack = self.check_weapon_serpent_spear()
                            attack[0] = attack
                            for player in players:
                                player.rouse_requested = False

                        elif attack in self.equipment:
                            self.check_warrior_saint(attack)
                            self.equipment.remove(attack)
                            discard_deck.add_to_top(attack)
                            for player in players:
                                player.rouse_requested = False

                        else:
                            self.check_dragon_heart_def_to_atk(attack)
                            self.check_warrior_saint(attack)
                            self.hand.contents.remove(attack)
                            discard_deck.add_to_top(attack)
                            for player in players:
                                player.rouse_requested = False

                        self.check_one_after_another()
                        if type(attack) == Card:
                            attack.effect2 = "Attack"

                if attack != "Repeat":
                    return attack

            elif response_required == "Defend" and card.effect2 == "Rain of Arrows":
                defend = 0
                possible_cards = []

                # Check for Eight Trigrams
                armor = False
                for eight_trigrams in self.equipment:
                    if eight_trigrams.effect == "Eight-Trigrams":
                        armor = True
                        break
                if armor:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        defend = self.check_armor_eight_trigrams()
                        if type(defend) == Card:
                            return defend

                # Check all possible cards
                if ("Dragon Heart" in self.char_abils):
                    for i in self.hand.contents:
                        if (i.effect == "Defend") or (i.effect == "Attack"):
                            possible_cards.append(i)

                elif ("Escort (Ruler Ability)" in self.char_abils) and ((self.role == "Emperor") or ("False Ruler" in self.char_abils)):
                    for i in self.hand.contents:
                        if i.effect == "Defend":
                            possible_cards.append(i)
                    targets = []
                    for player in players:
                        if (player != self) and (player.allegiance == "Wei"):
                            if (player.escort_requested == False):
                                targets.append(player)
                    if len(targets) > 0:
                        possible_cards.append("Escort")

                elif ("Impetus" in self.char_abils):
                    for i in self.hand.contents:
                        if (i.effect == "Defend") or (i.suit == "\u2660") or (i.suit == "\u2663"):
                            possible_cards.append(i)

                else:
                    for i in self.hand.contents:
                        if i.effect == "Defend":
                            possible_cards.append(i)

                # Choice of activation of response, and subsequent choice of card
                if len(possible_cards) > 0:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        defend = random.choice(possible_cards)
                        self.check_dragon_heart_atk_to_def(defend)
                        self.check_impetus(defend)
                        if defend in self.hand.contents:
                            self.hand.contents.remove(defend)
                            discard_deck.add_to_top(defend)
                        self.check_one_after_another()
                        if type(defend) == Card:
                            defend.effect2 = "Defend"
                        for player in players:
                            player.escort_requested = False

                return defend

            elif response_required == "Attack" and card.effect2 == "Duel":
                required = 1
                if source.check_without_equal():
                    required += 1
                activated = False

                while required > 0:
                    possible_cards = []

                    # Check all possible cards
                    if ("Dragon Heart" in self.char_abils):
                        for i in self.hand.contents:
                            if (i.effect == "Attack") or (i.effect == "Defend"):
                                possible_cards.append(i)

                    elif ("Rouse (Ruler Ability)" in self.char_abils) and ((self.role == "Emperor") or ("False Ruler" in self.char_abils)):
                        for i in self.hand.contents:
                            if i.effect == "Attack":
                                possible_cards.append(i)
                        targets = []
                        for player in players:
                            if (player != self) and (player.allegiance == "Shu"):
                                if (player.rouse_requested == False):
                                    targets.append(player)
                        if len(targets) > 0:
                            possible_cards.append("Rouse")

                    elif ("Warrior Saint" in self.char_abils):
                        for i in self.hand.contents:
                            if (i.effect == "Attack") or (i.suit == "\u2665") or (i.suit == "\u2666"):
                                possible_cards.append(i)
                        for i in self.equipment:
                            if (i.suit == "\u2665") or (i.suit == "\u2666"):
                                possible_cards.append(i)

                    else:
                        for i in self.hand.contents:
                            if i.effect == "Attack":
                                possible_cards.append(i)

                    # Check for Serpent Spear
                    if (serp_spear in self.equipment) and (len(self.hand.contents) > 1):
                        possible_cards.append(serp_spear)

                    # Choice of activation of response, and subsequent choice of card
                    if len(possible_cards) >= required:
                        choices = [True, False]
                        activated = random.choice(choices)
                        if activated:
                            attack = random.choice(possible_cards)

                            if attack == "Rouse":
                                attack = self.check_rouse()
                                if type(attack) == tuple:
                                    (attack, attack2) = attack
                                if attack != "Repeat":
                                    required -= 1
                                    for player in players:
                                        player.rouse_requested = False

                            elif attack == serp_spear:
                                attack = self.check_weapon_serpent_spear()
                                attack = attack[0]
                                required -= 1
                                for player in players:
                                    player.rouse_requested = False

                            elif attack in self.equipment:
                                self.check_warrior_saint(attack)
                                self.equipment.remove(attack)
                                discard_deck.add_to_top(attack)
                                required -= 1
                                for player in players:
                                    player.rouse_requested = False

                            else:
                                self.check_dragon_heart_def_to_atk(attack)
                                self.check_warrior_saint(attack)
                                self.hand.contents.remove(attack)
                                discard_deck.add_to_top(attack)
                                print(
                                    f"{self.character} played an {attack} during the DUEL!")
                                self.check_one_after_another()
                                if type(attack) == Card:
                                    attack.effect2 = "Attack"
                                    required -= 1
                                for player in players:
                                    player.rouse_requested = False

                        else:
                            print(f"{self.character} did not play an ATTACK!")
                            return True
                    elif (required > len(possible_cards)):
                        print(f"{self.character} did not play an ATTACK!")
                        return True

                duel_won = source.use_reaction_effect(
                    "Attack", card, self)
                if duel_won:
                    return False
                else:
                    return True

            elif response_required == "Defend" and ((card.effect2 == "Attack") or (card.effect2 == "Black Attack") or (card.effect2 == "Red Attack") or (card.effect2 == "Colourless Attack")):
                required = 1
                if source.check_without_equal():
                    required += 1

                while required > 0:
                    defend = 0
                    possible_cards = []

                    # Check for Eight Trigrams
                    armor = False
                    for eight_trigrams in self.equipment:
                        if eight_trigrams.effect == "Eight-Trigrams":
                            armor = True
                            break
                    if (source.check_weapon_black_pommel() == True) and armor:
                        print(
                            f"  >> {source.character} has [Black Pommel <:2:> - 6\u2660] equipped, and therefore ignores any armor when attacking.")
                    elif not source.check_weapon_black_pommel() and armor:
                        choices = [True, False]
                        activated = random.choice(choices)
                        if activated:
                            defend = self.check_armor_eight_trigrams()
                            if type(defend) == Card:
                                required -= 1
                                for player in players:
                                    player.escort_requested = False
                                if required == 0:
                                    return defend
                                else:
                                    choices = [True, False]
                                    activated = random.choice(choices)
                                    if activated:
                                        defend = self.check_armor_eight_trigrams()
                                        if type(defend) == Card:
                                            required -= 1
                                            for player in players:
                                                player.escort_requested = False
                                            if required == 0:
                                                return defend

                    # Check all possible cards
                    if ("Dragon Heart" in self.char_abils):
                        for i in self.hand.contents:
                            if (i.effect == "Defend") or (i.effect == "Attack"):
                                possible_cards.append(i)

                    elif ("Escort (Ruler Ability)" in self.char_abils) and ((self.role == "Emperor") or ("False Ruler" in self.char_abils)):
                        for i in self.hand.contents:
                            if i.effect == "Defend":
                                possible_cards.append(i)
                        targets = []
                        for player in players:
                            if (player != self) and (player.allegiance == "Wei"):
                                if (player.escort_requested == False):
                                    targets.append(player)
                        if len(targets) > 0:
                            possible_cards.append("Escort")

                    elif ("Impetus" in self.char_abils):
                        for i in self.hand.contents:
                            if (i.effect == "Defend") or (i.suit == "\u2660") or (i.suit == "\u2663"):
                                possible_cards.append(i)

                    else:
                        for i in self.hand.contents:
                            if i.effect == "Defend":
                                possible_cards.append(i)

                    # Choice of activation of response, and subsequent choice of card
                    if len(possible_cards) >= required:
                        choices = [True, False]
                        activated = random.choice(choices)
                        if activated:
                            defend = random.choice(possible_cards)
                            self.check_dragon_heart_atk_to_def(defend)
                            self.check_impetus(defend)
                            if defend in self.hand.contents:
                                self.hand.contents.remove(defend)
                                discard_deck.add_to_top(defend)
                            self.check_one_after_another()
                            if type(defend) == Card:
                                defend.effect2 = "Defend"
                            required -= 1
                            for player in players:
                                player.escort_requested = False
                            if required == 0:
                                return defend
                    else:
                        return defend
                return defend

            else:
                print(f"Something strange happened to {self.character} here!")
                return False

    def activate_attack(self, card, target, card2=None):
        # 'card' refers to the 'Attack' card used in Player.use_card_effect(card)
        # 'target' refers to the player targeted by Attack!
        # 'attacker' refers to the source of the Attack (Coerce causes this to vary!)
        # 'card2' refers to any secondary 'Attack' cards used; this is used when there are any special effects (such as Serpent Spear)
        self.attacks_this_turn += 1

        # Early reactionary abilities
        target = target.check_displacement(self)

        # Weapon and Black Shield checks
        self.check_weapon_gender_swords(target)
        armor = False
        if (card2 == None) or (card2.effect2 == "Black Attack"):
            if target.check_armor_black_shield(card):
                armor = True
            if (self.check_weapon_black_pommel() == True) and armor:
                print(
                    f"  >> {self.character} has [Black Pommel <:2:> - 6\u2660] equipped, and therefore ignores any armor when attacking.")
            elif armor:
                return "Break"

        # Undodgeable ATTACK checks
        if self.check_fearsome_archer(card, card2, target):
            return "Break"
        if self.check_iron_cavalry(card, card2, target):
            return "Break"

        # Check for DEFEND
        attack_defended = target.use_reaction_effect(
            "Defend", card, self)
        if type(attack_defended) == Card:
            if (attack_defended.effect == "Defend") or (attack_defended.effect2 == "Defend"):
                print(
                    f"{target.character} successfully defended the ATTACK with {attack_defended}.")

                # DEFENDED - reactionary abilities
                self.check_fearsome_advance(target)
                self.check_weapon_axe(target)
                self.check_weapon_green_dragon_halberd(target)

        else:
            # DAMAGED - pre-damage abilities
            if self.check_weapon_frost_blade(target):
                return "Break"

            # Damage Resolution
            damage_dealt = 1
            if self.used_bare_the_chest:
                damage_dealt += 1

            target.current_health -= damage_dealt
            print(f"{self.character} attacked {target.character}, dealing {damage_dealt} damage ({target.current_health}/{target.max_health} HP remaining).")
            self.check_weapon_huangs_longbow(target)
            for player in players:
                if player.current_health < 1:
                    player.check_brink_of_death_loop(self)

            # Retaliatory Abilities (post-damage)
            target.check_bequeathed_strategy(damage_dealt)
            target.check_evil_hero(card, card2)
            target.check_eye_for_an_eye(self)
            target.check_retaliation(self, damage_dealt)

    def activate_coerce(self, target):
        # 'target' refers to the player that will potentially be attacked by the coerced player!
        possible_cards = []

        if ("Dragon Heart" in self.char_abils):
            for i in self.hand.contents:
                if (i.effect == "Attack") or (i.effect == "Defend"):
                    possible_cards.append(i)

        elif ("Rouse (Ruler Ability)" in self.char_abils) and ((self.role == "Emperor") or ("False Ruler" in self.char_abils)):
            for i in self.hand.contents:
                if i.effect == "Attack":
                    possible_cards.append(i)
            targets = []
            for player in players:
                if (player != self) and (player.allegiance == "Shu"):
                    if (player.rouse_requested == False):
                        targets.append(player)
            if len(targets) > 0:
                possible_cards.append("Rouse")

        elif ("Warrior Saint" in self.char_abils):
            for i in self.hand.contents:
                if (i.effect == "Attack") or ((i.suit == "\u2665") or (i.suit == "\u2666")):
                    possible_cards.append(i)
            for i in self.equipment:
                if (i.suit == "\u2665") or (i.suit == "\u2666"):
                    possible_cards.append(i)

        else:
            for i in self.hand.contents:
                if i.effect == "Attack":
                    possible_cards.append(i)

        # Check for Serpent Spear
        if (serp_spear in self.equipment) and (len(self.hand.contents) > 1):
            possible_cards.append(serp_spear)

        if (len(possible_cards) > 0):
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                card = random.choice(possible_cards)
                card2 = None
                if card == "Rouse":
                    card = self.check_rouse()
                    if type(card) == tuple:
                        (card, card2) = card
                    if card != "Repeat":
                        for player in players:
                            player.rouse_requested = False
                    if card == "Repeat":
                        return self.activate_coerce(target)
                elif card == serp_spear:
                    card = self.check_weapon_serpent_spear()
                    return self.activate_attack(card[0], target, card[1])
                elif card in self.equipment:
                    self.check_warrior_saint(card)
                    self.equipment.remove(card)
                    discard_deck.add_to_top(card)
                else:
                    self.check_dragon_heart_def_to_atk(card)
                    self.check_warrior_saint(card)
                    self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                print(
                    f"{self.character} was coerced into attacking {target.character}.")
                self.check_one_after_another()
                extra_targets = self.check_weapon_sky_scorcher_halberd(
                    target)
                if (extra_targets == 0):
                    if card2 == None:
                        self.activate_attack(card, target)
                    else:
                        self.activate_attack(card, target, card2)
                elif (extra_targets[0] == 1):
                    self.activate_attack(card, target)
                    self.activate_attack(card, extra_targets[1])
                elif (extra_targets[0] == 2):
                    self.activate_attack(card, target)
                    self.activate_attack(card, extra_targets[1])
                    self.activate_attack(card, extra_targets[2])
                return True

        for i in self.equipment:
            if i.ctype == "Weapon":
                self.equipment.remove(i)
                self.check_warrior_woman()
                players[0].hand.add_to_top(i)
                print(
                    f"{self.character}'s weapon; {i}, has been stolen by {players[0].character} for not attacking {target.character}!")
                return True

    def activate_dismantle(self, card, target):
        # 'card' refers to the 'Dismantle' card used in Player.use_card_effect(card)
        # 'target' refers to the player targeted by Dismantle!
        # 'dismantled' refers to the card targeted by Dismantle!
        total_cards = target.hand.contents + target.equipment + target.pending_judgements
        if len(total_cards) > 0:
            dismantled = random.choice(total_cards)
            if dismantled in target.pending_judgements:
                target.pending_judgements.remove(dismantled)
                discard_deck.add_to_top(dismantled)
                print(
                    f"{self.character} dismantled {dismantled} from the pending judgements of {target.character}!")

            elif dismantled in target.equipment:
                target.equipment.remove(dismantled)
                discard_deck.add_to_top(dismantled)
                print(
                    f"{self.character} dismantled {dismantled} from the equipment of {target.character}!")
                target.check_warrior_woman()

            elif dismantled in target.hand.contents:
                target.hand.contents.remove(dismantled)
                discard_deck.add_to_top(dismantled)
                print(
                    f"{self.character} dismantled {dismantled} from the hand of {target.character}!")
                self.check_one_after_another()
                target.check_one_after_another()

    def activate_duel(self, card, target):
        # 'card' refers to the 'Duel' card used in Player.use_card_effect(card)
        # 'target' refers to the player targeted by Duel!
        # 'duel_won' is a boolean that determines the winner of the duel
        duel_won = target.use_reaction_effect("Attack", card, self)
        damage_dealt = 1

        if duel_won:
            if self.used_bare_the_chest:
                damage_dealt += 1
            target.current_health -= damage_dealt
            print(
                f"{self.character} has won the DUEL! {target.character} takes {damage_dealt} damage! ({target.current_health}/{target.max_health} HP remaining).")
            for player in players:
                if player.current_health < 1:
                    player.check_brink_of_death_loop(self)
            target.check_bequeathed_strategy(damage_dealt)
            target.check_evil_hero(card)
            target.check_eye_for_an_eye(self)
            target.check_retaliation(self, damage_dealt)

        elif not duel_won:
            self.current_health -= damage_dealt
            print(
                f"{target.character} has won the DUEL! {self.character} takes {damage_dealt} damage! ({self.current_health}/{self.max_health} HP remaining).")
            for player in players:
                if player.current_health < 1:
                    player.check_brink_of_death_loop(target)
            self.check_bequeathed_strategy(damage_dealt)
            self.check_evil_hero(card)
            self.check_eye_for_an_eye(target)
            self.check_retaliation(target, damage_dealt)

    def activate_steal(self, card, target):
        # 'card' refers to the 'Dismantle' card used in Player.use_card_effect(card)
        # 'target' refers to the player targeted by Steal!
        # 'stolen' refers to the card targeted by Steal!
        total_cards = target.hand.contents + target.equipment + target.pending_judgements
        if len(total_cards) > 0:
            stolen = random.choice(total_cards)
            if stolen in target.pending_judgements:
                target.pending_judgements.remove(stolen)
                self.hand.add_to_top(stolen)
                print(
                    f"{self.character} stole {stolen} from the pending judgements of {target.character}!")

            elif stolen in target.equipment:
                target.equipment.remove(stolen)
                self.hand.add_to_top(stolen)
                print(
                    f"{self.character} stole {stolen} from the equipment of {target.character}!")
                target.check_warrior_woman()

            elif stolen in target.hand.contents:
                target.hand.contents.remove(stolen)
                self.hand.add_to_top(stolen)
                print(
                    f"{self.character} stole a card from the hand of {target.character}!")
                target.check_one_after_another()

    # In-game General Checks
    def calculate_targets_in_physical_range(self, modifier=0):
        # 'modifier' refers to any bonuses granted/penalized by abilities/equipment
        my_index = get_player_index(self)
        indexes = []
        if self.check_horsemanship():
            modifier += 1

        for i in self.equipment:
            if i.ctype == "-1 Horse":
                modifier += 1
                break

        for (target_index, target) in enumerate(players):
            if target_index != my_index:
                distance = abs(target_index - my_index)

                target_modifier = 0
                for i in target.equipment:
                    if i.ctype == "+1 Horse":
                        target_modifier += 1
                        break

                if distance > len(players) / 2:
                    distance = len(players) - distance
                if distance - (1 + modifier) + (target_modifier) <= 0:
                    indexes.append(target_index)

        output = []
        for index in indexes:
            output.append(players[index])

        return output

    def calculate_targets_in_weapon_range(self, modifier=0, omit=None):
        # 'modifier' refers to any bonuses granted/penalized by abilities/equipment
        # 'omit' refers to any players that are untargetable during this calculation
        my_index = get_player_index(self)
        indexes = []
        weapon_range = 1
        if self.check_horsemanship():
            modifier += 1

        for i in self.equipment:
            if i.ctype == "-1 Horse":
                modifier += 1
            if i.ctype == "Weapon":
                weapon_range = i.weapon_range

        for (target_index, target) in enumerate(players):
            if target_index != my_index:
                distance = abs(target_index - my_index)

                target_modifier = 0
                for i in target.equipment:
                    if i.ctype == "+1 Horse":
                        target_modifier += 1
                        break

                if distance > len(players) / 2:
                    distance = len(players) - distance
                if distance - (weapon_range + modifier) + (target_modifier) <= 0:
                    indexes.append(target_index)

        output = []
        for index in indexes:
            if players[index] != omit:
                output.append(players[index])

        return output

    def check_break_brink_loop(self, amount_healed):
        if self.current_health + amount_healed > 0:
            return True
        else:
            return False

    def check_brink_of_death_loop(self, source):
        # 'source' refers to the player that is considered the source of the damage - this is relevant for attributing bounties/punishments for kills!
        if (self.max_health != 0) and (self.current_health < 1):
            print(f"{self.character} is on the brink of death ({self.current_health}/{self.max_health} health), and must be brought back to life with a PEACH or WINE.")
            dying_index = get_player_index(self)
            reacting_index = dying_index

            # Peach Loop
            for player in players[dying_index:]:
                if self.current_health > 0:
                    break
                self.current_health += player.use_reaction_effect(
                    "Brink Of Death", None, self)
                reacting_index += 1
                if reacting_index >= len(players):
                    reacting_index -= len(players)
            for player in players[:dying_index]:
                if self.current_health > 0:
                    break
                self.current_health += player.use_reaction_effect(
                    "Brink Of Death", None, self)
                reacting_index += 1
                if reacting_index >= len(players):
                    reacting_index -= len(players)

            # If player died
            if self.current_health < 1:
                if roles != 0:
                    print(
                        f"{self.character} wasn't saved from the brink of death! Their role is {self.role}!")
                else:
                    print(
                        f"{self.character} wasn't saved from the brink of death!")
                self.discard_all_cards(death=True)
                players.pop(dying_index)
                if roles != 0:
                    roles_dict[self.role] -= 1

                if source != None:
                    if (self.role == "Rebel"):
                        print(
                            f"{source.character} draws 3 cards for killing {self.character}!")
                        source.draw(main_deck, 3, False)
                    if (self.role == "Advisor") and (source.role == "Emperor"):
                        print(
                            f"{source.character} loses all their cards for killing their Advisor ({self.character}).")
                        source.discard_all_cards()
                return "Break"

            # If player survived
            else:
                print(
                    f"{self.character} has been successfully healed back to {self.current_health}/{self.max_health} HP.")

    def check_pending_judgements(self):
        while len(self.pending_judgements) > 0:
            pending_judgement = self.pending_judgements.pop(0)

            # ACEDIA
            if pending_judgement.effect2 == 'Acedia':
                if not check_negate_loop(players, pending_judgement, self, self):
                    print(
                        f"{self.character} must face judgement for ACEDIA; (needs \u2665 to pass, or else misses action-phase of turn).")
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    self.check_envy_of_heaven()
                    print(
                        f"  >> Judgement: {self.character} flipped a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, self)

                    if judgement_card.suit == "\u2665":
                        print(
                            f"{self.character}'s judgement card is a {judgement_card}, and therefore {pending_judgement} has no effect.")
                    else:
                        print(
                            f"{self.character}'s judgement card is a {judgement_card}, and thus they miss their action-phase of this turn.")
                        self.acedia_active = True
                discard_deck.add_to_top(pending_judgement)

            # LIGHTNING
            elif (pending_judgement.effect2 == 'Lightning') and (self.lightning_immunity == False):
                move_lightning = False
                self.lightning_immunity = True
                print(
                    f"{self.character} must face judgement for LIGHTNING; (needs anything but TWO to NINE of \u2660, or else they suffer {lightning_damage} points of lightning damage)! If no hit, LIGHTNING will pass onto the next player!")
                negated = check_negate_loop(
                    players, pending_judgement, self, self)
                if negated:
                    move_lightning = True
                if not negated:
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    self.check_envy_of_heaven()
                    print(
                        f"  >> Judgement: {self.character} flipped a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, self)

                    # IF JUDGEMENT OCCURS AND HITS PLAYER!
                    if (judgement_card.suit == "\u2660") and (10 > judgement_card.rank > 1):
                        print(
                            f"{self.character}'s judgement card is a {judgement_card}, and therefore {pending_judgement} deals {lightning_damage} damage, then gets discarded!")
                        discard_deck.add_to_top(pending_judgement)
                        damage_dealt = lightning_damage
                        self.current_health -= damage_dealt
                        self.check_evil_hero(pending_judgement)
                        if self.current_health < 1:
                            if self.check_brink_of_death_loop(None) == "Break":
                                return "Break"
                    else:
                        print(
                            f"{self.character}'s judgement card is a {judgement_card}, and therefore {pending_judgement} passes on to the next player!")
                        move_lightning = True

                # JUDGEMENT NEGATED OR OCCURS AND DOESN'T HIT!
                if move_lightning:
                    lightning_passed = False

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
                                        f"{self.character}'s {pending_judgement} passes on to {players[nextp].character}!")
                                    possible_players = 0
                                    lightning_passed = True
                                    break
                        else:
                            players[nextp].pending_judgements.insert(
                                0, pending_judgement)
                            print(
                                f"{self.character}'s {pending_judgement} passes on to {players[nextp].character}!")
                            possible_players = 0
                            lightning_passed = True

                    # OTHERWISE STAYS!
                    if not lightning_passed:
                        print(
                            f"{self.character}: There is no next player; {pending_judgement} stays put!")
                        self.pending_judgements.append(pending_judgement)

            # No more pending_judgements!
            elif (pending_judgement.effect2 == 'Lightning') and (self.lightning_immunity == True):
                self.pending_judgements.append(pending_judgement)
                return False

    def reset_once_per_turn(self):
        self.attacks_this_turn = 0
        self.acedia_active = False
        self.lightning_immunity = False
        self.tools_immunity = False
        self.used_trigrams = False

        # Reset Abilities
        self.used_bare_the_chest = False
        self.used_benevolence = False
        self.used_dual_heroes = False
        self.used_ferocious_assault = False
        self.used_green_salve = False
        self.used_marriage = False
        self.used_reconsider = False
        self.used_seed_of_animosity = False
        self.used_sow_dissension = False

        self.escort_requested = False
        self.rouse_requested = False

    # Equipment Checks
    def check_armor_black_shield(self, card):
        # 'card' refers to the ATTACK card used against the defending-player
        armor = False
        for i_index, i in enumerate(self.equipment):
            if i.effect == "Black Shield":
                armor_index = i_index
                armor = True
                break

        if armor:
            if card.suit == "\u2660" or card.suit == "\u2663":
                print(
                    f"  >> {self.character} has {self.equipment[armor_index]} equipped, and therefore CANNOT be affected by black ATTACK cards ({card} discarded as normal).")
                return True
        return False

    def check_armor_eight_trigrams(self):
        if self.used_trigrams:
            return False

        armor = False
        for i_index, i in enumerate(self.equipment):
            if i.effect == "Eight-Trigrams":
                armor_index = i_index
                armor = True
                break

        if armor:
            print(
                f"  >> {self.character} chose to activate their equipped {self.equipment[armor_index]} (armor); needs \u2665 or \u2666 to automatically dodge.")
            main_deck.discard_from_deck()
            judgement_card = discard_deck.contents[0]
            self.check_envy_of_heaven()
            print(
                f"  >> Judgement: {self.character} flipped a {judgement_card}.")
            judgement_card = check_judgement_tinkering(judgement_card, self)
            if judgement_card.suit == "\u2665" or judgement_card.suit == "\u2666":
                judgement_card.effect2 = "Defend"
                return judgement_card
            else:
                self.used_trigrams = True
                return False
        return False

    def check_weapon_axe(self, target):
        # 'target' refers to the target of the initial ATTACK card.
        weapon = False
        for i in self.equipment:
            if i.effect == "Axe":
                total_cards = self.hand.contents + self.equipment
                if len(total_cards) > 2:
                    weapon = True
                    break

        if weapon:
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                total_cards.remove(i)
                card = self.discard("Handquip")
                card2 = self.discard("Handquip")

                damage_dealt = 1
                if self.used_bare_the_chest:
                    damage_dealt += 1
                target.current_health -= damage_dealt
                print(
                    f"  >> {self.character} has forced the damage to {target.character}, by using their {i}, and discarding two cards ({target.current_health}/{target.max_health} HP remaining).")
                self.check_one_after_another()
                for player in players:
                    if player.current_health < 1:
                        player.check_brink_of_death_loop(self)
                target.check_bequeathed_strategy(damage_dealt)
                target.check_evil_hero(card, card2)
                target.check_eye_for_an_eye(self)
                target.check_retaliation(self, damage_dealt)
                return True

    def check_weapon_black_pommel(self):
        for i in self.equipment:
            if i.effect == "Black Pommel":
                return True

    def check_weapon_frost_blade(self, target):
        # 'target' refers to the target of the initial ATTACK card.
        weapon = False
        for i_index, i in enumerate(self.equipment):
            if i.effect == "Frost Blade":
                weapon_index = i_index
                weapon = True
                break

        if weapon:
            total_cards = target.hand.contents + target.equipment
            if len(total_cards) > 0:
                choices = [True, False]
                activated = random.choice(choices)
                if activated:
                    print(
                        f"{self.character} has {self.equipment[weapon_index]} equipped, and chose to make {target.character} discard two cards instead of taking damage.")
                    if len(total_cards) > 1:
                        total_cards = 2
                    else:
                        total_cards = 1
                    while total_cards > 0:
                        card = target.discard("Handquip")
                        print(
                            f"  >> {self.character} has forced {target.character} to discard {card}!")
                        total_cards -= 1

                    target.check_one_after_another()
                    return True
        return False

    def check_weapon_gender_swords(self, target):
        # 'target' refers to the target of the initial ATTACK card.
        weapon = False
        for i_index, i in enumerate(self.equipment):
            if i.effect == "Gender-Swords":
                weapon_index = i_index
                weapon = True
                break

        if weapon:
            if self.gender != target.gender:
                if len(target.hand.contents) > 0:
                    choices = ["Draw", "Discard"]
                    choice = random.choice(choices)
                    if choice == "Draw":
                        self.draw(main_deck, 1, False)
                        print(
                            f"  >> {self.character} draws a card after attacking with {self.equipment[weapon_index]}.")
                    if choice == "Discard":
                        card = target.discard()
                        target.check_one_after_another()
                        print(
                            f"  >> {target.character} discards {card} after being attacked by {self.equipment[weapon_index]}.")
                else:
                    self.draw(main_deck, 1, False)
                    print(
                        f"  >> {self.character} draws a card after attacking with {self.equipment[weapon_index]}.")

    def check_weapon_green_dragon_halberd(self, target):
        # 'target' refers to the target of the initial ATTACK card.
        weapon = False
        for i_index, i in enumerate(self.equipment):
            if i.effect == "Green Dragon Halberd":
                weapon_index = i_index
                weapon = True
                break

        if weapon:
            possible_cards = []
            for i in self.hand.contents:
                if i.effect == "Attack":
                    possible_cards.append(i)

            if len(possible_cards) > 0:
                choices = [True, False]
                activated = random.choice(choices)
                if activated:
                    card = random.choice(possible_cards)
                    self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                    self.check_one_after_another()
                    card.effect2 = "Attack"
                    print(
                        f"  >> {self.character} attacked {target.character} again with {card}, using {self.equipment[weapon_index]}!")
                    self.activate_attack(card, target)
                    return True

    def check_weapon_huangs_longbow(self, target):
        # 'target' refers to the target of the initial ATTACK card.
        weapon = False
        for i_index, i in enumerate(self.equipment):
            if i.effect == "Huang's Longbow":
                weapon_index = i_index
                weapon = True
                break

        if (weapon) and (target in players):
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                choices = []
                for i2 in target.equipment:
                    if i2.ctype == "-1 Horse" or i2.ctype == "+1 Horse":
                        choices.append(i2)
                if len(choices) < 1:
                    return False
                else:
                    horse_slain = random.choice(choices)
                    target.equipment.remove(horse_slain)
                    discard_deck.add_to_top(horse_slain)
                    print(
                        f"  >> {self.character} has {self.equipment[weapon_index]} equipped, and therefore slays {horse_slain} of {target.character}!")
                    target.check_warrior_woman()
                    return True

    def check_weapon_serpent_spear(self):
        weapon = False
        for i_index, i in enumerate(self.equipment):
            if i.effect == "Serpent Spear":
                weapon_index = i_index
                weapon = True
                break

        if (weapon) and (len(self.hand.contents) > 1):
            card = self.discard()
            card2 = self.discard()
            if (card.suit == "\u2660" or card.suit == "\u2663") and (card2.suit == "\u2660" or card2.suit == "\u2663"):
                card.effect2 = "Black Attack"
                card2.effect2 = "Black Attack"
            elif (card.suit == "\u2665" or card.suit == "\u2666") and (card2.suit == "\u2665" or card2.suit == "\u2666"):
                card.effect2 = "Red Attack"
                card2.effect2 = "Red Attack"
            else:
                card.effect2 = "Colourless Attack"
                card.effect2 = "Colourless Attack"
            print(
                f"  >> {self.character} discarded two cards ({card}/{card2} to use as an ATTACK via {self.equipment[weapon_index]}!")
            self.check_one_after_another()
            return [card, card2]

    def check_weapon_sky_scorcher_halberd(self, target):
        # 'target' refers to the target of the initial ATTACK card. They cannot be hit again via this weapon's effect!
        weapon = False
        if len(self.hand.contents) == 0:
            for i_index, i in enumerate(self.equipment):
                if i.effect == "Sky Scorcher Halberd":
                    weapon_index = i_index
                    weapon = True
                    break

        if weapon:
            print(
                f"  >> {self.character} has used their last hand-card to ATTACK {target.character} with {self.equipment[weapon_index]}. They can target up to two extra players!")
            targets = self.calculate_targets_in_weapon_range()
            targets.remove(target)
            if len(targets) < 1:
                return 0

            else:
                targets.append("No more!")
                target2 = random.choice(targets)
                if target2 == "No more!":
                    return 0
                targets.remove(target2)
                if len(targets) < 1:
                    return [True, target2]

                else:
                    target3 = random.choice(targets)
                    if target3 == "No more!":
                        return [True, target2]
                    return [True, target2, target3]
        return 0

    def check_weapon_zhuge_crossbow(self):
        for i_index, i in enumerate(self.equipment):
            if i.effect == "Zhuge Crossbow":
                print(
                    f"  >> {self.character} has {self.equipment[i_index]} equipped, and therefore has no limit to the amount of attacks per turn.")
                return True

    # Character Ability Checks
    def check_astrology(self):
        # "Astrology: Before your judgement phase, you can view the top X cards of the deck (X being the number of players still in play, with a maximum of five). Of these X cards, you can rearrange the order of the cards, and choose any number to place at the top or bottom of the draw-deck."
        if "Astrology" in self.char_abils:
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                cards_viewed = len(players)
                if cards_viewed > 4:
                    cards_viewed = 5
                astrology = Player()
                astrology.draw(main_deck, cards_viewed, False)

                top = 0
                bottom = 0
                for i in range(cards_viewed):
                    card = random.choice(astrology.hand.contents)
                    astrology.hand.contents.remove(card)
                    choices = ["Top", "Bottom"]
                    new_location = random.choice(choices)
                    if new_location == "Top":
                        main_deck.add_to_top(card)
                        top += 1
                    else:
                        main_deck.add_to_bottom(card)
                        bottom += 1

                print(
                    f"  >> Character Ability: Astrology; {self.character} has rearranged the top {cards_viewed} of the deck; {top} to the top, {bottom} to the bottom!")

    def check_bare_the_chest(self):
        # "Bare the Chest: You can choose to draw one less card in your drawing phase. If you do so, any ATTACK or DUEL cards that you you play in your action phase will deal an additional unit of damage."
        if "Bare the Chest" in self.char_abils:
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                print(
                    f"  >> Character Ability: Bare the Chest; {self.character} has activated Bare the Chest, drawing one card only, and all their ATTACK and DUEL cards will do increased damage for this turn.")
                self.used_bare_the_chest = True
                return True

    def check_benevolence(self):
        # "Benevolence: You can give any number of your hand-cards to any players. If you give away more than one card, you recovers one unit of health."
        if ("Benevolence" in self.char_abils) and (self.used_benevolence == False):
            total_cards = len(self.hand.contents)
            if total_cards > 0:
                self.used_benevolence = True
                target = random.choice(players[1:])
                cards_given = random.randint(1, total_cards)
                for i in range(cards_given):
                    card = random.choice(self.hand.contents)
                    self.hand.contents.remove(card)
                    target.hand.add_to_top(card)
                print(
                    f"  >> Character Ability: Benevolence; {self.character} has given {cards_given} card(s) to {target.character}!")
                if (cards_given > 1) and (self.max_health > self.current_health):
                    self.current_health += 1
                    print(
                        f"  >> Character Ability: Benevolence; {self.character} recovers one unit of health ({self.current_health}/{self.max_health} HP remaining)!")

    def check_bequeathed_strategy(self, damage):
        # --- "Bequeathed Strategy: For every one unit of damage you recieve, you can draw two cards from the deck. You can then choose to give away one, two or none of these cards to any player."
        # 'damage' refers to the amount of units of damage dealt (the amount of times this ability activates)
        if ("Bequeathed Strategy" in self.char_abils) and (self in players):
            for i in range(damage):
                choices = [True, False]
                activated = random.choice(choices)
                if activated:
                    beq_strat = Player()
                    beq_strat.draw(main_deck, 2, False)
                    cards_to_dist = random.choice([0, 1, 2])
                    target = random.choice(players)
                    if cards_to_dist == 0:
                        print(
                            f"  >> Character Ability: Bequeathed Strategy; {self.character} drew two cards!")
                    elif cards_to_dist == 1:
                        print(
                            f"  >> Character Ability: Bequeathed Strategy; {self.character} drew two cards, and gave a card to {target.character}!")
                    elif cards_to_dist == 2:
                        print(
                            f"  >> Character Ability: Bequeathed Strategy; {self.character} drew two cards, gave two cards to {target.character}!")
                    while cards_to_dist > 0:
                        card = random.choice(beq_strat.hand.contents)
                        beq_strat.hand.contents.remove(card)
                        target.hand.add_to_top(card)
                        cards_to_dist -= 1
                    while len(beq_strat.hand.contents) > 0:
                        self.hand.add_to_top(beq_strat.hand.contents.pop())

    def check_berserk(self):
        # "Berserk: There is no limit on how many times you can ATTACK during your turn."
        if "Berserk" in self.char_abils:
            print(
                f"  >> Character Ability: Berserk; {self.character} has no limit to the amount of attacks they can play.")
            return True

    def check_bloodline(self):
        # "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive."
        limit_increase = 0
        if ((self.role == "Emperor") or ("False Ruler" in self.char_abils)):
            if ("Bloodline (Ruler Ability)" in self.char_abils):
                heroes = []
                for player in players:
                    if player.allegiance == 'Heroes':
                        heroes.append("1")
                limit_increase = ((len(heroes)-1)*2)
                if limit_increase > 0:
                    print(
                        f"  >> Ruler Ability: Bloodline; {self.character}'s hand limit is increased by {limit_increase} (two for every other HERO character still alive).")
        return limit_increase

    def check_dashing_hero(self):
        # "Dashing Hero: Draw an extra card at the start of your turn."
        if "Dashing Hero" in self.char_abils:
            print(
                f"  >> Character Ability: Dashing Hero; {self.character} draws an extra card from the deck (total of 3) in their drawing phase.")
            return True

    def check_devil(self, judgement_card):
        # --- "Devil: After any judgement has been flipped over, you can immediately discard one of your on-hand or equipped cards to replace the judgement card."
        # 'judgement_card' refers to the card that is currently applying for the judgement taking place
        if "Devil" in self.char_abils:
            total_cards = self.hand.contents + self.equipment
            if len(total_cards) > 0:
                choices = [True, False]
                activated = random.choice(choices)
                if activated:
                    new_judgement_card = self.discard("Handquip")
                    print(
                        f"  >> Character Ability: Devil; {self.character} has replaced the judgement card: {judgement_card} with {new_judgement_card}!")
                    return new_judgement_card
        return judgement_card

    def check_displacement(self, source):
        # --- "Displacement: Whenever you become the target of an ATTACK, you can discard any card to divert the ATTACK to any player within your attacking range. This effect cannot be used against the player that played the ATTACK card."
        # 'source' refers to the source of the ATTACK
        if "Displacement" in self.char_abils:
            targets = self.calculate_targets_in_weapon_range(0, source)
            if (len(targets) > 0) and ((len(self.hand.contents) + len(self.equipment)) > 0):
                choices = [True, False]
                activated = random.choice(choices)
                if activated:
                    card = self.discard("Handquip")
                    target = random.choice(targets)
                    print(
                        f"  >> Character Ability: Displacement; {self.character} has discarded {card} to redirect the ATTACK to {target.character}.")
                    return target
        return self

    def check_dragon_heart_atk_to_def(self, card):
        # --- "Dragon Heart: Your ATTACK and DEFEND cards can be used interchangeably."
        # 'card' refers to the card used as an ATTACK
        if "Dragon Heart" in self.char_abils:
            if card.effect == "Attack":
                card.effect2 = "Defend"
                print(
                    f"  >> Character Ability: Dragon Heart; {self.character} used {card} as a DEFEND!")
                return True

    def check_dragon_heart_def_to_atk(self, card):
        # "Dragon Heart: Your ATTACK and DEFEND cards can be used interchangeably."
        # 'card' refers to the card used as a DEFEND
        if "Dragon Heart" in self.char_abils:
            if card.effect == "Defend":
                card.effect2 = "Attack"
                print(
                    f"  >> Character Ability: Dragon Heart; {self.character} used {card} as an ATTACK!")
                return True

    def check_dual_heroes(self):
        # "Dual Heroes: At the beginning of your turn, you can choose to forgo your drawing phase and instead flip a judgement. Unlike usual judgement cards, this card will be added to your hand. Note the colour of the suit of this judgement card. For the rest of your action phase, you can choose to use any on-hand card with a different colour suit from this judgement card as a DUEL."
        if "Dual Heroes" in self.char_abils:
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                print(
                    f"  >> Character Ability: Dual Heroes; {self.character} have activated Dual Heroes, flipping a judgement, then adding it to their hand.")
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(
                    f"  >> Judgement: {self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(
                    judgement_card, self)
                self.draw(discard_deck, 1, False)

                if judgement_card.suit == "\u2660" or judgement_card.suit == "\u2663":
                    self.used_dual_heroes = "Red"
                    print(
                        f"  >> Character Ability: Dual Heroes; {self.character} drew {judgement_card} and can use any on-hand red cards as DUEL!")
                    return True

                if judgement_card.suit == "\u2665" or judgement_card.suit == "\u2666":
                    self.used_dual_heroes = "Black"
                    print(
                        f"  >> Character Ability: Dual Heroes; {self.character} drew {judgement_card} and can use any on-hand black cards as DUEL!")
                    return True

    def check_eclipse_the_moon(self):
        # "Eclipse the Moon: At the end of your turn, you may draw an additional card from the deck."
        if "Eclipse the Moon" in self.char_abils:
            print(
                f"  >> Character Ability: Eclipse the Moon; {self.character} draws an extra card from the deck in their end-phase.")
            self.draw(main_deck, 1, False)

    def check_empty_city(self):
        # "Empty City: When you have no hand-cards, you cannot become the target of an ATTACK or a DUEL."
        if "Empty City" in self.char_abils:
            if len(self.hand.contents) == 0:
                print(
                    f"  >> Character Ability; Empty City: {self.character} has no hand-cards, and therefore cannot be targeted by ATTACK or DUEL.")
                return True

    def check_envy_of_heaven(self):
        # "Envy of Heaven: You can obtain any judgement card that you flip over."
        if "Envy of Heaven" in self.char_abils:
            print(
                f"  >> Character Ability: Envy of Heaven; The top judgement card has been added to {self.character}'s hand before it takes effect.")
            self.draw(discard_deck, 1, False)

    def check_escort(self):
        # "Escort (Ruler Ability): If you need to use a DEFEND, you can ask any member of Wei to play it on your behalf."
        if ("Escort (Ruler Ability)" in self.char_abils) and ((self.role == "Emperor") or ("False Ruler" in self.char_abils)):
            targets = []
            for player in players:
                if (player != self) and (player.allegiance == "Wei"):
                    if (player.escort_requested == False):
                        targets.append(player)
            if len(targets) > 0:
                target = random.choice(targets)
                card = target.use_reaction_effect("Escort Defend", None, self)
                if type(card) == Card:
                    if (card.effect == "Defend") or (card.effect2 == "Defend"):
                        print(
                            f"  >> Ruler Ability: Escort; {target.character} played a DEFEND ({card}) on behalf of {self.character}!")
                        return card
                print(
                    f"  >> Ruler Ability: Escort; {target.character} did not play a DEFEND on behalf of {self.character}!")
                target.escort_requested = True
        return "Repeat"

    def check_evil_hero(self, card, card2=None):
        # --- "Evil Hero: Whenever you are damaged by a card, you can immediately add it to your hand."
        # 'card' refers to the card that damaged the player
        # 'card2' refers to the any secondary card (if applicable) that damaged the player
        if ("Evil Hero" in self.char_abils) and (self in players):
            if card in discard_deck.contents:
                discard_deck.contents.remove(card)
                self.hand.add_to_top(card)
                print(
                    f"  >> Character Ability: Evil Hero; {self.character} immediately draws {card} after taking damage from it.")
            elif card in main_deck.contents:
                main_deck.contents.remove(card)
                self.hand.add_to_top(card)
                print(
                    f"  >> Character Ability: Evil Hero; {self.character} immediately draws {card} after taking damage from it.")

            if card2 != None:
                if card2 in discard_deck.contents:
                    discard_deck.contents.remove(card2)
                    self.hand.add_to_top(card2)
                    print(
                        f"  >> Character Ability: Evil Hero; {self.character} immediately draws {card2} after taking damage from it.")
                elif card2 in main_deck.contents:
                    main_deck.contents.remove(card2)
                    self.hand.add_to_top(card2)
                    print(
                        f"  >> Character Ability: Evil Hero; {self.character} immediately draws {card2} after taking damage from it.")

    def check_eye_for_an_eye(self, source):
        # --- "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not \u2665, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards."
        # 'source' refers to the person who damaged the user of this ability
        if ("Eye for an Eye" in self.char_abils) and (self in players) and (source in players):
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                print(
                    f"  >> Character Ability: Eye for an Eye; {self.character} is forcing a judgement card to be flipped. If not \u2665, {source.character} must either take one damage or discard two hand-cards.")
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(
                    f"  >> Judgement: {self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(
                    judgement_card, self)

                if (judgement_card.suit == "\u2665"):
                    print(
                        f"  >> Character Ability: Eye for an Eye; {self.character}'s judgement card is a {judgement_card} and therefore has no effect.")
                else:
                    choices = ["Health"]
                    if len(source.hand.contents) > 1:
                        choices.append("Cards")
                    activated = random.choice(choices)
                    if activated == "Health":
                        source.current_health -= 1
                        print(
                            f"  >> Character Ability: Eye for an Eye; {source.character} has lost one health ({source.current_health}/{source.max_health} HP remaining)!")
                        source.check_brink_of_death_loop(self)
                        source.check_bequeathed_strategy(1)
                        source.check_retaliation(self, 1)
                    elif activated == "Cards":
                        card = source.discard()
                        card2 = source.discard()
                        print(
                            f"  >> Character Ability: Eye for an Eye; {source.character} has been forced to discard {card} and {card2}!")
                        source.check_one_after_another()

    def check_false_ruler(self):
        # "False Ruler: You possess the same ruler ability as the current emperor."
        if "False Ruler" in self.char_abils:
            for player in players:
                if player.role == 'Emperor':
                    if player.character == "Liu Bei":
                        self.char_abils.append(
                            "Rouse (Ruler Ability): If you need to use an ATTACK, you can ask any member of Shu to play it on your behalf.")
                    elif player.character == "Cao Cao":
                        self.char_abils.append(
                            "Escort (Ruler Ability): If you need to use a DEFEND, you can ask any member of Wei to play it on your behalf.")
                    elif player.character == "Sun Quan":
                        self.char_abils.append(
                            "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health.")
                    elif player.character == "Yuan Shao":
                        self.char_abils.append(
                            "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive.")

    def check_fearsome_advance(self, target):
        # --- "Fearsome Advance: Whenever your ATTACK is evaded by a DEFEND, you can discard one of your opponents cards (on-hand or equipped)."
        # 'target' refers to the target of the ATTACK effect
        if "Fearsome Advance" in self.char_abils:
            total_cards = target.hand.contents + target.equipment
            if len(total_cards) > 0:
                choices = [True, False]
                activated = random.choice(choices)
                if activated:
                    card = target.discard("Handquip")
                    print(
                        f"  >> Character Ability: Fearsome Advance; {self.character} has made {target.character} discard a card: {card}!")

    def check_fearsome_archer(self, card, card2=None, target=None):
        # --- "Fearsome Archer: During your action phase, your ATTACK cards cannot be evaded by a DEFEND under the following two conditions: the number of on-hand cards of the target player is less than or equal to your attacking range; or the number of on-hand cards of the target player is more than or equal to the units of health you have remaining."
        # 'card' refers to the card that caused the ATTACK effect
        # 'card2' refers to the secondary card (if applicable) that caused the ATTACK effect (eg. via Serpent Spear)
        # 'target' refers to the target of the ATTACK effect
        if "Fearsome Archer" in self.char_abils:
            if self != players[0]:

                modifier = 0
                weapon_range = 1
                if self.check_horsemanship():
                    modifier += 1
                for i in self.equipment:
                    if i.ctype == "-1 Horse":
                        modifier += 1
                    if i.ctype == "Weapon":
                        weapon_range = i.weapon_range
                total_range = weapon_range + modifier

                if (len(target.hand.contents) <= total_range) or (len(target.hand.contents) >= self.current_health):
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        if self.check_weapon_frost_blade(target):
                            return True

                        damage_dealt = 1
                        target.current_health -= damage_dealt
                        print(
                            f"  >> Character Ability: Fearsome Archer; {self.character} attacked {target.character} with an undodgable ATTACK, dealing {damage_dealt} damage. ({target.current_health}/{target.max_health} HP remaining).")
                        self.check_weapon_huangs_longbow(target)
                        for player in players:
                            if player.current_health < 1:
                                player.check_brink_of_death_loop(self)

                        target.check_bequeathed_strategy(damage_dealt)
                        target.check_evil_hero(card, card2)
                        target.check_eye_for_an_eye(self)
                        target.check_retaliation(self, damage_dealt)
                        return True

    def check_ferocious_assault(self):
        # "Ferocious Assault: During your action phase, you can inflict one unit of damage to any player within your attacking range by either; reducing one unit of your own health, or discarding one weapon card (on-hand or equipped). Limited to one use per turn."
        if ("Ferocious Assault" in self.char_abils) and (self.used_ferocious_assault == False):
            weapon_targets = self.calculate_targets_in_weapon_range()
            if len(weapon_targets) > 0:
                total_cards = self.hand.contents + self.equipment
                choices = ["Health"]
                possible_weapons = []
                for i in total_cards:
                    if i.ctype == "Weapon":
                        if "Weapon" not in choices:
                            choices.append("Weapon")
                        possible_weapons.append(i)

                mode = random.choice(choices)
                target = random.choice(players[1:])
                if mode == "Health":
                    print(
                        f"  >> Character Ability: Ferocious Assault; {self.character} has lost 1 health to damage {target.character} ({target.current_health - 1}/{target.max_health} HP remaining)!")
                    self.current_health -= 1
                    self.check_brink_of_death_loop(None)

                elif mode == "Weapon":
                    weapon = random.choice(possible_weapons)
                    if weapon in self.equipment:
                        self.equipment.remove(weapon)
                    else:
                        self.hand.contents.remove(weapon)
                    discard_deck.add_to_top(weapon)
                    print(
                        f"  >> Character Ability: Ferocious Assault; {self.character} has discarded {weapon} to damage {target.character} ({target.current_health - 1}/{target.max_health} HP remaining)!")

                if check_win_conditions():
                    return False
                target.current_health -= 1
                target.check_brink_of_death_loop(self)
                target.check_bequeathed_strategy(1)
                target.check_eye_for_an_eye(self)
                target.check_retaliation(self, 1)
                self.used_ferocious_assault = True

    def check_first_aid(self, card):
        # "First Aid: Outside of your turn, you can use any red-suited cards (on-hand or equipped) as a PEACH."
        if "First Aid" in self.char_abils:
            if (card.suit == "\u2665") or (card.suit == "\u2666"):
                print(
                    f"  >> Character Ability: First Aid; {self.character} used {card} as a PEACH!")
                card.effect2 = "Peach"
            return True

    def check_goddess_luo(self):
        # "Goddess Luo: At the beginning of your turn, you flip a judgement card. If the judgement is a black-suited, you may choose to flip another. This process continues until you flip a red-suited card. The red card is discarded and all black-suited cards are added to your hand."
        if "Goddess Luo" in self.char_abils:
            cards_drawn = []
            choices = [True, False]
            activated = random.choice(choices)
            while activated:
                judgement_card = main_deck.remove_from_top()
                print(
                    f"  >> {self.character}'s judgement card is a {judgement_card}.")
                judgement_card = check_judgement_tinkering(
                    judgement_card, self)

                if (judgement_card.suit == "\u2660") or (judgement_card.suit == "\u2663"):
                    cards_drawn.append(judgement_card)
                else:
                    discard_deck.add_to_top(judgement_card)
                    activated = False

            if len(cards_drawn) > 0:
                print(
                    f"  >> Character Ability: Goddess Luo; {self.character} adds {len(cards_drawn)} black card(s) to their hand.")
                for card in cards_drawn:
                    self.hand.contents.append(card)

    def check_green_salve(self):
        # "Green Salve: During your action phase, you can discard any card and allow any player to regain one unit of health. Limited to one use per turn."
        if ("Green Salve" in self.char_abils) and (self.used_green_salve == False):
            targets = []
            for player in players:
                if player.max_health > player.current_health:
                    targets.append(player)
            if (len(targets) > 0) and (len(self.hand.contents) > 0):
                self.used_green_salve = True
                card = self.discard("Handquip")
                target = random.choice(targets)
                target.current_health += 1
                print(
                    f"  >> Character Ability: Green Salve; {self.character} has used {card} to heal {target.character} by one ({target.current_health}/{target.max_health} HP remaining)!")

    def check_horsemanship(self):
        # "Horsemanship: You will always be -1 distance in any range calculations."
        if "Horsemanship" in self.char_abils:
            return True

    def check_humility(self):
        # "Humility: You cannot become the target of STEAL or ACEDIA."
        if "Humility" in self.char_abils:
            return True

    def check_impetus(self, card):
        # "Impetus: Every one of your black-suited on-hand cards may be used as DEFEND."
        if "Impetus" in self.char_abils:
            if (card.suit == "\u2660") or (card.suit == "\u2663"):
                print(
                    f"  >> Character Ability: Impetus; {self.character} used {card} as DEFEND!")
                card.effect2 = "Defend"
                return True

    def check_iron_cavalry(self, card, card2=None, target=None):
        # --- "Iron Cavalry: Whenever you ATTACK a player, you can flip a judgement card. If it is red, the ATTACK cannot be dodged."
        # 'card' refers to the card that caused the ATTACK effect
        # 'card2' refers to the secondary card (if applicable) that caused the ATTACK effect (eg. via Serpent Spear)
        # 'target' refers to the target of the ATTACK effect
        if "Iron Cavalry" in self.char_abils:
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                print(
                    f"  >> Character Ability: Iron Cavalry; {self.character} has activated Iron Cavalry, forcing a judgement card to be flipped. If red, {target.character} cannot dodge the attack.")
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(
                    f"  >> Judgement: {self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(
                    judgement_card, self)

                if (judgement_card.suit == "\u2665") or (judgement_card.suit == "\u2666"):
                    if self.check_weapon_frost_blade(target):
                        return "Break"

                    damage_dealt = 1
                    print(f"{self.character}'s judgement card is a {judgement_card} and therefore the ATTACK cannot be dodged, dealing {damage_dealt} damage to {target.character}. ({target.current_health}/{target.max_health} HP remaining).")
                    self.check_weapon_huangs_longbow(target)
                    for player in players:
                        if player.current_health < 1:
                            player.check_brink_of_death_loop(self)

                    target.check_bequeathed_strategy(damage_dealt)
                    target.check_evil_hero(card, card2)
                    target.check_eye_for_an_eye(self)
                    target.check_retaliation(self, damage_dealt)

                else:
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and Iron Cavalry has no effect.")

    def check_marriage(self):
        # "Marriage: During your action phase, you can choose to discard two on-hand cards and pick any male character that is not at full-health. By doing so, both the male character and yourself will recover one unit of health. Limited to one use per turn."
        if ("Marriage" in self.char_abils) and (self.used_marriage == False):
            targets = []
            for player in players:
                if (player.gender == "Male") and (player.max_health > player.current_health):
                    targets.append(player)
            if (len(targets) > 0) and (len(self.hand.contents) > 1):
                self.used_marriage = True
                target = random.choice(targets)
                card = self.discard()
                card2 = self.discard()
                if self.max_health > self.current_health:
                    self.current_health += 1
                    target.current_health += 1
                    print(
                        f"  >> Character Ability: Marriage; {self.character} ({self.current_health}/{self.max_health} HP remaining) has healed both themselves and {target.character} ({target.current_health}/{target.max_health} HP remaining) by discarding {card}/{card2}!")
                else:
                    target.current_health += 1
                    print(
                        f"  >> Character Ability: Marriage; {self.character} has healed {target.character} ({target.current_health}/{target.max_health} HP remaining) by discarding {card}/{card2}!")

    def check_mediocrity_draw(self):
        # "Mediocrity: During your drawing phase, you draw an extra X cards, X being the total number of allegiances still in play. During your discard phase, you must discard at least as many card as there are allegiances still in play. If you have less cards than there are allegiances, you must discard all of them."
        if "Mediocrity" in self.char_abils:
            print(
                f"  >> Character Ability: Mediocrity; {self.character} draws {check_allegiances_in_play()} extra card(s) (one for every allegiance still in play)!")
            return True

    def check_mediocrity_discard(self):
        # "Mediocrity: During your drawing phase, you draw an extra X cards, X being the total number of allegiances still in play. During your discard phase, you must discard at least as many card as there are allegiances still in play. If you have less cards than there are allegiances, you must discard all of them."
        if "Mediocrity" in self.char_abils:
            allegiances = check_allegiances_in_play()
            print(
                f"  >> Character Ability: Mediocrity; {self.character} discards at least {allegiances} cards (one for every allegiance in play) - and then down to their health-level ({self.current_health}/{self.max_health} HP remaining).")
            total_cards = self.hand.contents + self.equipment
            if allegiances >= len(total_cards):
                self.discard_all_cards()
                return True
            else:
                difference = (allegiances - len(total_cards))
                if difference > 0:
                    self.discard("Handquip", difference)
                return True
        return False

    def check_national_colours(self, card):
        # --- "National Colours: During your action phase, you can use any of your cards (on-hand or equipped) with a \u2666 suit as ACEDIA."
        # 'card' refers to the card being used as an ACEDIA
        if "National Colours" in self.char_abils:
            print(
                f"  >> Character Ability: National Colours; {self.character} has attempted to use {card} as ACEDIA.")
            card.effect2 = "Acedia"
            return True

    def check_one_after_another(self):
        # "One After Another: Whenever you use or lose your last on-hand card, you can immediately draw one card from the deck."
        if "One After Another" in self.char_abils:
            if len(self.hand.contents) == 0:
                print(
                    f"  >> Character Ability: One After Another; {self.character} draws a card whenever they use or lose their last on-hand card.")
                self.draw(main_deck, 1, False)

    def check_raid(self):
        # "Raid: In your drawing phase, you can choose to forgo drawing cards from the deck and, instead, draw one on-hand card from a maximum of two other players."
        if "Raid" in self.char_abils:
            targets = []
            for player in players[1:]:
                if len(player.hand.contents) > 0:
                    targets.append(player)

            if len(targets) > 0:
                choices = [True, False]
                activated = random.choice(choices)
                if activated:
                    target1 = random.choice(targets)
                    stolen = random.choice(target1.hand.contents)
                    target1.hand.contents.remove(stolen)
                    self.hand.add_to_top(stolen)
                    print(
                        f"  >> Character Ability: Raid; {self.character} stole a card from the hand of {target1.character}!")
                    target1.check_one_after_another()
                    targets.remove(target1)

                    if len(targets) > 0:
                        choices = [True, False]
                        activated = random.choice(choices)
                        if activated:
                            target2 = random.choice(targets)
                            stolen = random.choice(target2.hand.contents)
                            target2.hand.contents.remove(stolen)
                            self.hand.add_to_top(stolen)
                            print(
                                f"  >> Character Ability: Raid; {self.character} stole a card from the hand of {target2.character}!")
                            target2.check_one_after_another()

                    return True
        return False

    def check_random_strike(self, card, card2):
        # --- "Random Strike: You can use any two hand-cards which have the same suit as RAIN OF ARROWS."
        # 'card' refers to the first card being used as RAIN OF ARROWS
        # 'card2' refers to the second card being used as RAIN OF ARROWS
        if "Random Strike" in self.char_abils:
            print(
                f"  >> Character Ability: Random Strike; {self.character} used {card}/{card2} as RAIN OF ARROWS!")
            card.effect2 = "Rain of Arrows"
            card2.effect2 = "Rain of Arrows"
            return True

    def check_reckless(self, card):
        # --- "Reckless: Every instance that you suffer damage from a red-suited ATTACK, or a WINE ATTACK, your maximum health limit is reduced by one instead."
        # 'card' refers to the card that caused the ATTACK effect
        if "Reckless" in self.char_abils:
            if (card.suit == "\u2665") or (card.suit == "\u2666"):
                self.max_health -= 1
                if self.current_health > self.max_health:
                    self.current_health -= 1
                print(
                    f"  >> Character Ability: Reckless; {self.character} has taken damage from {card}, and therefore loses a maximum health! ({self.current_health}/{self.max_health} HP remaining).")
                for player in players:
                    if player.current_health < 1:
                        player.check_brink_of_death_loop(self)
                return True

    def check_reconsider(self):
        # "Reconsider: You can discard any number of cards to then draw the same number. Limited to one use per turn."
        if ("Reconsider" in self.char_abils) and (self.used_reconsider == False):
            total_cards = (self.hand.contents) + (self.equipment)
            amount = len(total_cards)
            if amount > 0:
                self.used_reconsider = True
                cards_changed = random.randint(1, (amount))
                for i in range(cards_changed):
                    card = random.choice(total_cards)
                    total_cards.remove(card)
                    if card in self.equipment:
                        self.equipment.remove(card)
                    else:
                        self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                self.draw(main_deck, cards_changed, False)
                print(
                    f"  >> Character Ability: Reconsider; {self.character} has discarded {cards_changed}, then drew the same amount! ({len(self.hand.contents)} cards total in-hand)")

    def check_rescued(self, healer):
        # --- "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health."
        # 'healer' refers to the player who played the PEACH card
        if ("Rescued (Ruler Ability)" in self.char_abils) and ((self.role == "Emperor") or ("False Ruler" in self.char_abils)):
            if self != healer:
                if healer.allegiance == "Wu":
                    print(
                        f"  >> Ruler Ability: Rescued: {self.character} was saved from the brink of death by a member of Wu, and therefore recovers two health!")
                    return 1
        return 0

    def check_restraint(self):
        # "Restraint: If you did not use any ATTACK cards during your action phase, you can skip your discard phase."
        if "Restraint" in self.char_abils:
            if self.attacks_this_turn == 0:
                print(
                    f"  >> Character Ability: Restraint; {self.character} skips their discard phase ({len(self.hand.contents)} cards total in-hand).")
                return True

    def check_retaliation(self, source, damage):
        # ---"Retaliation: For every one unit of damage you recieve, you can take one card (whether on-hand or equipped) from the player who was the source of that damage."
        # 'source' refers to the source of the damage
        # 'damage' refers to the amount of units of damage dealt (the amount of times this ability activates)
        if ("Retaliation" in self.char_abils) and (self in players) and (source in players):
            total_cards = source.hand.contents + source.equipment
            while (damage > 0) and (len(total_cards) > 0):
                choices = [True, False]
                activated = random.choice(choices)
                if not activated:
                    return False
                if activated:
                    stolen = random.choice(total_cards)
                    if stolen in source.equipment:
                        source.equipment.remove(stolen)
                        self.hand.add_to_top(stolen)
                        print(
                            f"  >> Character Ability: Retaliation; {self.character} took {stolen} from {source.character}!")
                        source.check_warrior_woman()
                    elif stolen in source.hand.contents:
                        source.hand.contents.remove(stolen)
                        self.hand.add_to_top(stolen)
                        print(
                            f"  >> Character Ability: Retaliation; {self.character} took a card from {source.character}!")
                        source.check_one_after_another()
                    damage -= 1

    def check_rouse(self):
        # "Rouse (Ruler Ability): If you need to use an ATTACK, you can ask Sun Shang Xiang or any member of Shu to play it on your behalf."
        if ("Rouse (Ruler Ability)" in self.char_abils) and ((self.role == "Emperor") or ("False Ruler" in self.char_abils)):
            targets = []
            for player in players:
                if (player != self) and (player.allegiance == "Shu"):
                    if (player.rouse_requested == False):
                        targets.append(player)
            if len(targets) > 0:
                target = random.choice(targets)
                card, card2 = target.use_reaction_effect(
                    "Rouse Attack", None, self)
                if type(card) == Card:
                    if (card.effect == "Attack") or (card.effect2 == "Attack") or (card.effect2 == "Black Attack") or (card.effect2 == "Red Attack") or (card.effect2 == "Colourless Attack"):
                        if type(card2) == Card:
                            print(
                                f"  >> Ruler Ability: Rouse; {target.character} played an ATTACK ({card}/{card2}) on behalf of {self.character}!")
                            return card, card2
                        else:
                            print(
                                f"  >> Ruler Ability: Rouse; {target.character} played an ATTACK ({card}) on behalf of {self.character}!")
                            return card, None
                else:
                    print(
                        f"  >> Ruler Ability: Rouse; {target.character} did not play an ATTACK on behalf of {self.character}!")
                    target.rouse_requested = True
        return "Repeat"

    def check_seed_of_animosity(self):
        # "Seed of Animosity: During your action phase, you can discard one card (on-hand or equipped) and select two male characters to undergo a DUEL with eachother. This ability cannot be prevented using NEGATE, and is limited to one use per turn."
        if ("Seed of Animosity" in self.char_abils) and (self.used_seed_of_animosity == False):
            targets = []
            for player in players[1:]:
                if player.gender == "Male":
                    targets.append
            if len(targets) > 1:
                self.used_seed_of_animosity = True
                card = self.discard("Handquip")
                target1 = random.choice(targets)
                targets.remove(target1)
                target2 = random.choice(targets)
                if target2.check_empty_city():
                    print(
                        f"  >> Character Ability: Seed of Animosity; {self.character} has forced {target2.character} to DUEL against {target1.character}!")
                    target2.activate_duel(card, target1)
                else:
                    print(
                        f"  >> Character Ability: Seed of Animosity; {self.character} has forced {target1.character} to DUEL against {target2.character} by discarding {card}!")
                    target1.activate_duel(card, target2)

    def check_sow_dissension(self):
        # "Sow Dissension: During your action phase, you can show an on-hand card and give it to any other player. They must either choose to lose one unit of health or show their entire hand and discard all cards of the same suit as the card you showed them. Limited to one use per turn."
        if ("Sow Dissension" in self.char_abils) and (self.used_sow_dissension == False):
            if len(self.hand.contents) > 0:
                target = random.choice(players[1:])
                card = random.choice(self.hand.contents)
                self.hand.contents.remove(card)
                target.hand.add_to_top(card)
                mode = random.choice(["Cards", "Health"])
                self.used_sow_dissension = True
                if mode == "Cards":
                    print(
                        f"  >> Character Ability: Sow Dissension; {self.character} has given {card} to {target.character}, and they discarded all cards of {card.suit} from their hand!")
                    for i in target.hand.contents:
                        if i.suit == card.suit:
                            target.hand.contents.remove(i)
                            target.hand.contents.insert(0, "Placeholder")
                    while "Placeholder" in target.hand.contents:
                        target.hand.contents.remove("Placeholder")
                    target.check_one_after_another()
                elif mode == "Health":
                    target.current_health -= 1
                    print(
                        f"  >> Character Ability: Sow Dissension; {self.character} has given {card} to {target.character}, making them lose 1 health ({target.current_health}/{target.max_health} HP remaining)!")
                    target.check_brink_of_death_loop(self)
                    target.check_bequeathed_strategy(1)
                    target.check_eye_for_an_eye(self)
                    target.check_retaliation(self, 1)

    def check_surprise(self, card):
        # --- "Surprise: During your action phase, you can use any of your black-suited cards (on-hand or equipped) as DISMANTLE."
        # 'card' refers to the card being used as an DISMANTLE
        if "Surprise" in self.char_abils:
            print(
                f"  >> Character Ability: Surprise; {self.character} has attempted to use {card} as DISMANTLE.")
            card.effect2 = "Dismantle"
            return True

    def check_talent(self):
        # "Talent: You can use tool cards without range restrictions."
        if "Talent" in self.char_abils:
            return True

    def check_trojan_flesh(self):
        # "Trojan Flesh: During your action phase, you can choose to lose one unit of health to draw two more cards from the deck. This ability can be used repeatedly in a turn."
        if "Trojan Flesh" in self.char_abils:
            self.current_health -= 1
            print(
                f"  >> Character Ability: Trojan Flesh; {self.character} lost one health to draw two cards from the deck ({self.current_health}/{self.max_health} HP remaining).")
            if self.current_health < 1:
                if self.current_health < 1:
                    self.check_brink_of_death_loop(None)
            else:
                self.draw(main_deck, 2, False)

    def check_warrior_saint(self, card):
        # "Warrior Saint: You can use any red-suited cards (on-hand or equipped) as an ATTACK."
        # 'card' refers to the card being used as an ATTACK
        if "Warrior Saint" in self.char_abils:
            if (card.suit == "\u2665") or (card.suit == "\u2666"):
                print(
                    f"  >> Character Ability: Warrior Saint; {self.character} has attempted to use {card} as ATTACK.")
                card.effect2 = "Attack"
                return True

    def check_warrior_woman(self):
        # "Warrior Woman: Whenever any equipped card is removed from your equipment, you can immediately draw two cards from the deck."
        if "Warrior Woman" in self.char_abils:
            print(
                f"  >> Character Ability: Warrior Woman; {self.character} immediately draws 2 cards from the deck whenever one of their equipment cards are destroyed/removed/replaced.")
            self.draw(main_deck, 2, False)

    def check_wisdom(self):
        # "Wisdom: Whenever you use a non-delay tool card, you immediately draw a card from the deck."
        if "Wisdom" in self.char_abils:
            print(
                f"  >> Character Ability: Wisdom; {self.character} immediately draws a card from the deck after using a non-delay tool card.")
            self.draw(main_deck, 1, False)

    def check_without_equal(self):
        # "Without Equal: Whenever you use ATTACK, your target has to use two DEFEND cards to successfully evade the attack. During a DUEL, your opponent has to use two ATTACK cards for every one ATTACK card that you use."
        if "Without Equal" in self.char_abils:
            print(
                f"  >> Character Ability: Without Equal; {self.character}'s victim must play two cards for every ATTACK that {self.character} plays!")
            return True

    # --- Game-Phases
    # 1. "Beginning Phase" determines the start of a turn, resetting all "once-per-turn" effects.
    #       In some cases, certain character-abilities can apply here.
    # 2. "Judgement Phase" is where any pending-judgements from Delay-Tool cards apply.
    # 3. "Drawing Phase" is where the player gets to draw 2 cards for their turn.
    #       In some cases, certain character-abilities can alter the number, and possibly cause various effects as a result!
    #       If a player is affected by RATIONS DEPLETED (in their judgement phase), they forfeit their drawing phase.
    # 4. "Action Phase" refers to where a player can use cards and use activatable-character abilities.
    #       If a player is affected by ACEDIA (in their judgement phase), they forfeit their action phase.
    # 5. "Discard Phase" refers to where a player must discard hand-cards, such that they do not exceed their current_health level.
    #       Certain character abilities can alter this behaviour.
    # 6. "End Phase" only applies to some characters. In most cases, nothing happens here.
    def start_beginning_phase(self):
        self.reset_once_per_turn()
        print(
            f"-----------------------------<{self.character} has started their turn!>-----------------------------")
        self.check_astrology()
        self.check_goddess_luo()
        return self.start_judgement_phase()

    def start_judgement_phase(self):
        if self.check_pending_judgements() == "Break":
            return False
        else:
            return self.start_drawing_phase()

    def start_drawing_phase(self):
        if self.check_raid():
            if self.acedia_active:
                return self.start_discard_phase()
            else:
                return self.start_action_phase()

        cards_drawn = 2
        message = True
        if self.check_bare_the_chest():
            cards_drawn -= 1
            message = False
        elif self.check_dashing_hero():
            cards_drawn = 3
            message = False
        elif self.check_dual_heroes():
            cards_drawn = 0
            message = False
        elif self.check_mediocrity_draw():
            cards_drawn += check_allegiances_in_play()
            message = False

        self.draw(main_deck, cards_drawn, message)

        if self.acedia_active:
            return self.start_discard_phase()
        else:
            return self.start_action_phase()

    def start_action_phase(self):
        action_phase_active = True
        while action_phase_active:
            if roles != 0:
                if check_win_conditions():
                    return False

            elif len(players) < 2:
                return False

            if self.current_health < 1:
                return self.start_end_phase()

            actions = self.hand.contents + ["End Action-Phase"]

            # Ability Checks; (adding extra actions!)
            if ("Benevolence" in self.char_abils) and (self.used_benevolence == False):
                actions.append("benevolence")
            elif ("Ferocious Assault" in self.char_abils) and (self.used_ferocious_assault == False):
                targets = self.calculate_targets_in_weapon_range()
                if len(targets) > 0:
                    actions.append("ferocious_assault")
            elif ("Green Salve" in self.char_abils):
                actions.append("green_salve")
            elif ("Marriage" in self.char_abils) and (self.used_marriage == False):
                actions.append("marriage")
            elif ("National Colours" in self.char_abils):
                for i in self.equipment:
                    if i.suit == "\u2666":
                        actions.append(i)
            elif ("Random Strike" in self.char_abils):
                same_cards = {"\u2660": 0, "\u2663": 0,
                              "\u2665": 0, "\u2666": 0}
                suits = []
                for i in self.hand.contents:
                    same_cards[i.suit] += 1
                for suit in same_cards:
                    if same_cards[suit] > 1:
                        suits.append(suit)
            elif ("Reconsider" in self.char_abils):
                actions.append("reconsider")
            elif ("Rouse (Ruler Ability)" in self.char_abils) and ((self.role == "Emperor") or ("False Ruler" in self.char_abils)):
                if (self.attacks_this_turn == 0) or (self.check_weapon_zhuge_crossbow()):
                    targets = []
                    for player in players:
                        if (player != self) and (player.allegiance == "Shu"):
                            if (player.rouse_requested == False):
                                targets.append(player)
                    if len(targets) > 0:
                        targets = self.calculate_targets_in_weapon_range()
                        if len(targets) > 0:
                            actions.append("rouse")
            elif ("Seed of Animosity" in self.char_abils) and (self.used_seed_of_animosity == False):
                actions.append("seed_of_animosity")
            elif ("Sow Dissension" in self.char_abils) and (self.used_sow_dissension == False) and (len(self.hand.contents) > 0):
                actions.append("sow_dissension")
            elif ("Surprise" in self.char_abils):
                for i in self.equipment:
                    if (i.suit == "\u2660") or (i.suit == "\u2663"):
                        actions.append(i)
            elif ("Trojan Flesh" in self.char_abils):
                actions.append("trojan_flesh")
            elif ("Warrior Saint" in self.char_abils):
                for i in self.equipment:
                    if (i.suit == "\u2665") or (i.suit == "\u2666"):
                        actions.append(i)

            # Check for Serpent Spear
            if (serp_spear in self.equipment) and (len(self.hand.contents) > 1):
                actions.append("serp_spear")

            card = random.choice(actions)
            # print(f"Options: {actions}")
            # print(f"Selected: {card}")

            if card == "End Action-Phase":
                if self.check_restraint():
                    return self.start_end_phase()
                else:
                    return self.start_discard_phase()

            elif card == "serp_spear":
                card = self.check_weapon_serpent_spear()
                self.use_card_effect(card[0], card[1])

            elif card == "benevolence":
                self.check_benevolence()

            elif card == "ferocious_assault":
                self.check_ferocious_assault()

            elif card == "green_salve":
                self.check_green_salve()

            elif card == "marriage":
                self.check_marriage()

            elif card == "reconsider":
                self.check_reconsider()

            elif card == "rouse":
                card = self.check_rouse()
                if type(card) == tuple:
                    (card, card2) = card
                if card != "Repeat":
                    for player in players:
                        player.rouse_requested = False
                    if card2 == None:
                        self.use_card_effect(card)
                    else:
                        self.use_card_effect(card, card2)

            elif card == "seed_of_animosity":
                self.check_seed_of_animosity()

            elif card == "sow_dissension":
                self.check_sow_dissension()

            elif card == "trojan_flesh":
                self.check_trojan_flesh()

            else:
                activated = False
                card2 = None

                # Checks for character-specific card-effects
                if (self.used_dual_heroes == "Black") and ((card.suit == "\u2660") or (card.suit == "\u2663")):
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        print(
                            f"  >> Character Ability: Dual Heroes; {self.character} uses {card} as DUEL!")
                        card.effect2 = "Duel"

                elif (self.used_dual_heroes == "Red") and ((card.suit == "\u2665") or (card.suit == "\u2666")):
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        print(
                            f"  >> Character Ability: Dual Heroes; {self.character} uses {card} as DUEL!")
                        card.effect2 = "Duel"

                elif ("Random Strike" in self.char_abils) and (card.suit in suits):
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        possible_cards = []
                        for i in self.hand.contents:
                            if (i != card) and (i.suit == card.suit):
                                possible_cards.append(i)
                        card2 = random.choice(possible_cards)
                        self.check_random_strike(card, card2)

                elif ("National Colours" in self.char_abils) and (card.suit == "\u2666"):
                    if card in self.equipment:
                        activated = True
                        self.check_national_colours(card)
                    else:
                        choices = [True, False]
                        activated = random.choice(choices)
                        if activated:
                            self.check_national_colours(card)

                elif ("Surprise" in self.char_abils) and ((card.suit == "\u2660") or (card.suit == "\u2663")):
                    if card in self.equipment:
                        activated = True
                        self.check_surprise(card)
                    else:
                        choices = [True, False]
                        activated = random.choice(choices)
                        if activated:
                            self.check_surprise(card)

                elif ("Warrior Saint" in self.char_abils) and ((card.suit == "\u2665") or (card.suit == "\u2666")):
                    if card in self.equipment:
                        activated = True
                        self.check_warrior_saint(card)
                    else:
                        choices = [True, False]
                        activated = random.choice(choices)
                        if activated:
                            self.check_warrior_saint(card)

                # Otherwise, use normal card-effect
                if not activated:
                    card.effect2 = card.effect
                self.use_card_effect(card, card2)

    def start_discard_phase(self):
        # Hand-limit abilities
        limit_increase = self.check_bloodline()

        # Unique discarding abilities
        if self.check_mediocrity_discard():
            if len(self.hand.contents) > (self.current_health + limit_increase):
                difference = (len(self.hand.contents) -
                              (self.current_health + limit_increase))
                self.discard("Handquip", difference)
            return self.start_end_phase()

        # Discard down to your current health level
        difference = 0
        if len(self.hand.contents) > (self.current_health + limit_increase):
            difference = (len(self.hand.contents) -
                          (self.current_health + limit_increase))
            self.discard("Hand", difference)
        return self.start_end_phase()

    def start_end_phase(self):
        if (self.current_health > 0) and (self.max_health > 0):
            self.check_eclipse_the_moon()
            print(
                f"------------------------------<{self.character} has ended their turn!>------------------------------")


# --- LOOK HERE TO AUTOPLAY GAMES
# 'num_players' refers to the number of players
# 'iterations' refers to the number of iterations that the game will run
# 'lightning_dmg' refers to the amount of damage a player takes when hit by lightning // 3 by default
# 'mode' refers to whether there are any player roles in-game // 0 = all rebels, 1 = normal roles, 2 = more spies
# 'chars' refers to whether character cards will be used in game // True by default
play_games(num_players=8, num_iterations=5000,
           lightning_dmg=3, mode=1, chars=True)
