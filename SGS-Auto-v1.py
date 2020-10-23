"""
    __________   ___     ____    ___  _________   ___    ___  __________  __________   ___   ___  ___      ___
   / _______//  / ||    /   ||  / // / ______//  / //   / // / _____  // / _______//  / //  / // / ||     / //
  / //_______  /  ||   / /| || / // / // ____   / //   / // / //   / // / //_______  / //__/ // /  ||    / //
 /_______  // / ` ||  / //| ||/ // / // /_  // / //   / // / //   / // /_______  // / ____  // / ` ||   /_//
 _______/ // / /| || / // | |/ // / //___/ // / //___/ // / //___/ //  _______/ // / //  / // / /| ||  ___
/________// /_//|_||/_//  |___// /________// /________// /________//  /________// /_//  /_// /_//| || /_//
                                SanGuoSha Coding by Saba Tazayoni               /||______________| ||
                    Started: 21/07/2020                                        /___________________||
Current Version: 23/10/2020
Version 1.23

 + 23/10/2020 (v1.23);
 - Was very sick for the last week :(
 - Emperor now gets +1 health in games above 4 players!

 TO DO:
 - Greedy Player Mode
 - CSV stuff...
"""
import random


# --- Game-Setup
def generate_players(num, roles):
    # 'num' refers to the number of players you want to generate
    # 'roles' refers to whether the players will be generated with roles (for win-conditions) or not
    global roles_dict

    if num > 10:
        num = 10
    if 3 > num:
        num = 3

    char_names = ["p0", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9"]
    genders = ["Male", "Male", "Male", "Male", "Male",
               "Female", "Female", "Female", "Female", "Female"]
    random.shuffle(genders)

    if roles:
        roles_dict = generate_roles(num)
        roles_list = []
        for key in roles_dict.keys():
            for item in range(0, roles_dict[key]):
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


def generate_deck():
    # The deck! (108 cards total)
    global main_deck
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
        roles_dict = {"Emperor": 1, "Advisor": 1, "Rebel": 3, "Spy": 1}
    elif num == 7:
        roles_dict = {"Emperor": 1, "Advisor": 2, "Rebel": 3, "Spy": 1}
    elif num == 8:
        roles_dict = {"Emperor": 1, "Advisor": 2, "Rebel": 4, "Spy": 1}
    elif num == 9:
        roles_dict = {"Emperor": 1, "Advisor": 3, "Rebel": 4, "Spy": 1}
    else:
        roles_dict = {"Emperor": 1, "Advisor": 3, "Rebel": 4, "Spy": 2}

    return roles_dict


def check_win_conditions():
    if roles_dict["Emperor"] == 1 and roles_dict["Rebel"] == 0 and roles_dict["Spy"] == 0:
        return True

    elif roles_dict["Spy"] == 1 and roles_dict["Emperor"] == 0 and roles_dict["Advisor"] == 0 and roles_dict["Rebel"] == 0:
        return True

    elif roles_dict["Emperor"] == 0:
        return True

    else:
        return False


def play_games(num_players, num_iterations, lightning_dmg=3, roles=True):
    # 'num_players' refers to the number of players
    # 'iterations' refers to the number of iterations that the game will run
    # 'lightning_dmg' refers to the amount of damage a player takes when hit by lightning - 3 by default
    # 'roles' refers to whether there are any player roles in-game - True by default (if False: all players will be considered rebels)
    for i in range(num_iterations):
        global lightning_damage
        global players
        global win_conditions
        global main_deck
        global discard_deck

        if lightning_dmg > 3:
            lightning_dmg = 3
        if lightning_dmg < 0:
            lightning_dmg = 0
        lightning_damage = lightning_dmg

        players = generate_players(num_players, roles)

        if roles:
            win_conditions = "Roles"
            emp_and_co = []
            rebels = []
            for player in players:
                if player.role == "Emperor" or player.role == "Advisor":
                    emp_and_co.append(player)
                elif player.role == "Rebel":
                    rebels.append(player)
        else:
            win_conditions = "Survival"

        main_deck = generate_deck()
        discard_deck = Deck([])
        main_deck.shuffle()

        print(
            f"----------------------------------------<Game {i}: The deck has been shuffled!>----------------------------------------")
        for player in players:
            player.draw(main_deck, 4, False)
        print("All players have been dealt 4 cards!")
        game_started = True
        while game_started:
            if roles and check_win_conditions():
                game_started = False

                if roles_dict["Emperor"] == 1 and roles_dict["Rebel"] == 0 and roles_dict["Spy"] == 0:
                    print(
                        "----------------------------<Emperor and Advisor(s) win!>-----------------------------")
                    for player in emp_and_co:
                        print(f"{player} - {player.role}")

                elif roles_dict["Spy"] == 1 and roles_dict["Emperor"] == 0 and roles_dict["Advisor"] == 0 and roles_dict["Rebel"] == 0:
                    print(
                        "-------------------------------------<Spy wins!>--------------------------------------")
                    for player in players:
                        if player.role == "Spy":
                            print(f"{player} - {player.role}")

                elif roles_dict["Emperor"] == 0:
                    print(
                        "------------------------------------<Rebels win!>-------------------------------------")
                    for player in rebels:
                        print(f"{player} - {player.role}")

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


# --- Loose Functions
def get_player_index(target):
    for player_index, player in enumerate(players):
        if target == player:
            target_index = player_index
            return target_index


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

    def __gt__(self, other):
        return self.rank > other.rank


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
# 1. 'Turn_number' is a counter that will return how many turns this player has had at the end of the game.
# 2. 'Gender' is a PLACEHOLDER for future versions when character-cards are introduced! Currently you get Male/Female at random
# 3. 'Role' is the secret win-condition assigned to each player: Emperor, Advisor, Rebel, Spy
# 4. 'Character' is a PLACEHOLDER for future versions when character-cards are introduced! Currently you get a number only (eg. p5)
# 5. 'Attacks_this_turn' is defaultly set to 0; players can only do 1 ATTACK per turn unless a Zhuge Crossbow is equipped
# 6. 'Current_health' is defaultly set to 4 (this will change in future versions); when a players' health reaches 0, they are on the BRINK OF DEATH!
# 7. 'Max_health' is defaultly set to 4 (this will change in future versions); current_health cannot exceed max_health
# 8. 'Hand' refers to the playing-cards in a players' hand
# 9. 'Equipment' refers to equipped items; only one of each type of equipment can be equipped at one time
# 10. 'Pending_judgements' refers to any Delay-Tool cards that have yet to take effect on a player. These take effect at the start of their turn
# 11. 'Acedia_active' refers to having failed the judgement (above), and missing the action-phase of this turn - False by default
# 12. 'Lightning_immunity' applies when you have already faced judgement (above) for Lightning in this turn - False by default
# 13. 'Tools_immunity' refers to having had a Tool-card negated for an individual player - False by default
# 14. 'Used_trigrams' refers to having used Eight-Trigrams to automatically produce a defend in that single action already - False by default
class Player:
    def __init__(self, gender=None, role="Rebel", character=None):
        self.turn_number = 1
        self.gender = gender
        self.role = role
        self.character = character
        self.attacks_this_turn = 0
        self.current_health = 4
        self.max_health = 4
        self.hand = Hand([])
        self.equipment = []
        self.pending_judgements = []
        self.acedia_active = False
        self.lightning_immunity = False
        self.tools_immunity = False
        self.used_trigrams = False

    def __str__(self):
        equips = ""
        pending = " // Pending: "
        character_details = f"{self.character} // {self.current_health}/{self.max_health} HP remaining"
        for item in self.equipment:
            if item.ctype == "Weapon":
                equips += (f" // W:{item}")
            if item.ctype == "Armor":
                equips += (f" // A:{item}")
            if item.ctype == "-1 Horse":
                equips += (f" // H:{item}")
            if item.ctype == "+1 Horse":
                equips += (f" // H:{item}")
        for item in self.pending_judgements:
            if item.effect2 == "Acedia":
                pending += "[A]"
            if item.effect2 == "Lightning":
                pending += "[L]"
            if item.effect2 == "Rations Depleted":
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
                    f"{num} card has been added to {self.character}'s hand.")
            else:
                print(
                    f"{num} cards have been added to {self.character}'s hand.")
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
                else:
                    self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                num -= 1
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

    # Using Cards/Effects
    def use_card_effect(self, card, card2=None):
        # "Special Attack types":
        if card.effect2 == "Black Attack":
            if (self.attacks_this_turn == 0) or (self.check_weapon_zhuge_crossbow()):
                targets = self.calculate_targets_in_weapon_range()
                if len(targets) < 1:
                    return False
                else:
                    target = players[random.choice(targets)]
                    self.attacks_this_turn += 1
                    if (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card)
                        discard_deck.add_to_top(card)
                    if (card2 != None) and (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card2)
                        discard_deck.add_to_top(card2)
                    print(
                        f"{self.character} has played a BLACK ATTACK against {target.character}.")
                    self.activate_attack(card, target, card2)
                    return True
            else:
                return False

        elif card.effect2 == "Red Attack":
            if (self.attacks_this_turn == 0) or (self.check_weapon_zhuge_crossbow()):
                targets = self.calculate_targets_in_weapon_range()
                if len(targets) < 1:
                    return False
                else:
                    target = players[random.choice(targets)]
                    self.attacks_this_turn += 1
                    if (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card)
                        discard_deck.add_to_top(card)
                    if (card2 != None) and (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card2)
                        discard_deck.add_to_top(card2)
                    print(
                        f"{self.character} has played a RED ATTACK against {target.character}.")
                    self.activate_attack(card, target, card2)
                    return True
            else:
                return False

        elif card.effect2 == "Colourless Attack":
            if (self.attacks_this_turn == 0) or (self.check_weapon_zhuge_crossbow()):
                targets = self.calculate_targets_in_weapon_range()
                if len(targets) < 1:
                    return False
                else:
                    target = players[random.choice(targets)]
                    self.attacks_this_turn += 1
                    if (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card)
                        discard_deck.add_to_top(card)
                    if (card2 != None) and (card not in discard_deck.contents) and (card in self.hand.contents):
                        self.hand.contents.remove(card2)
                        discard_deck.add_to_top(card2)
                    print(
                        f"{self.character} has played a COLOURLESS ATTACK against {target.character}.")
                    self.activate_attack(card, target, card2)
                    return True
            else:
                return False

        # card.ctype == 'Basic':
        elif card.effect2 == "Attack":
            if (self.attacks_this_turn == 0) or (self.check_weapon_zhuge_crossbow()):
                targets = self.calculate_targets_in_weapon_range()
                if len(targets) < 1:
                    return False
                else:
                    target = players[random.choice(targets)]
                    self.attacks_this_turn += 1
                    self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has played {card} against {target.character}.")
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
            return False

        elif card.effect2 == "Peach":
            if self.max_health > self.current_health:
                self.hand.contents.remove(card)
                discard_deck.add_to_top(card)
                self.current_health += 1
                print(
                    f"{self.character} has used a PEACH to heal by one from {self.current_health -1} to {self.current_health}.")
                return True
            else:
                return False

        # card.ctype == 'Tool':
        elif card.effect2 == "Barbarians":
            self.hand.contents.remove(card)
            print(
                f"{self.character} has activated {card}. All players will take one damage (unless playing ATTACK or tool-card negated).")

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

                        for item in players:
                            if item.current_health < 1:
                                item.check_brink_of_death_loop(self)

            discard_deck.add_to_top(card)
            return True

        elif card.effect2 == "Granary":
            self.hand.contents.remove(card)
            print(f"{self.character} has activated {card}. {len(players)} cards have been flipped from the deck. Everyone (unless negated) takes a card; {self.character} goes first!")

            check_aoe_negate_loop(players, card, self, self, card)

            granary = Player()
            granary.draw(main_deck, len(players), False)
            for player in players:
                if not player.tools_immunity:
                    drawn = random.choice(granary.hand.contents)
                    granary.hand.contents.remove(drawn)
                    player.hand.add_to_top(drawn)
                    print(f"{player.character} has taken {drawn} via GRANARY!")

            for item in granary.hand.contents:
                discard = granary.hand.remove_from_top()
                discard_deck.add_to_top(discard)

            discard_deck.add_to_top(card)
            return True

        elif card.effect2 == "Peach Gardens":
            self.hand.contents.remove(card)
            print(
                f"{self.character} has activated {card}. All damaged players will be healed by one health (unless negated).")

            check_aoe_negate_loop(players, card, self, self, card)

            for player in players:
                if not player.tools_immunity:
                    if player.max_health > player.current_health:
                        player.current_health += 1
                        print(
                            f"{player.character} has been healed by one. ({player.current_health}/{player.max_health} HP remaining)")

            discard_deck.add_to_top(card)
            return True

        elif card.effect2 == "Rain of Arrows":
            self.hand.contents.remove(card)
            print(
                f"{self.character} has activated {card}. All players will take one damage (unless playing DEFEND or tool-card negated).")

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

                        for item in players:
                            if item.current_health < 1:
                                item.check_brink_of_death_loop(self)

            discard_deck.add_to_top(card)
            return True

        elif card.effect2 == "Coerce":
            possible_targets = 0
            for player in players[1:]:
                if len(player.equipment) > 0:
                    for item in player.equipment:
                        if item.ctype == "Weapon":
                            possible_targets += 1

            if possible_targets == 0:
                return False

            elif possible_targets > 0:
                targets = []
                for player in players[1:]:
                    for item in player.equipment:
                        if item.ctype == "Weapon":
                            targets.append(player)

                coerced = random.choice(targets)
                targets = coerced.calculate_targets_in_weapon_range()
                if len(targets) < 1:
                    return False
                else:
                    self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                    attacked = players[random.choice(targets)]
                    print(
                        f"{coerced.character} is being coerced into attacking {attacked.character}!")
                    if not check_negate_loop(players, card, self, coerced):
                        coerced.activate_coerce(attacked)
                    return True

        elif card.effect2 == "Dismantle":
            target = random.choice(players[1:])

            if (len(target.hand.contents) + len(target.equipment) + len(target.pending_judgements)) < 1:
                return False
            else:
                self.hand.contents.remove(card)
                discard_deck.add_to_top(card)
                print(
                    f"{self.character} has played {card} against {target.character}.")
                if not check_negate_loop(players, card, self, target):
                    self.activate_dismantle(card, target)
                return True

        elif card.effect2 == "Duel":
            target = random.choice(players[1:])
            self.hand.contents.remove(card)
            discard_deck.add_to_top(card)
            print(f"{self.character} has played {card} against {target.character}.")
            if not check_negate_loop(players, card, self, target):
                self.activate_duel(card, target)
            return True

        elif card.effect2 == "Greed":
            self.hand.contents.remove(card)
            discard_deck.add_to_top(card)
            print(f"{self.character} has played {card}.")
            if not check_negate_loop(players, card, self, self):
                self.draw(main_deck, 2)
            return True

        elif card.effect2 == "Negate":
            return False

        elif card.effect2 == "Steal":
            targets = self.calculate_targets_in_physical_range()
            if len(targets) < 1:
                return False
            target = players[random.choice(targets)]

            if (len(target.hand.contents) + len(target.equipment) + len(target.pending_judgements)) < 1:
                return False
            else:
                self.hand.contents.remove(card)
                discard_deck.add_to_top(card)
                print(
                    f"{self.character} has played {card} against {target.character}.")
                if not check_negate_loop(players, card, self, target):
                    self.activate_steal(card, target)
                return True

        # card.ctype == 'Delay-Tool':
        elif card.effect2 == "Acedia":
            target = random.choice(players[1:])
            for item in target.pending_judgements:
                if item.effect2 == 'Acedia':
                    return False

            else:
                self.hand.contents.remove(card)
                target.pending_judgements.insert(0, card)
                print(f"{self.character} has placed {card} on {target.character}!")
                return True

        elif card.effect2 == "Lightning":
            for item in self.pending_judgements:
                if item.effect2 == 'Lightning':
                    return False
            else:
                self.hand.contents.remove(card)
                self.pending_judgements.insert(0, card)
                print(f"{self.character} has called {card}.")
                return True

        elif card.effect2 == "Rations Depleted":
            return False

        # card.ctype == 'Equipment':
        elif card.ctype == "Weapon":
            weapon_index = None
            for item_index, item in enumerate(self.equipment):
                if item.ctype == "Weapon":
                    weapon_index = item_index
                    break

            if weapon_index != None:
                discard_deck.add_to_top(self.equipment.pop(weapon_index))
            self.hand.contents.remove(card)
            self.equipment.append(card)
            print(f"{self.character} has equipped {card}.")
            return True

        elif card.ctype == "Armor":
            armor_index = None
            for item_index, item in enumerate(self.equipment):
                if item.ctype == "Armor":
                    armor_index = item_index
                    break

            if armor_index != None:
                discard_deck.add_to_top(self.equipment.pop(armor_index))
            self.hand.contents.remove(card)
            self.equipment.append(card)
            print(f"{self.character} has equipped {card}.")
            return True

        elif card.ctype == "-1 Horse":
            horse_index = None
            for item_index, item in enumerate(self.equipment):
                if item.ctype == "-1 Horse":
                    horse_index = item_index
                    break

            if horse_index != None:
                discard_deck.add_to_top(self.equipment.pop(horse_index))
            self.hand.contents.remove(card)
            self.equipment.append(card)
            print(f"{self.character} has equipped {card}.")
            return True

        elif card.ctype == "+1 Horse":
            horse_index = None
            for item_index, item in enumerate(self.equipment):
                if item.ctype == "+1 Horse":
                    horse_index = item_index
                    break

            if horse_index != None:
                discard_deck.add_to_top(self.equipment.pop(horse_index))
            self.hand.contents.remove(card)
            self.equipment.append(card)
            print(f"{self.character} has equipped {card}.")
            return True

    def use_reaction_effect(self, response_required, card, source, other_card=None):
        # 'response_required' refers to what sort of reaction-effect needed, eg. ATTACK, DEFEND, PEACH, NEGATE?
        # 'card' refers to the card played that is being 'reacted' against
        # 'source' refers to the person who played the 'card'
        # 'other_card' refers to the original card used, typically required in reactions to reactions to reactions etc...
        output_value = 0
        for item in self.hand.contents:
            item.effect2 = None
        for item in self.equipment:
            item.effect2 = None
        reactions_possible = True
        while reactions_possible:
            if response_required == "Brink Of Death":
                possible_cards = []
                for item in self.hand.contents:
                    if item.effect == "Peach":
                        possible_cards.append(item)

                if len(possible_cards) > 0:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        peach = random.choice(possible_cards)
                        self.hand.contents.remove(peach)
                        discard_deck.add_to_top(peach)
                        output_value += 1

                        if self == source:
                            print(
                                f"{self.character} has healed themselves using a {peach}! ({self.current_health + output_value}/{self.max_health} HP remaining!)")
                        else:
                            print(
                                f"{self.character} has healed {source.character} using a {peach}. ({source.current_health + output_value}/{source.max_health} HP remaining!)")
                            if source.check_break_brink_loop(output_value):
                                reactions_possible = False
                                return output_value

                reactions_possible = False
                return output_value

            elif response_required == "Negate":
                possible_cards = []
                for item in self.hand.contents:
                    if item.effect == "Negate":
                        possible_cards.append(item)

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
                        else:
                            print(
                                f"{self.character} has played a {negate} against the {card} of {source.character}!")
                        return negate
                return False

            elif response_required == "AoE Negate":
                possible_cards = []
                for item in self.hand.contents:
                    if item.effect == "Negate":
                        possible_cards.append(item)

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
                            print(
                                f"{self.character} played a {negate} against the effects of {card.effect2.upper()} on {negated_for.character}!")
                            return [True, negate, negated_for, self]
                return [False, None, None, None]

            elif response_required == "Attack" and card.effect2 == "Barbarians":
                attack = 0
                possible_cards = []
                for item in self.hand.contents:
                    if item.effect == "Attack":
                        possible_cards.append(item)

                serp_spear = None
                if (len(self.hand.contents) > 1):
                    for serp_spear in self.equipment:
                        if serp_spear.effect == "Serpent Spear":
                            possible_cards.append(serp_spear)
                            break

                if len(possible_cards) > 0:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        attack = random.choice(possible_cards)
                        if attack == serp_spear:
                            serp_spear = self.check_weapon_serpent_spear()
                            attack = serp_spear[0]
                        else:
                            self.hand.contents.remove(attack)
                            discard_deck.add_to_top(attack)

                return attack

            elif response_required == "Defend" and card.effect2 == "Rain of Arrows":
                defend = 0

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

                possible_cards = []
                for item in self.hand.contents:
                    if item.effect == "Defend":
                        possible_cards.append(item)

                if len(possible_cards) > 0:
                    choices = [True, False]
                    activated = random.choice(choices)
                    if activated:
                        defend = random.choice(possible_cards)
                        self.hand.contents.remove(defend)
                        discard_deck.add_to_top(defend)
                return defend

            elif response_required == "Attack" and card.effect2 == "Duel":
                required = 1
                while required > 0:
                    possible_cards = []
                    for item in self.hand.contents:
                        if item.effect == "Attack":
                            possible_cards.append(item)

                    serp_spear = None
                    if (len(self.hand.contents) > 1):
                        for serp_spear in self.equipment:
                            if serp_spear.effect == "Serpent Spear":
                                possible_cards.append(serp_spear)
                                break

                    if (len(possible_cards) > 0):
                        choices = [True, False]
                        activated = random.choice(choices)
                        if activated:
                            attack = random.choice(possible_cards)
                            if attack == serp_spear:
                                serp_spear = self.check_weapon_serpent_spear()
                                attack = serp_spear[0]
                                required -= 1
                            else:
                                self.hand.contents.remove(attack)
                                discard_deck.add_to_top(attack)
                                print(
                                    f"{self.character} played an {attack} during the DUEL!")
                                required -= 1
                        else:
                            print(f"{self.character} did not play an ATTACK!")
                            return True
                    elif len(possible_cards) < 1:
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
                while required > 0:
                    defend = 0

                    # Check for Eight Trigrams
                    armor = False
                    for eight_trigrams in self.equipment:
                        if eight_trigrams.effect == "Eight-Trigrams":
                            armor = True
                            break
                    if source.check_weapon_black_pommel() and armor:
                        print(
                            f"  >> {source.character} has [Black Pommel <:2:> - 6\u2660] equipped, and therefore ignores any armor when attacking.")
                    elif not source.check_weapon_black_pommel() and armor:
                        choices = [True, False]
                        activated = random.choice(choices)
                        if activated:
                            defend = self.check_armor_eight_trigrams()
                            if type(defend) == Card:
                                required -= 1
                                if required == 0:
                                    return defend
                                else:
                                    choices = [True, False]
                                    activated = random.choice(choices)
                                    if activated:
                                        defend = self.check_armor_eight_trigrams()
                                        if type(defend) == Card:
                                            required -= 1
                                            if required == 0:
                                                return defend

                    possible_cards = []
                    for item in self.hand.contents:
                        if item.effect == "Defend":
                            possible_cards.append(item)

                    if len(possible_cards) > 0:
                        choices = [True, False]
                        activated = random.choice(choices)
                        if activated:
                            defend = random.choice(possible_cards)
                            self.hand.contents.remove(defend)
                            discard_deck.add_to_top(defend)
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

        # Weapon and Black Shield checks
        self.check_gender_swords(target)
        armor = False
        if (card2 == None) or (card2.effect2 == "Black Attack"):
            if target.check_armor_black_shield(card):
                armor = True
            if self.check_weapon_black_pommel() and armor:
                print(
                    f"  >> {self.character} has [Black Pommel <:2:> - 6\u2660] equipped, and therefore ignores any armor when attacking.")
            elif armor:
                return False

        # Check for DEFEND
        attack_defended = target.use_reaction_effect(
            "Defend", card, self)
        if type(attack_defended) == Card:
            if (attack_defended.effect == "Defend") or (attack_defended.effect2 == "Defend"):
                print(
                    f"{target.character} successfully defended the ATTACK with {attack_defended}.")

                # DEFENDED - reactionary abilities
                self.check_weapon_axe(target)
                self.check_weapon_green_dragon_halberd(target)
        else:
            # DAMAGED - pre-damage abilities
            if self.check_frost_blade(target):
                return "Break"

            # Damage Resolution
            damage_dealt = 1
            target.current_health -= damage_dealt
            print(f"{self.character} attacked {target.character}, dealing {damage_dealt} damage ({target.current_health}/{target.max_health} HP remaining).")
            self.check_weapon_huangs_longbow(target)
            for player in players:
                if player.current_health < 1:
                    if player.check_brink_of_death_loop(self) == "Break":
                        return "Break"

    def activate_coerce(self, target):
        # 'target' refers to the player that will potentially be attacked by the coerced player!
        possible_cards = []
        for item in self.hand.contents:
            if item.effect == "Attack":
                possible_cards.append(item)

        serp_spear = None
        if (len(self.hand.contents) > 1):
            for serp_spear in self.equipment:
                if serp_spear.effect == "Serpent Spear":
                    possible_cards.append(serp_spear)
                    break

        if (len(possible_cards) > 0):
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                card = random.choice(possible_cards)
                if card == serp_spear:
                    serp_spear = self.check_weapon_serpent_spear()
                    return self.activate_attack(serp_spear[0], target, serp_spear[1])
                else:
                    self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                    card.effect2 = "Attack"

                    print(
                        f"{self.character} was coerced into attacking {target.character}.")
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

        for item in self.equipment:
            if item.ctype == "Weapon":
                self.equipment.remove(item)
                players[0].hand.add_to_top(item)
                print(
                    f"{self.character}'s weapon; {item}, has been stolen by {players[0].character} for not attacking {target.character}!")
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

            elif dismantled in target.hand.contents:
                target.hand.contents.remove(dismantled)
                discard_deck.add_to_top(dismantled)
                print(
                    f"{self.character} dismantled {dismantled} from the hand of {target.character}!")

    def activate_duel(self, card, target):
        # 'card' refers to the 'Duel' card used in Player.use_card_effect(card)
        # 'target' refers to the player targeted by Duel!
        # 'duel_won' is a boolean that determines the winner of the duel
        duel_won = target.use_reaction_effect("Attack", card, self)
        damage_dealt = 1

        if duel_won:
            target.current_health -= damage_dealt
            print(
                f"{self.character} has won the DUEL! {target.character} takes {damage_dealt} damage! ({target.current_health}/{target.max_health} HP remaining)")
            for player in players:
                if player.current_health < 1:
                    if player.check_brink_of_death_loop(self) == "Break":
                        return False

        elif not duel_won:
            self.current_health -= damage_dealt
            print(
                f"{target.character} has won the DUEL! {self.character} takes {damage_dealt} damage! ({self.current_health}/{self.max_health} HP remaining)")
            for player in players:
                if player.current_health < 1:
                    if player.check_brink_of_death_loop(target) == "Break":
                        return False

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

            elif stolen in target.hand.contents:
                target.hand.contents.remove(stolen)
                self.hand.add_to_top(stolen)
                print(
                    f"{self.character} stole {stolen} from the hand of {target.character}!")

    # In-game General Checks
    def calculate_targets_in_physical_range(self, modifier=0):
        # 'modifier' refers to any bonuses granted/penalized by abilities/equipment
        my_index = get_player_index(self)
        output = []
        for item in self.equipment:
            if item.ctype == "-1 Horse":
                modifier += 1
                break

        for (target_index, target) in enumerate(players):
            if target_index != my_index:
                distance = abs(target_index - my_index)

                target_modifier = 0
                for item in target.equipment:
                    if item.ctype == "+1 Horse":
                        target_modifier += 1
                        break

                if distance > len(players) / 2:
                    distance = len(players) - distance
                if distance - (1 + modifier) + (target_modifier) <= 0:
                    output.append(target_index)
        return output

    def calculate_targets_in_weapon_range(self, modifier=0, omit=None):
        # 'modifier' refers to any bonuses granted/penalized by abilities/equipment
        # 'omit' refers to any players that are untargetable during this calculation
        my_index = get_player_index(self)
        output = []
        weapon_range = 1
        for item in self.equipment:
            if item.ctype == "-1 Horse":
                modifier += 1
            if item.ctype == "Weapon":
                weapon_range = item.weapon_range

        for (target_index, target) in enumerate(players):
            if target_index != my_index:
                distance = abs(target_index - my_index)

                target_modifier = 0
                for item in target.equipment:
                    if item.ctype == "+1 Horse":
                        target_modifier += 1
                        break

                if distance > len(players) / 2:
                    distance = len(players) - distance
                if distance - (weapon_range + modifier) + (target_modifier) <= 0:
                    output.append(target_index)
        if omit != None:
            output.remove(omit)
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

        # Regular Brink of Death Loop
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
            print(f"{self.character} wasn't saved from the brink of death!")
            self.discard_all_cards(death=True)
            players.pop(dying_index)
            if win_conditions == "Roles":
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
                    print(
                        f"  >> Judgement: {self.character} flipped a {judgement_card}.")
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
                    print(
                        f"  >> Judgement: {self.character} flipped a {judgement_card}.")

                    # IF JUDGEMENT OCCURS AND HITS PLAYER!
                    if (judgement_card.suit == "\u2660") and (10 > judgement_card.rank > 1):
                        print(
                            f"{self.character}'s judgement card is a {judgement_card}, and therefore {pending_judgement} deals {lightning_damage} damage, then gets discarded!")
                        discard_deck.add_to_top(pending_judgement)
                        damage_dealt = lightning_damage
                        self.current_health -= damage_dealt
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

    # Equipment Checks
    def check_armor_black_shield(self, card):
        # 'card' refers to the ATTACK card used against the defending-player
        armor = False
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Black Shield":
                armor_index = item_index
                armor = True
                break

        if armor:
            if card.suit == "\u2660" or card.suit == "\u2663":
                print(
                    f"  >> {self.character} has {self.equipment[armor_index]} equipped, and therefore CANNOT be affected by black attack cards ({card} discarded as normal).")
                return True
        return False

    def check_armor_eight_trigrams(self):
        if self.used_trigrams:
            return False

        armor = False
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Eight-Trigrams":
                armor_index = item_index
                armor = True
                break

        if armor:
            print(
                f"  >> {self.character} chose to activate their equipped {self.equipment[armor_index]} (armor); needs \u2665 or \u2666 to automatically dodge.")
            main_deck.discard_from_deck()
            judgement_card = discard_deck.contents[0]
            print(
                f"  >> Judgement: {self.character} flipped a {judgement_card}.")
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
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Axe":
                total_cards = self.hand.contents + self.equipment
                if len(total_cards) > 2:
                    weapon = True
                    break

        if weapon:
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                cards_to_discard = 2
                while cards_to_discard > 0:
                    card = self.discard("Handquip")
                    if card.effect == "Axe":
                        discard_deck.contents.remove(card)
                        self.equipment.insert(item_index, card)
                    else:
                        cards_to_discard -= 1
                damage_dealt = 1
                target.current_health -= damage_dealt
                print(
                    f"  >> {self.character} has forced the damage to {target.character}, by using their [Axe <:3:> - 5\u2666], and discarding two cards ({target.current_health}/{target.max_health} HP remaining).")
                for player in players:
                    if player.current_health < 1:
                        player.check_brink_of_death_loop(self)
                return True

    def check_weapon_black_pommel(self):
        for item in self.equipment:
            if item.effect == "Black Pommel":
                return True

    def check_frost_blade(self, target):
        # 'target' refers to the target of the initial ATTACK card.
        weapon = False
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Frost Blade":
                weapon_index = item_index
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
                    return True
        return False

    def check_gender_swords(self, target):
        # 'target' refers to the target of the initial ATTACK card.
        weapon = False
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Gender-Swords":
                weapon_index = item_index
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
                        print(
                            f"  >> {target.character} discards {card} after being attacked by {self.equipment[weapon_index]}.")
                else:
                    self.draw(main_deck, 1, False)
                    print(
                        f"  >> {self.character} draws a card after attacking with {self.equipment[weapon_index]}.")

    def check_weapon_green_dragon_halberd(self, target):
        # 'target' refers to the target of the initial ATTACK card.
        weapon = False
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Green Dragon Halberd":
                weapon_index = item_index
                weapon = True
                break

        if weapon:
            possible_cards = []
            for item in self.hand.contents:
                if item.effect == "Attack":
                    possible_cards.append(item)

            if len(possible_cards) > 0:
                choices = [True, False]
                activated = random.choice(choices)
                if activated:
                    card = random.choice(possible_cards)
                    self.hand.contents.remove(card)
                    discard_deck.add_to_top(card)
                    card.effect2 = "Attack"
                    print(
                        f"  >> {self.character} attacked {target.character} again with {card}, using {self.equipment[weapon_index]}!")
                    self.activate_attack(card, target)
                    return True

    def check_weapon_huangs_longbow(self, target):
        # 'target' refers to the target of the initial ATTACK card.
        weapon = False
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Huang's Longbow":
                weapon_index = item_index
                weapon = True
                break

        if weapon:
            choices = [True, False]
            activated = random.choice(choices)
            if activated:
                choices = []
                for item2 in target.equipment:
                    if item2.ctype == "-1 Horse" or item2.ctype == "+1 Horse":
                        choices.append(item2)
                if len(choices) < 1:
                    return False
                else:
                    horse_slain = random.choice(choices)
                    target.equipment.remove(horse_slain)
                    discard_deck.add_to_top(horse_slain)
                    print(
                        f"  >> {self.character} has {self.equipment[weapon_index]} equipped, and therefore slays {horse_slain} of {target.character}!")
                    return True

    def check_weapon_serpent_spear(self):
        weapon = False
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Serpent Spear":
                weapon_index = item_index
                weapon = True
                break

        if weapon and (len(self.hand.contents) > 1):
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
            return [card, card2]
        return [False]

    def check_weapon_sky_scorcher_halberd(self, target):
        # 'target' refers to the target of the initial ATTACK card. They cannot be hit again via this weapon's effect!
        weapon = False
        if len(self.hand.contents) == 0:
            for item_index, item in enumerate(self.equipment):
                if item.effect == "Sky Scorcher Halberd":
                    weapon_index = item_index
                    weapon = True
                    break

        if weapon:
            print(
                f"  >> {self.character} has used their last hand-card to ATTACK {target.character} with {self.equipment[weapon_index]}. They can target up to two extra players!")
            targets = self.calculate_targets_in_weapon_range()
            target_index1 = get_player_index(target)
            targets.remove(target_index1)
            if len(targets) < 1:
                return 0

            else:
                targets.append("No more!")
                target_index2 = random.choice(targets)
                if target_index2 == "No more!":
                    return 0
                target2 = players[target_index2]
                targets.remove(target_index2)
                if len(targets) < 1:
                    return [True, target2]

                else:
                    target_index3 = random.choice(targets)
                    if target_index3 == "No more!":
                        return [True, target2]
                    target3 = players[target_index3]
                    return [True, target2, target3]
        return 0

    def check_weapon_zhuge_crossbow(self):
        for item_index, item in enumerate(self.equipment):
            if item.effect == "Zhuge Crossbow":
                print(
                    f"  >> {self.character} has {self.equipment[item_index]} equipped, and therefore has no limit to the amount of attacks per turn.")
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
        return self.start_judgement_phase()

    def start_judgement_phase(self):
        if self.check_pending_judgements() == "Break":
            return "Break"
        else:
            return self.start_drawing_phase()

    def start_drawing_phase(self):
        cards_drawn = 2
        self.draw(main_deck, cards_drawn)
        if self.acedia_active:
            return self.start_discard_phase()
        else:
            return self.start_action_phase()

    def start_action_phase(self):
        action_phase_active = True
        while action_phase_active:
            if win_conditions == "Roles":
                if check_win_conditions():
                    return self.start_end_phase()

            elif len(players) < 2:
                return self.start_end_phase()

            actions = self.hand.contents + ["End Action-Phase"]

            # Serpent Spear Check
            serp_spear = None
            if (len(self.hand.contents) > 1) and (self.attacks_this_turn == 0):
                for serp_spear in self.equipment:
                    if serp_spear.effect == "Serpent Spear":
                        actions.append(serp_spear)
                        break

            card = random.choice(actions)
            # print(f"Options: {actions}")
            # print(f"Selected: {card}")

            if card == "End Action-Phase":
                return self.start_discard_phase()

            elif card == serp_spear:
                serp_spear = self.check_weapon_serpent_spear()
                self.use_card_effect(serp_spear[0], serp_spear[1])
            else:
                card.effect2 = card.effect
                self.use_card_effect(card)

    def start_discard_phase(self):
        difference = 0
        # Discard down to your current health level
        if len(self.hand.contents) > self.current_health:
            difference = (len(self.hand.contents) - self.current_health)
            self.discard("Hand", difference)
        return self.start_end_phase()

    def start_end_phase(self):
        print(
            f"------------------------------<{self.character} has ended their turn!>------------------------------")


# --- LOOK HERE TO AUTOPLAY GAMES
# 'num_players' refers to the number of players
# 'iterations' refers to the number of iterations that the game will run
# 'lightning_dmg' refers to the amount of damage a player takes when hit by lightning - 3 by default
# 'roles' refers to whether there are any player roles in-game - True by default (if False: all players will be considered rebels)
play_games(num_players=8, num_iterations=10000, lightning_dmg=3, roles=True)
