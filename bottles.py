def bottle_song(num):
	for x in reversed(range(num)):
		if(x > 1):
			print(f"{x} bottles of beer on the wall, {x} bottles of beer. Take one down and pass it around,{x - 1} bottles of beer on the wall.")
			x -= 1
		elif(x == 1):
			print("1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.")
			x -= 1
		else:
			print("No more bottles of beer on the wall, no more bottles of beer.")

bottle_song(100)
