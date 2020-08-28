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


def attack(card_A, card_B):
    if card_A.is_shield == True:
        card_A.is_shoeld = False
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
    def __init__(self, name, *cards):
        self.name = name
        self.cards = list(cards)
    
    def change(self, site_A, site_B):
        self.cards[site_A], self.cards[site_B] =  self.cards[site_B], self.cards[site_A]
        
    def is_live_counter(self):
        return sum(card.is_live for card in self.cards)
    
    def rank_counter(self):
        return sum(card.rank for card in self.cards if card.is_live)
    
    def copy(self):
        health = [card.health for card in self.cards]
        shield = [card.is_shield for card in self.cards]
        return health, shield
    
    def one_round(self, op_table):
        copy_H_self, copy_S_self = self.copy()
        copy_H_op, copy_S_op = op_table.copy()
        
        attacker_index_self = attacker_index_op = -1
        initial_live_self = int(self.is_live_counter())
        initial_live_op = int(op_table.is_live_counter())
        
        while self.is_live_counter() != 0 and op_table.is_live_counter() != 0:
            attacker_index_self += 1
            attacker_index_self %= initial_live_self

            while not self.cards[attacker_index_self].is_live:
                attacker_index_self += 1
                attacker_index_self %= initial_live_self

            random_int = np.random.randint(0,initial_live_op)

            while not op_table.cards[random_int].is_live:
                random_int += 1
                random_int %= initial_live_op
            
            attack(self.cards[attacker_index_self], op_table.cards[random_int])
            print("%s in %s attack %s in %s" %(self.cards[attacker_index_self].name, self.name,
                                                    op_table.cards[random_int].name, op_table.name))

            if self.is_live_counter() != 0 and op_table.is_live_counter() != 0:
                attacker_index_op += 1
                attacker_index_op %= initial_live_op

                while not op_table.cards[attacker_index_op].is_live:
                    attacker_index_op += 1
                    attacker_index_op %= initial_live_op

                random_int = np.random.randint(0,initial_live_self)
                
                while not self.cards[random_int].is_live:
                    random_int += 1
                    random_int %= initial_live_self

                attack(op_table.cards[attacker_index_op], self.cards[random_int])
                print("%s in %s attack %s in %s" %(op_table.cards[attacker_index_op].name, op_table.name,
                                                   self.cards[random_int].name, self.name))
                        
        if self.is_live_counter() != 0 and op_table.is_live_counter() == 0:
            print("%s wins this round." %(self.name))
            return "self", self.rank_counter()
            
        elif self.is_live_counter() == 0 and op_table.is_live_counter() != 0:
            print("%s wins this round." %(op_table.name))
            return "op", op_table.rank_counter()
            
        else:
            print("It's a tie.")
            return "nobody", 0
        
        for i in range(len(self.cards)):
            self.cards[i].health = copy_H_self[i]
            self.cards[i].is_shield = copy_S_self[i]
        
        for i in range(len(op_table.cards)):
            op_table.cards[i].health = copy_H_op[i]
            op_table.cards[i].is_shield = copy_S_op[i]
            
            
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
    def __init__(self):
        self.rank = 1
        self.upgrade_coin = 6
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
            temp = prob_mach([1,self.rank])
            return card_rank[temp-1][np.random.randint(0,2)]
        elif self.rank == 2:
            temp = prob_mach([1,1], [1,2])
            return card_rank[temp-1][np.random.randint(0,2)]
        elif self.rank == 3:
            temp = prob_mach([1,1], [2,2], [2,3])
            return card_rank[temp-1][np.random.randint(0,2)]
        elif self.rank == 4:
            temp = prob_mach([1,1], [2,2], [3,3], [3,4])
            return card_rank[temp-1][np.random.randint(0,2)]
        else:
            temp = prob_mach([1,1], [2,2], [3,3], [4,4], [4,5])
            return card_rank[temp-1][np.random.randint(0,2)]
    
    def show(self):
        if self.rank == 1:
            show_cards = [self.random_pick() for i in range (3)]
        elif self.rank == 2:
            show_cards = [self.random_pick() for i in range (3)]
        elif self.rank == 3:
            show_cards = [self.random_pick() for i in range (4)]
        elif self.rank == 4:
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
    
    def buy_card(self, card):
        if self.coin >= 3 and len(self.cards) < 5:
            self.cards += [card]
            self.coin -= 3
        
        elif self.coin < 3:
            print("You don't have enough coins to buy a card.")
        
        else:
            print("Your hands are full.")
    
    def sell_card(self, site):
        if site > 0 and site <= len(self.cards):
            del self.cards[site-1]
            self.coin += 1
        else:
            print("You have no cards in site %d" %(site))
            
            
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
                print("    %d. rank = %d, attack = %d, health = %d, poisonous = %s, shield = %s"
                      %(i+1, card.rank, card.attack, card.health, printer(card.is_poisonous), printer(card.is_shield)))
    
    elif who == "table":
        print("Cards on the table:")
        if len(cards) == 0:
            print("    No cards on the table.")
        
        for i, card in enumerate(cards):
            print("    %d. rank = %d, attack = %d, health = %d, poisonous = %s, shield = %s"
                  %(i+1, card.rank, card.attack, card.health, printer(card.is_poisonous), printer(card.is_shield)))
    
    elif who == "player":
        print("Your cards:")
        if len(cards) == 0:
            print("    You don't hava any cards.")
        
        for i, card in enumerate(cards):
            print("    %d. rank = %d, attack = %d, health = %d, poisonous = %s, shield = %s"
                  %(i+1, card.rank, card.attack, card.health, printer(card.is_poisonous), printer(card.is_shield)))
    
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

def Hearthstone():
    name_one = input("What is your name (player_one):")
    name_two = input("What is your name (player_two):")
    
    player_one = Player(name = name_one, coin = 3, blood = 10)
    player_two = Player(name = name_two, coin = 3, blood = 10)
    
    boss_one = Boss()
    boss_two = Boss()
    
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
        print("-----------------------")

        def parser_do_sth(input_str):
            if input_str == "B" and player.coin >= 3 and len(player.cards) < 5:
                return input_str
            
            elif input_str == "P" and len(table.cards) < 5 and len(player.cards) > 0:
                return input_str
            
            elif input_str == "S" and len(table.cards) >= 2:
                return input_str
            
            elif input_str == "U" and player.coin >= boss.upgrade_coin:
                return input_str

            elif input_str == "R" and player.coin >= 1:
                return input_str

            elif input_str == "C":
                return input_str

            else:
                if input_str == "B":
                    print("You don't have enough coins to buy a card.")

                elif input_str == "U":
                    print("You don't have enough coins to upgrade.")

                elif input_str == "R":
                    print("You don't have enough coins to refresh cards.")

                else:
                    print("Please input B/P/S/U/R/C to do different things, thanks!")

                raise ValueError

    
        def parser_buy(input_str):
            card_num = int(input_str) - 1
            if 0 <= card_num <= len(show) and show[card_num] != None:
                return card_num

            else:
                if card_num <= len(show) and show[card_num] == None:
                    print("This card is sold out.")
                else:
                    print("There is no card on site %s." %(intput_str))

                raise ValueError
                
        def parser_put(input_str):
            card_num = int(input_str) - 1
            if 0 <= card_num <= len(player.cards):
                return card_num
            
            else:
                print("There is no card on site %s." %(intput_str))
                raise ValueError
                
        def parser_start(input_str):
            card_start = int(input_str) - 1
            if 0 <= card_start <= len(table.cards):
                return card_start
            
            else:
                print("There is no card on site %s." %(intput_str))
                raise ValueError
                
        def parser_end(input_str):
            card_end = int(input_str) - 1
            if 0 <= card_end <= len(table.cards) and card_end != card_start:
                return card_end
            
            else:
                if 0 <= card_end <= len(table.cards) and card_end == card_start:
                    print("This is the orginal card.")
                
                else:
                    print("There is no card on site %s." %(intput_str))
                
                raise ValueError
            
        while True:
            do_sth = require(parser_do_sth, "Buy cards(B) / Put cards(P) / Switch cards(S) / Upgrade(U) / Refresh cards(R) / Complete(C): ")

            if do_sth == "B":
                card_num = require(parser_buy, "Which card do you want to buy?")
                player.buy_card(show[card_num])
                show[card_num] = None
                interface_total(B = show, T = table.cards, P = player.cards)
                print("Upgrade the rank of Boss needs %d coins." %(boss.upgrade_coin))
                print("%d coins are still on your hand." %(player.coin))
                print("-----------------------")
            
            elif do_sth == "P":
                card_num = require(parser_put, "Which card do you want to put onto the table?")
                table.cards.append(player.cards[card_num])
                del player.cards[card_num]
                interface_total(B = show, T = table.cards, P = player.cards)
                print("Upgrade the rank of Boss needs %d coins." %(boss.upgrade_coin))
                print("%d coins are still on your hand." %(player.coin))
                print("-----------------------")
                
            elif do_sth == "S":
                card_start = require(parser_start, "Which card do you want to move on the table?")
                card_end = require(parser_end, "Which site do you want to move to the table?")
                table.change(card_start, card_end)
                interface_total(B = show, T = table.cards, P = player.cards)
                print("Upgrade the rank of Boss needs %d coins." %(boss.upgrade_coin))
                print("%d coins are still on your hand." %(player.coin))
                print("-----------------------")
                
            elif do_sth == "U":
                player.coin -= boss.upgrade_coin
                boss.rank_upgrade()
                interface_total(B = show, T = table.cards, P = player.cards)
                print("Upgrade the rank of Boss needs %d coins." %(boss.upgrade_coin))
                print("%d coins are still on your hand." %(player.coin))
                print("-----------------------")

            elif do_sth == "R":
                player.coin -= 1
                show = boss.show()
                interface_total(B = show, T = table.cards, P = player.cards)
                print("Upgrade the rank of Boss needs %d coins." %(boss.upgrade_coin))
                print("%d coins are still on your hand." %(player.coin))
                print("-----------------------")

            else:
                break

    while player_one.blood != 0 and player_two.blood != 0:
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
        
        if who_win == "self":
            player_two.blood -= card_damage + boss_one.rank
        
        elif who_win == "op":
            player_one.blood -= card_damage + boss_two.rank
           
        else:
            pass