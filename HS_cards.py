def card_row1(card = 0, END = True):
    if END == True:
        print("╔═══╦══════════════════════╗")
    else:
        print("╔═══╦══════════════════════╗", end = "")
        
def card_row2(card = 0, END = True):
    if END == True:
        print("║ %d ║ %s ║" %(6,"『祕法巨龍』卡雷苟斯"))
    else:
        print("║ %d ║ %s ║" %(6,"『祕法巨龍』卡雷苟斯"), end = "")
        
def card_row3(card = 0, END = True):
    if END == True:
        print("╠═══╩══════════════════════╣")
    else:
        print("╠═══╩══════════════════════╣", end = "")
        
def card_row4(card = 0, END = True):
    if END == True:
        print("║   劇毒：✓    聖盾：✓     ║")
    else:
        print("║   劇毒：✓    聖盾：✓     ║", end = "")
        
def card_row5(card = 0, END = True):
    if END == True:
        print("║   風怒：✗    嘲諷：✗     ║")
    else:
        print("║   風怒：✗    嘲諷：✗     ║", end = "")
        
def card_row6(card = 0, END = True):
    if END == True:
        print("║                          ║")
    else:
        print("║                          ║", end = "")
        
def card_row9(card = 0, END = True):
    if END == True:
        print("╠════════════╦═════════════╣")
    else:
        print("╠════════════╦═════════════╣", end = "")
              
def card_row10(card = 0, END = True):
    if END == True:
        print("║ Attack=%d ║  Health=%d ║" %(100,100))
    else:
        print("║ Attack=%d ║  Health=%d ║" %(100,100), end = "")
        
def card_row11(card = 0, END = True):
    if END == True:
        print("╚════════════╩═════════════╝")
    else:
        print("╚════════════╩═════════════╝", end = "")
    
def print_table(card1 = 0, END1 = False, card2 = 0, END2 = True):
    card_row1(card1, END1)
    card_row1(card1, END1)
    card_row1(card1, END1)
    card_row1(card1, END1)
    card_row1(card2, END2)
    card_row2(card1, END1)
    card_row2(card2, END2)
    card_row3(card1, END1)
    card_row3(card2, END2)
    card_row4(card1, END1)
    card_row4(card2, END2)
    card_row5(card1, END1)
    card_row5(card2, END2)
    card_row6(card1, END1)
    card_row6(card2, END2)
    card_row6(card1, END1)
    card_row6(card2, END2)
    card_row6(card1, END1)
    card_row6(card2, END2)
    card_row9(card1, END1)
    card_row9(card2, END2)
    card_row10(card1, END1)
    card_row10(card2, END2)
    card_row11(card1, END1)
    card_row11(card2, END2)

print_table()