osszes_masodperc = int(input("Összesen hány másodperc? "))
orak = osszes_masodperc // 3600
megmaradt_masodpercek = osszes_masodperc % 3600
percek = megmaradt_masodpercek // 60
megmaradt_masodpercek_a_vegen = megmaradt_masodpercek % 60
6
7
8
print("Órák=", orak, " Percek=", percek,
" Másodpercek=", megmaradt_masodpercek_a_vegen)
