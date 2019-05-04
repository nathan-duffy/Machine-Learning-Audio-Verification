import os

def main():
	#Creating array to store songs
	song_titles = []

	for file in os.listdir(r'C:\DJ Music\HDD Recovery'):
		song_titles.append(file)

	#Writing to txt file 
	with open('song_titles.txt', 'w') as f:
		for song in song_titles:
			f.write("%s\n" % song)

	#Finding all the finished songs
#	for file in os.listdir(r'C:\Users\spitf_000'):
#		if file.endswith(".png"):
#			clean_file = file.replace('png','')
#			finished_songs.append(clean_file)

#	print(finished_songs)
	#Writing to txt file 
#	with open('song_list.txt', 'w') as f:
#		for song in finished_songs:
#			f.write("%s\n" % song)

#	with open('song_list.txt', 'w') as f:
#		for song in finished_songs:
#			print(song)


if __name__ == '__main__':
  main()