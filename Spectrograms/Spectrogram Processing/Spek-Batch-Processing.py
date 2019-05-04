import subprocess
import os
import pyautogui
import time

def grab():
	print('Please import filepath for batch-process.')
	filepath = input()
	return str(filepath)

def main():
	#Grab Filepath for Batch Processing
	filepath = grab()

	#Loop through all files in directory
	for root, dir, files, in os.walk(filepath):
		for file in files:
			#Find File Path of Song (need to not hard code)
			song_filepath =  filepath +'\\' + str(file)
			print('Processing: ', song_filepath)

			#Call Spek with that filepath

			subprocess.Popen([r'C:\Program Files (x86)\Spek\Spek.exe', song_filepath])

			#subprocess.Popen([r'C:\Users\spitf_000\Downloads\spek-0.8.2\Spek\spek.exe', fp])

			
			#Implementing adaptive wait time based on file size
			file_size = os.stat(fp).st_size
			print(file_size)
			wait_time = (file_size/1000000)/2
			time.sleep(wait_time)			
			
			#Setting SAFE pyautogui
			#Can tune once the rest is stable
			pyautogui.FAIL_SAFE = True
			pyautogui.PAUSE = 0.5

			#Key Presses to Save each file
			pyautogui.hotkey('ctrl', 's')
			pyautogui.press('enter')
			pyautogui.hotkey('alt', 'f4')
			






if __name__ == '__main__':
	main()
