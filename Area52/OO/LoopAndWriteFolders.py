import os
class LoopFolders:
	'''
	class LoopFolders

	Loop Folders in given folder.
	print Root folder, sub folders, and files.
	Write output to currentdir\FileList.txt

	*Folders and file exceptions are skipped*
	'''
	def __init__(self, targetFolder):
		self.targetFolder = targetFolder
		print('Target Folder:', targetFolder)

	def loop(self):
		counter = 0
		with open('fileList.txt', 'w') as self.logFile:
			 for root, dirs, files in os.walk(self.targetFolder):
				level = root.replace(self.targetFolder, '').count(os.sep)
				indent = ' ' * 4 * (level)
				print('{}{}/'.format(indent, os.path.basename(root)))
				try:
					self.logFile.write('{}{}{}{}{}'.format(indent,'Map:\n', indent, os.path.basename(root), '\n'))
				except:
					continue
				subindent = ' ' * 4 * (level + 1)
				if any(files):
					self.logFile.write('\tBestanden:\n')
					for f in files:
						print('{}{}'.format(subindent, f))
						try:
							self.logFile.write('{}{}{}'.format(subindent, f, '\n'))
						except:
							print('0101010111000..2... Error... Error...!!!')
							self.logFile.write('\tBestand heeft een identiteitscrisis')
				else:
					self.logFile.write('')
				try:
					self.logFile.write('\n')
				except:
					continue
run = LoopFolders('J:/shared.ond/').loop()
