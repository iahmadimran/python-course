import os
from datetime import datetime

os.chdir('/Users/user/OneDrive/Desktop/')

# Writing files on the desktop
# os.mkdir('demo.txt')
# os.makedirs('test/test.txt')

# Removing files on the desktop
# os.rmdir('test')
# os.removedirs('demo.txt')

# Renaming the name of directory
# os.rename('ai_engineer_roadmap_2025_v2.pdf', 'ai-engineer-codebasics-roadmap.pdf')

# Datetime module with os.stat
# mod_time = os.stat('ai-engineer-codebasics-roadmap.pdf').st_mtime
# print(datetime.fromtimestamp(mod_time))

# Walking through all the files in the operating systems
# for dirpath, dirnames, filenames in os.walk('/Users/user/OneDrive/Desktop/'):
#   print('Directories:', dirpath)
#   print('Directory Names:', dirnames)
#   print('File:', filenames)

# Getting environment variables using os.environ
# print(os.environ.get('HOMEPATH'))

# Joining files through os.path.join()
# file_path = os.path.join(os.environ.get('HOMEPATH'), 'demo.txt')

# Exploring os.path methods
# print(os.path.splitext('/tmp/test.txt'))

# print(dir(os.path))
# print(os.listdir())