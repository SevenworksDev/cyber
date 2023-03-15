 ####  #   # #####  ###### #####
#    #  # #  #    # #      #    #
#        #   #####  #####  #    #
#        #   #    # #      #####
#    #   #   #    # #      #   #
 ####    #   #####  ###### #    #

from pick import pick
from zipfile import ZipFile
import os,urllib.request,shutil,time


# Starting Screen
print(" _  |_  _ ._\n(_\/|_)(/_|\n  /\nTool by Sevenworks\nOriginal Bot Code by: Harm\nBuilt with <3 on Python 3.10")
time.sleep(2)
print("[cyber]: starting")

# If the bots folder does not exist, create it
if not os.path.exists("./bots"):
    os.makedirs("./bots")

# Remove Python Cache
if os.path.exists("./bots/__pycache__"):
    shutil.rmtree("./bots/__pycache__")

# Download Bot Library
print("[cyber]: updating bot library")
urllib.request.urlretrieve("http://sevenworks.x10.mx/cyber/bots.zip", "bots.zip") # Download bots.zip

# Extract Bot Library
with ZipFile("./bots.zip", 'r') as zip_ref:
    zip_ref.extractall("./bots")

os.remove("./bots.zip") # Remove bots.zip to clear space
print("[cyber]: finished updating")
time.sleep(1)

# Bot Maker Advertisemnt
print("[cyber]: make your own bot easier at http://sevenworks.x10.mx/botmaker")
time.sleep(1)

# Select Menu
title = ' _  |_  _ ._\n(_\/|_)(/_|\n  /\n\nPlease choose a bot: '
options = os.listdir("./bots") # Get all files from the bots folder
options.remove("bettercomm.py") # Remove the bettercomm library from appearing
option, index = pick(options, title, indicator='»', default_index=1) # Open the bot selector


# Bot Runner
print(f"[cyber]: running {option}")
os.system(f"py ./bots/{option}") # Run the bot selected
