from Game_HS import *

# card_1_01 = BuffedCard("巷弄小貓", 1, 1, 1, species = "Beast", )
# card_1_02 = BuffedCard("惡魔僕從", 1, 2, 1, species = "Demon", )
# card_1_03 = BuffedCard("機械袋鼠", 1, 1, 1, species = "Mech", )
card_1_04 = BuffedCard("正義保衛者", 1, 1, 1, shield = True, taunt = True)
# card_1_05 = BuffedCard("無私的英雄", 1, 2, 1,)
# card_1_06 = BuffedCard("獵潮魚人", 1, 2, 1, species = "Murloc", )
card_1_07 = BuffedCard("石塘獵人", 1, 2, 3, species = "Murloc", battle_cry = BuffCry(attack = 1, health = 1, species = ("Murloc", 1)))
card_1_08 = BuffedCard("粗鄙的魔胎", 1, 2, 4,species = "Demon", taunt = True, battle_cry = BuffCry(health = -1, species = ("Player", 1)))
# card_1_09 = BuffedCard("食腐土狼", 1, 2, 2, species = "Beast", )
# card_1_10 = BuffedCard("魚人招潮者", 1, 1, 2, species = "Murloc", )
# card_1_11 = BuffedCard("微型裝甲", 1, 1, 2, species = "Mech", )
# card_1_12 = BuffedCard("海上無賴", 1, 2, 1, species = "Pirate", )
card_1_13 = BuffedCard("甲板菜鳥", 1, 2, 4, species = "Pirate", battle_cry = BuffCry(upgrade_coin = -1, species = ("Boss", 1)))
# card_1_14 = BuffedCard("紅色幼龍", 1, 1, 2, species = "Dragon", )
# card_1_15 = BuffedCard("織怒者" , 1, 1, 1, )
card_1_16 = BuffedCard("龍裔副官", 1, 2, 3, taunt = True)


# card_2_01 = BuffedCard("不穩定的食屍鬼", 2, 1, 3, taunt = True, )
# card_2_02 = BuffedCard("南海船長", 2, 3, 3, species = "Pirate", )
# card_2_03 = BuffedCard("恩若司之子", 2, 2, 2, )
# card_2_04 = BuffedCard("慈祥的外婆", 2, 1, 1, species = "Beast", )
# card_2_05 = BuffedCard("炸彈機器人", 2, 2, 2, species = "Mech", )
# card_2_06 = BuffedCard("老瞎眼", 2, 2, 4, species = "Murloc", )
card_2_07 = BuffedCard("鋼牙獸", 2, 3, 3, species = "Mech", battle_cry = BuffCry(attack = 2, species = ("Mech", 100)))
# card_2_08 = BuffedCard("魚人隊長", 2, 3, 3, species = "Murloc", )
# card_2_09 = BuffedCard("麥田魔像", 2, 2, 3, species = "Mech", )
# card_2_10 = BuffedCard("保本賭客", 2, 3, 3, species = "Pirate", )
card_2_11 = BuffedCard("展覽廳茶杯", 2, 2, 2, battle_cry = BuffCry(attack = 1, health = 1, species = ("Random", 3)))
# card_2_12 = BuffedCard("時間服務員", 2, 3, 4, species = "Dragon", )
# card_2_13 = BuffedCard("染病的尖角蜥", 2, 4, 2, species = "Beast", )
# card_2_14 = BuffedCard("獸群領袖", 2, 3, 3, )
card_2_15 = BuffedCard("納斯雷茲姆監督者", 2, 2, 3, species = "Demon", battle_cry = BuffCry(attack = 2, health = 2, species = ("Demon", 1)))
# card_2_16 = BuffedCard("結界守護者", 2, 2, 4, species = "Dragon", )
# card_2_17 = BuffedCard("蠟騎士托戈瓦哥", 2, 1, 2, )
card_2_18 = BuffedCard("蹦蹦兔", 2, 1, 1, species = "Mech", battle_cry = BuffCry(attack = 2, health = 2, species = ("Me", 1)))
# card_2_19 = BuffedCard("鬼卒", 2, 3, 3, species = "Demon", taunt = True, )


card_3_01 = BuffedCard("冷光先知", 3, 2, 3, species = "Murloc", battle_cry = BuffCry(health = 2, species = ("Murloc", 100)))
# card_3_02 = BuffedCard("卡德加", 3, 2, 2, )
# card_3_03 = BuffedCard("合體威脅者", 3, 3, 1, species = "Mech", )
# card_3_04 = BuffedCard("大明星", 3, 4, 4, )
# card_3_05 = BuffedCard("小鬼幫派老大", 3, 2, 4, species = "Demon", )
# card_3_06 = BuffedCard("感染的狼", 3, 3, 3, species = "Beast", )
# card_3_07 = BuffedCard("比斯巨獸", 3, 9, 7, species = "Beast", )
card_3_08 = BuffedCard("破舊的維修機甲", 3, 2, 5, species = "Mech", battle_cry = BuffCry(attack = 2, health = 2, species = ("Mech", 1)))
card_3_09 = BuffedCard("編晶師", 3, 5, 4, battle_cry = BuffCry(attack = 1, health = 1, species = ("Demon", 100)))
card_3_10 = BuffedCard("訓犬者", 3, 4, 3, battle_cry = BuffCry(attack = 2, health = 2, taunting = True, species = ("Beast", 1)))
card_3_11 = BuffedCard("魔鰭領航員", 3, 4, 4, species = "Murloc", battle_cry = BuffCry(attack = 1, health = 1, species = ("Murloc", 100)))
# card_3_12 = BuffedCard("鼠黨老大", 3, 2, 2, species = "Beast", )
# card_3_13 = BuffedCard("偏斜防護機器人", 3, 2, 3, species = "Mech", shield = True, )
# card_3_14 = BuffedCard("唷齁巨魔", 3, 2, 8, species = "Pirate", taunt = True, )
# card_3_15 = BuffedCard("怒吃龍", 3, 4, 4, species = "Dragon", )
# card_3_16 = BuffedCard("恐怖的鸚鵡", 3, 4, 3, species = "Beast", )
card_3_17 = BuffedCard("暮光使者", 3, 4, 4, species = "Dragon", taunt = True, battle_cry = BuffCry(attack = 2, health = 2, species = ("Dragon", 1)))
# card_3_18 = BuffedCard("有駕駛的伐木機", 3, 4, 3, species = "Mech", )
# card_3_19 = BuffedCard("老練的強奪者", 3, 3, 3, species = "Pirate", )
card_3_20 = BuffedCard("血帆火炮手", 3, 4, 2, species = "Pirate", battle_cry = BuffCry(attack = 3, species = ("Pirate", 100)))
# card_3_21 = BuffedCard("變換者澤魯斯", 3, 1, 1, )
# card_3_22 = BuffedCard("靈魂飛刀手", 3, 3, 3, )
# card_3_23 = BuffedCard("青銅守望者", 3, 2, 1, species = "Dragon", shield = True, )


# card_4_01 = BuffedCard("『龍焰之血』伯瓦爾", 4, 1, 7, shield = True, )
# card_4_02 = BuffedCard("保全單輪機器人", 4, 2, 6, species = "Mech", )
card_4_03 = BuffedCard("兔夭師尊", 4, 4, 5, battle_cry = BuffCry(attack = 2, health = 2, species = ("Beast", 1)))
# card_4_04 = BuffedCard("攻城魔", 4, 5, 8, species = "Demon", taunt = True, )
# card_4_05 = BuffedCard("機械蛋" , 4, 0, 8, species = "Mech", )
card_4_06 = BuffedCard("毒鰭魚人", 4, 1, 2, species = "Murloc", battle_cry = BuffCry(poisoning = True))
# card_4_07 = BuffedCard("洞穴多頭蛇", 4, 2, 4, species = "Beast", )
# card_4_08 = BuffedCard("漂浮看守者", 4, 4, 4, species = "Demon", )
# card_4_09 = BuffedCard("煩人模組", 4, 2, 4, species = "Mech", shield = True, taunt = True, )
# card_4_10 = BuffedCard("鈷藍逆鱗龍人", 4, 5, 5, species = "Dragon", )
# card_4_11 = BuffedCard("鋼鐵師尊", 4, 2, 2, species = "Mech", )
# card_4_12 = BuffedCard("長鬃草原獅", 4, 6, 5, species = "Beast", )
card_4_13 = BuffedCard("阿古斯防衛者", 4, 2, 3, battle_cry = BuffCry(attack = 1, health = 1, taunting = True, species = ("next", 1)))
# card_4_14 = BuffedCard("利普斯納爾船長", 4, 3, 4, species = "Pirate", )
card_4_15 = BuffedCard("南海惡棍", 4, 5, 4, species = "Pirate", battle_cry = BuffCry(attack = 1, health = 1, species = ("Pirate", 1)))
# card_4_16 = BuffedCard("原魚偵查兵", 4, 3, 2, species = "Murloc", )
card_4_17 = BuffedCard("展覽廳茶壺", 4, 3, 3, battle_cry = BuffCry(attack = 2, health = 2, species = ("Random", 3)))
# card_4_18 = BuffedCard("掘金工", 4, 2, 2, species = "Pirate", )
# card_4_19 = BuffedCard("火焰使者", 4, 5, 6, species = "Dragon", )
# card_4_20 = BuffedCard("龍獸執法者", 4, 3, 6, species = "Dragon", )


# card_5_01 = BuffedCard("布萊恩。銅鬚", 5, 2, 4, )
# card_5_02 = BuffedCard("拾荒機器人", 5, 1, 5, species = "Mech", )
# card_5_03 = BuffedCard("瑞文戴爾男爵", 5, 1, 7, )
# card_5_04 = BuffedCard("瑪爾加尼斯", 5, 9, 7, species = "Demon")
card_5_05 = BuffedCard("硬殼拾荒者", 5, 2, 3, battle_cry = BuffCry(attack = 2, health = 2, species = ("is_taunt", 100)))
# card_5_06 = BuffedCard("虛無領主", 5, 3, 9, species = "Demon", taunt = True, )
# card_5_07 = BuffedCard("鐵皮恐角龍", 5, 7, 7, species = "Beast", )
# card_5_08 = BuffedCard("光牙執法者", 5, 2, 2, )
# card_5_09 = BuffedCard("吧嘎咕王", 5, 6, 3, species = "Murloc", battle_cry = BuffCry(attack = 2, health = 2, species = ("Murloc", 100)), )
# card_5_10 = BuffedCard("姆多茲諾", 5, 5, 5, species = "Dragon", )
card_5_11 = BuffedCard("安尼希蘭戰鬥大師", 5, 3, 1, species = "Demon", battle_cry = BuffCry(health = 1, species = ("Me", 1)))
# card_5_12 = BuffedCard("斯尼德的伐木機", 5, 5, 7, species = "Mech", )
# card_5_13 = BuffedCard("極限釣手納特。帕格", 5, 8, 5, species = "Pirate", )
# card_5_14 = BuffedCard("熊媽媽", 5, 4, 4, species = "Beast", )
# card_5_15 = BuffedCard("狂野的拉佐格爾", 5, 2, 4, species = "Dragon", )
# card_5_16 = BuffedCard("破浪巨人", 5, 6, 7, species = "Pirate", )
# card_5_17 = BuffedCard("霍格爾船長", 5, 6, 6, species = "Pirate", )


# card_6_01 = BuffedCard("敵人收割者四千", 6, 6, 9, species = "Mech", )
card_6_02 = BuffedCard("梅克斯娜", 6, 2, 8, species = "Beast", poisonous = True)
# card_6_03 = BuffedCard("『巨狼先祖』戈德林", 6, 4, 4, species = "Beast", )
# card_6_04 = BuffedCard("『祕法巨龍』卡雷苟斯", 6, 4, 12, species = "Dragon", )
# card_6_05 = BuffedCard("『紅袍』納蒂娜", 6, 7, 4, )
# card_6_06 = BuffedCard("剃浪號", 6, 6, 4, )
# card_6_07 = BuffedCard("崗古的學徒", 6, 3, 6, )
# card_6_08 = BuffedCard("恐怖的巨蛇", 6, 7, 7, species = "Beast", )
# card_6_09 = BuffedCard("末日聚合體", 6, 6, 6, species = "ALL", battle_cry = BuffCry())
# card_6_10 = BuffedCard("札普。狡芯", 6, 7, 10, windfury = True, )
# card_6_11 = BuffedCard("驚懼上將伊莉莎", 6, 6, 7, )
card_6_12 = BuffedCard("鬼母", 6, 6, 10, )

# ==========================================================================================

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

# ==========================================================================================

card_rank1 = [card11, card12, card11, card12]
card_rank2 = [card21, card22, card21, card22]
card_rank3 = [card32, card33, card32, card33]
card_rank4 = [card41, card42, card43, card44]
card_rank5 = [card52, card53, card52, card53]
card_rank6 = [card61, card62, card63, card64]

card_rank = [card_rank1, card_rank2, card_rank3, card_rank4, card_rank5, card_rank6]

Hearthstone(card_rank)
