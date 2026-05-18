import random
exit_index = 0

print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")
msg = input()

while True:
	if msg == "ПОКА!":
		exit_index += 1

		if exit_index == 3:
			print("ДО СВИДАНИЯ, МИЛЫЙ!")
			break

	elif msg != "ПОКА!" and exit_index > 0:
		exit_index = 0

	if msg != "ПОКА!" and msg.isupper():
		print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
		msg = input()
		continue

	print(f"НЕТ, НИ РАЗУ С {random.randint(1930, 1950)} ГОДА!")
	msg = input()
