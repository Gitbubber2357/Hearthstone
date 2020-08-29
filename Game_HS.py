import numpy as np

# ==========================================================================================
# preparing CODE

class Card:
    def __init__(self, name, rank, attack, health):
        self.name = name
        self.rank = rank
        self.attack = attack
        self.health = health

        if self.health > 0:
            self.is_live = True

        else:
            self.is_live = False

    def accept_damage(self, attack):
        self.health -= attack

        if self.health > 0:
            self.is_live = True
        else:
            self.is_live = False


class BuffedCard(Card):
    def __init__(self, name, rank, attack, health, poisonous = False, shield = False, windfury = False, taunt = False):
        super().__init__(name, rank, attack, health)
        self.is_poisonous = poisonous
        self.is_shield = shield
        self.is_windfury = windfury
        self.is_taunt = taunt

    def copy(self):
        return BuffedCard(self.name, self.rank, self.attack, self.health,
                          self.is_poisonous, self.is_shield, self.is_windfury, self.is_taunt)


def attack(card_A, card_B):
    if card_A.is_shield == True:
        card_A.is_shield = False
    elif card_B.is_poisonous == True:
        card_A.accept_damage(card_A.health)
    else:
        card_A.accept_damage(card_B.attack)

    if card_B.is_shield == True:
        card_B.is_shield = False
    elif card_A.is_poisonous == True:
        card_B.accept_damage(card_B.health)
    else:
        card_B.accept_damage(card_A.attack)


class Table:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def change(self, site_A, site_B):
        self.cards[site_A], self.cards[site_B] =  self.cards[site_B], self.cards[site_A]

    def is_live_counter(self):
        return sum(card.is_live for card in self.cards)

    def is_taunt_counter(self):
        return sum(card.is_live and card.is_taunt for card in self.cards)

    def rank_counter(self):
        return sum(card.rank for card in self.cards if card.is_live)

    def copy_table(self):
        table_copy = Table(self.name)
        for card in self.cards:
            table_copy.cards.append(card.copy())
        return table_copy

    def one_round(self, op_table):
        table_copy_self = self.copy_table()
        table_copy_op = op_table.copy_table()

        attacker_index_self = attacker_index_op = -1
        initial_live_self = int(table_copy_self.is_live_counter())
        initial_live_op = int(table_copy_op.is_live_counter())

        def total_attack(table_copy_self, table_copy_op, attacker_index_self):
            if table_copy_op.is_taunt_counter() != 0:
                random_int = np.random.randint(0, table_copy_op.is_taunt_counter())
                taunt_num = -1
                temp = -1
                while taunt_num != random_int:
                    temp += 1
                    if table_copy_op.cards[temp].is_taunt and table_copy_op.cards[temp].is_live:
                        taunt_num += 1
                random_int = temp

            else:
                random_int = np.random.randint(0, int(table_copy_op.is_live_counter()))

                while not table_copy_op.cards[random_int].is_live:
                    random_int += 1
                    random_int %= int(table_copy_op.is_live_counter())

            attack(table_copy_self.cards[attacker_index_self], table_copy_op.cards[random_int])

            print("%s in %s attack %s in %s" %(table_copy_self.cards[attacker_index_self].name, table_copy_self.name,
                                               table_copy_op.cards[random_int].name, table_copy_op.name))


        while table_copy_self.is_live_counter() != 0 and table_copy_op.is_live_counter() != 0:
            attacker_index_self += 1
            attacker_index_self %= initial_live_self

            while not table_copy_self.cards[attacker_index_self].is_live:
                attacker_index_self += 1
                attacker_index_self %= initial_live_self

            total_attack(table_copy_self, table_copy_op, attacker_index_self)

            if table_copy_self.cards[attacker_index_self].is_windfury and (
                    table_copy_self.is_live_counter() != 0 and table_copy_op.is_live_counter() != 0):
                total_attack(table_copy_self, table_copy_op, attacker_index_self)

            if table_copy_self.is_live_counter() != 0 and table_copy_op.is_live_counter() != 0:
                attacker_index_op += 1
                attacker_index_op %= initial_live_op

                while not table_copy_op.cards[attacker_index_op].is_live:
                    attacker_index_op += 1
                    attacker_index_op %= initial_live_op

                total_attack(table_copy_op, table_copy_self, attacker_index_op)

                if table_copy_self.cards[attacker_index_self].is_windfury and (
                        table_copy_self.is_live_counter() != 0 and table_copy_op.is_live_counter() != 0):
                    total_attack(table_copy_self, table_copy_op, attacker_index_self)

        if table_copy_self.is_live_counter() != 0 and table_copy_op.is_live_counter() == 0:
            print("%s wins this round." %(table_copy_self.name))
            return table_copy_self.name, table_copy_self.rank_counter()

        elif table_copy_self.is_live_counter() == 0 and table_copy_op.is_live_counter() != 0:
            print("%s wins this round." %(table_copy_op.name))
            return table_copy_op.name, table_copy_op.rank_counter()

        else:
            print("It's a tie.")
            return "None", 0

def prob_mach(*prob_number):
    prob_number = prob_number
    prob = [prob_number[i][0] for i in range(len(prob_number))]
    number = [prob_number[i][1] for i in range(len(prob_number))]
    prob_list = []
    for i in range(len(prob)):
        prob_list += [number[i] for n in range(prob[i])]

    temp = np.random.randint(0,len(prob_list))

    return prob_list[temp]


class Boss:
    def __init__(self, card_rank):
        self.rank = 1
        self.upgrade_coin = 6
        self.card_rank = card_rank
#         self.cards = cards

    def upgrade_coin_counter(self):
        if self.rank == 2:
            return 7
        elif self.rank == 3:
            return 8
        elif self.rank == 4:
            return 9
        elif self.rank == 5:
            return 10
        else:
            raise VauleError

    def rank_upgrade(self):
        self.rank += 1
        self.upgrade_coin = self.upgrade_coin_counter()

    def random_pick(self):
        if self.rank == 1:
            temp = prob_mach([1,1])
            return self.card_rank[temp-1][np.random.randint(0,4)].copy()
        elif self.rank == 2:
            temp = prob_mach([1,1], [1,2])
            return self.card_rank[temp-1][np.random.randint(0,4)].copy()
        elif self.rank == 3:
            temp = prob_mach([1,1], [2,2], [2,3])
            return self.card_rank[temp-1][np.random.randint(0,4)].copy()
        elif self.rank == 4:
            temp = prob_mach([1,1], [2,2], [3,3], [3,4])
            return self.card_rank[temp-1][np.random.randint(0,4)].copy()
        elif self.rank == 5:
            temp = prob_mach([1,1], [2,2], [3,3], [4,4], [4,5])
            return card_rank[temp-1][np.random.randint(0,4)].copy()
        else:
            temp = prob_mach([1,1], [2,2], [3,3], [4,4], [5,5], [5,6])
            return card_rank[temp-1][np.random.randint(0,4)].copy()

    def show(self):
        if self.rank == 1:
            show_cards = [self.random_pick() for i in range (2)]
        elif self.rank == 2:
            show_cards = [self.random_pick() for i in range (3)]
        elif self.rank == 3:
            show_cards = [self.random_pick() for i in range (3)]
        elif self.rank == 4:
            show_cards = [self.random_pick() for i in range (4)]
        elif self.rank == 5:
            show_cards = [self.random_pick() for i in range (4)]
        else:
            show_cards = [self.random_pick() for i in range (5)]

        return show_cards


class Player:
    def __init__(self, name, coin, blood):
        self.name = name
        self.coin = coin
        self.cards = []
        self.blood = blood


def interface(who, cards):
    def printer(TF):
        if TF:
            return "O"
        else:
            return "X"

    if who == "boss":
        print("Boss cards:")
        for i, card in enumerate(cards):
            if card == None:
                print("    %d. Sold out." %(i+1))
            else:
                print("    %d.  %s rank %d, attack = %d, health = %d, poisonous = %s, shield = %s, windfury = %s, taunt = %s"
                           %(i+1, card.name, card.rank, card.attack, card.health, printer(card.is_poisonous),
                                             printer(card.is_shield),printer(card.is_windfury), printer(card.is_taunt)))

    elif who == "table":
        print("Cards on the table:")
        if len(cards) == 0:
            print("    No cards on the table.")

        for i, card in enumerate(cards):
            print("    %d. %s rank %d, attack = %d, health = %d, poisonous = %s, shield = %s, windfury = %s, taunt = %s"
                      %(i+1, card.name, card.rank, card.attack, card.health, printer(card.is_poisonous),
                                        printer(card.is_shield),printer(card.is_windfury), printer(card.is_taunt)))

    elif who == "player":
        print("Your cards:")
        if len(cards) == 0:
            print("    You don't hava any cards.")

        for i, card in enumerate(cards):
            print("    %d. %s rank %d, attack = %d, health = %d, poisonous = %s, shield = %s, windfury = %s, taunt = %s"
                      %(i+1, card.name, card.rank, card.attack, card.health, printer(card.is_poisonous),
                                        printer(card.is_shield),printer(card.is_windfury), printer(card.is_taunt)))

    else:
        raise ValueError


def interface_total(B, T, P):
    print("-----------------------")
    interface("boss", B)
    interface("table", T)
    interface("player", P)
    print("-----------------------")


def require(parser, require_hint, exception_hint = None):
    while True:
        try:
            input_str = input(require_hint)
            if input_str == "Quit" or input_str == "quit" or input_str == "Q" or input_str == "q":
                require = None
            else:
                require = parser(input_str)
            break

        except:
            if exception_hint is not None:
                print(exception_hint)

    if require is None:
        raise ValueError
    return require

# ==========================================================================================
# GAME CODE (Hearthstone)

def Hearthstone(card_rank):
    name_one = input("What is your name(player_one):")
    name_two = input("What is your name(player_two):")

    player_one = Player(name = name_one, coin = 0, blood = 10)
    player_two = Player(name = name_two, coin = 0, blood = 10)

    boss_one = Boss(card_rank)
    boss_two = Boss(card_rank)

    table_one = Table(name = name_one)
    table_two = Table(name = name_two)

    coin_max = 2

    def round_player(player, boss, table):
        player.coin = coin_max
        print("-----------------------")
        print("Time for %s." %(player.name))
        boss.upgrade_coin -= 1

        show = boss.show()
        interface_total(B = show, T = table.cards, P = player.cards)
        print("Upgrade the rank of Boss needs %d coins." %(boss.upgrade_coin))
        print("%d coins are still on your hand." %(player.coin))
        print("%d bloods is left." %(player.blood))
        print("-----------------------")

        def parser_do_sth(input_str):
            if input_str == "B" and player.coin >= 3 and len(player.cards) < 5:
                return input_str

            elif input_str == "P" and len(table.cards) < 5 and len(player.cards) > 0:
                return input_str

            elif input_str == "C" and len(table.cards) >= 2:
                return input_str

            elif input_str == "S" and len(table.cards) >= 1:
                return input_str

            elif input_str == "U" and player.coin >= boss.upgrade_coin:
                return input_str

            elif input_str == "R" and player.coin >= 1:
                return input_str

            elif input_str == "O":
                return input_str

            else:
                if input_str == "B":
                    if player.coin < 3:
                        print("You don't have enough coins to buy a card.")
                    else:
                        print("Your hands are full.")

                elif input_str == "P":
                    print("You can not put this card here.")

                elif input_str == "C":
                    print("You should have at least two cards.")

                elif input_str == "S":
                    print("You should have at least one card.")

                elif input_str == "U":
                    print("You don't have enough coins to upgrade.")

                elif input_str == "R":
                    print("You don't have enough coins to refresh cards.")

                else:
                    print("Please input B/P/S/U/R/C to do different things, thanks!")

                raise ValueError


        def parser_buy(input_str):
            card_num = int(input_str) - 1
            if 0 <= card_num < len(show) and show[card_num] == None:
                print("This card is sold out.")
                raise ValueError
            if card_num < 0 or card_num >= len(show):
                print("There is no card on site %s." %(intput_str))
                raise ValueError
            return card_num

        def parser_put(input_str):
            card_num = int(input_str) - 1
            if card_num < 0 or card_num >= len(player.cards):
                print("There is no card on site %d." %(card_num+1))
                raise ValueError
            return card_num

        def parser_start(input_str):
            card_start = int(input_str) - 1
            if card_start < 0 or card_start >= len(table.cards):
                print("There is no card on site %d." %(card_start+1))
                raise ValueError
            return card_start

        def parser_end(input_str):
            card_end = int(input_str) - 1
            if 0 <= card_end < len(table.cards) and card_end == card_start:
                print("This is the orginal card.")
                raise ValueError
            if card_end < 0 or card_end >= len(table.cards):
                print("There is no card on site %s." %(input_str))
                raise ValueError
            return card_end

        def parser_sell(input_str):
            card_num = int(input_str) - 1
            if card_num < 0 or card_num >= len(table.cards):
                print("There is no card on site %d." %(card_num+1))
                raise ValueError
            return card_num

        while True:
            do_sth = require(parser_do_sth,
                     "Buy cards(B) / Put cards(P) / Change cards(C) / Sell a card(S) / Upgrade(U) / Refresh cards(R) / Over(O): ")

            if do_sth == "B":
                card_num = require(parser_buy, "Which card do you want to buy?")
                player.cards += [show[card_num].copy()]
                player.coin -= 3
                show[card_num] = None

            elif do_sth == "P":
                card_num = require(parser_put, "Which card do you want to put onto the table?")
                table.cards.append(player.cards[card_num].copy())
                del player.cards[card_num]

            elif do_sth == "C":
                card_start = require(parser_start, "Which card do you want to move on the table?")
                card_end = require(parser_end, "Which site do you want to move to the table?")
                table.change(card_start, card_end)

            elif do_sth == "S":
                card_num = require(parser_sell, "Which card is going to be sold on the table?")
                del table.cards[card_num]
                player.coin += 1

            elif do_sth == "U":
                player.coin -= boss.upgrade_coin
                boss.rank_upgrade()

            elif do_sth == "R":
                player.coin -= 1
                show = boss.show()

            else:
                break

            interface_total(B = show, T = table.cards, P = player.cards)
            print("Upgrade the rank of Boss needs %d coins." %(boss.upgrade_coin))
            print("%d coins are still on your hand." %(player.coin))
            print("%d bloods is left." %(player.blood))
            print("-----------------------")

    while player_one.blood > 0 and player_two.blood > 0:
        coin_max = min(coin_max+1, 10)
        round_player(player_one, boss_one, table_one)
        round_player(player_two, boss_two, table_two)

        print("-----------------------")
        print("Let's battle!")
        print("-----------------------")

        temp = np.random.randint(1,3)

        if temp == 1:
            who_win, card_damage = table_one.one_round(table_two)

        else:
            who_win, card_damage = table_two.one_round(table_one)

        if who_win == player_one.name:
            player_two.blood -= card_damage + boss_one.rank

        elif who_win == player_two.name:
            player_one.blood -= card_damage + boss_two.rank

        else:
            pass

        if player_one.blood > 0 and player_two.blood <= 0:
            print("%s wins this game." %(player_one.name))

        elif player_one.blood <= 0 and player_two.blood > 0:
            print("%s wins this game." %(player_two.name))

        else:
            pass
