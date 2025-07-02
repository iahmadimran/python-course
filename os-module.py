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

# print(os.listdir())