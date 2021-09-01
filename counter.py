circumfrence = input("what is the circumfrence? ")
height = input("how many rows did you count? ")
volume = ((int(circumfrence)/6.28)**2)*3.14*int(height)
print ("There are approximately "+str(round(volume, 2))+" things in your container based on your estimation.")
