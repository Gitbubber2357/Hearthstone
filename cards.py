from Game_HS import *

card11 = BuffedCard("一星白板", 1, 2, 3, taunt = True)
card12 = BuffedCard("正義保衛者", 1, 1, 1, shield = True, taunt = True)

card21 = BuffedCard("二星白板", 2, 4, 4)
card22 = BuffedCard("鬼卒_改", 2, 3, 4, taunt = True)

card31 = BuffedCard("三星白板", 3, 6, 6)
card32 = BuffedCard("巨魔_改", 3, 2, 8, taunt = True)
card33 = BuffedCard("青銅龍_改", 3, 3, 2, shield = True)

card41 = BuffedCard("四星白板", 4, 8, 7)
card42 = BuffedCard("伯瓦爾_改", 4, 3, 7, shield = True)
card43 = BuffedCard("攻城魔_改", 4, 5, 8, taunt = True)
card44 = BuffedCard("毒魚_改", 4, 1, 2, poisonous = True)

card51 = BuffedCard("五星白板", 5, 10, 10)
card52 = BuffedCard("虛無領主_改", 5, 5, 15, taunt = True)
card53 = BuffedCard("破浪巨人_改", 5, 6, 7, windfury = True)

card61 = BuffedCard("六星白板", 6, 12, 12)
card62 = BuffedCard("梅克斯娜", 6, 2, 8, poisonous = True)
card63 = BuffedCard("札普_改", 6, 7, 10, windfury = True)
card64 = BuffedCard("聚合體_改", 6, 6, 6, poisonous = True, shield = True)

card_rank1 = [card11, card12, card11, card12]
card_rank2 = [card21, card22, card21, card22]
card_rank3 = [card32, card33, card32, card33]
card_rank4 = [card41, card42, card43, card44]
card_rank5 = [card52, card53, card52, card53]
card_rank6 = [card61, card62, card63, card64]

card_rank = [card_rank1, card_rank2, card_rank3, card_rank4, card_rank5, card_rank6]

Hearthstone(card_rank)