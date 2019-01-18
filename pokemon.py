import time
import random

print()
print('-' * 65)
print()

print('A wild MewTwo appears!')
time.sleep(0.7)
print('...the background music changes...')
time.sleep(0.7)
print('You only have one Pokemon, Pachirisu')
time.sleep(0.7)
print('I choose you Pacharisu!!!')
time.sleep(0.7)
print()

#set the starting health values
Pacharisu_hp = 250
MewTwo_hp =400

#display the current healths
print('Starting HP:')
time.sleep(0.3)
print('Pacharisu HP:' + str(pacharisu_hp))
time.sleep(0.3)
print('MewTwo HP:' + str(mewTwo_hp))
time.sleep(0.3)
print()

print('Choose your battle move')
time.sleep(0.7)
print('- [1] Tackle')
time.sleep(0.7)
print('- [2] Screech')
time.sleep(0.7)
print('- [3] Absorb')
time.sleep(0.7)
print('- [4] Hotbox')
time.sleep(0.7)
print('- [5] Capture')
time.sleep(0.7)
print()

player_move = input('Pick a move using the corresponding number')
player_move = int(player_move)
if player_move == 1:
	print('Pacharisu uses Tackle and deals 25 HP of damage to MewTwo.')
elif player_move == 2:
	damage = random.rindint(5,40)
	MewTwo_hp = MewTwo_hp -25
	print('Pacharisu uses Screech and deals' + str(damage) + 'HP of damage')
elif player_move == 3:
	Pacharisu_hp = Pacharisu_hp + 100
	print('Pacharisu uses Absorb and recovers 100 HP.')
elif player_move == 4:
	Pacharisu_hp = Pacharisu_hp + 25
	MewTwo_hp = MewTwo_hp -10
	print('Pacharisu uses hotbox and recovers 25 HP while dealing 10 HP to MewTwo!')
elif player_move == 5:
	capture_roll = random.randint(0,170)
	if capture_roll > MewTwo_hp:
		print('You have captured MewTwo!')
		break
	else:
		print('You have tried to capture MewTwo but failed!')

	# enemy battle choices
	enemy_move = random.randint(1,2)
	if enemy_move == 1:
		Pacharisu_hp = Pacharisu_hp - 20
		print('MewTwo uses Confuse and deals 20 HP to Pacharisu!')
	elif enemy_move == 2:
		Pacharisu_hp = Pacharisu_hp - 50
		print('MewTwo uses strong pucng and deals 50 HP to Pacharisu!')

	time.sleep(0.3)
	print()

	#check and avoid negative HP
	if Pacharisu_hp < 0:
		Pacharisu_hp = 0

	if MewTwo_hp < 0:
		MewTwo_hp = 0


