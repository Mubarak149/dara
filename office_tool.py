import random
import time
#wara!! wara!!! wara!!!!!!
abun_zaba = ["jirgi","mota","mashin","keke"]

print("zaba Achikin wadannan")
print(f""" 
1.	{abun_zaba[0]}
2.	{abun_zaba[1]}
3.	{abun_zaba[2]}
4.	{abun_zaba[3]}
""")
na_zaba = int(input("shigar da zabin ka: "))
zabin_mutum = abun_zaba[na_zaba-1]
abun_zaba.remove(zabin_mutum)
zabin_computer = ''
adadin_yatsu = ''
adadin_yatsu_na_computer = 0
sun_zaba = False
wasa_ya_fara = False
while True:
	if na_zaba == 1 and not sun_zaba:
		print(f"ka zaba {zabin_mutum}\n")
		print("sauran computer..........")
		time.sleep(0.5)
		zabin_computer = random.choice(abun_zaba)
		print(f"computer: na zaba {zabin_computer}")
		sun_zaba = True
		
	if na_zaba == 2 and not sun_zaba:
		print(f"ka zaba {zabin_mutum}\n")
		print("sauran computer..........")
		time.sleep(0.5)
		zabin_computer = random.choice(abun_zaba)
		print(f"computer: na zaba {zabin_computer}")
		sun_zaba = True
	if na_zaba == 3 and not sun_zaba:
		print(f"ka zaba {zabin_mutum}\n")
		print("sauran computer..........")
		time.sleep(0.5)
		zabin_computer = random.choice(abun_zaba)
		print(f"computer: na zaba {zabin_computer}")
		sun_zaba = True
	if na_zaba == 4 and not sun_zaba:
		print(f"ka zaba {zabin_mutum}\n")
		print("sauran computer..........")
		time.sleep(0.5)
		zabin_computer = random.choice(abun_zaba)
		print(f"computer: na zaba {zabin_computer}")
		sun_zaba = True
	#filin wasa
	if not wasa_ya_fara:
		print("\n************* wasa zai fara ************\n")
		wasa_ya_fara = True
		
	adadin_yatsu = int(input("\nshigar da adadin yatsu: "))
	adadin_yatsu_na_computer = random.randint(1,len(abun_zaba))
	if adadin_yatsu > 5:
		print("yatsun ka basu wuche biyar bah")
		
	duka_yatsu = adadin_yatsu + adadin_yatsu_na_computer
	print("\nadadin yatsun ku shine: " + str(duka_yatsu))
	 
	