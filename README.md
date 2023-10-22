# Uwuifier
This project is written mainly for learning Python myself. Does exactly what it say on the tin (UwU~ifies text you write). Needs Pyperclip to be installed for script to run (in CMD, run `pip install pyperclip`). Other than that, it uses everything built in Python 3.11 exports.
## Dictionary System (killer feature of my version)
It has a flexible dictionary system, from which it replaces letters (letter=>replacement), words (words=>synonyms), also adds 'ending' at the end of sentence, and an 'emoticon' at the new line.
You can easily edit dictionaries by adding new entries as text in new lines.
![image](https://github.com/BedrockDotWebp/Uwuifier/assets/144620948/3b26c516-1f50-40f2-9cc3-3f6b12beea7a)
## Arguments (inspired by StarrFox's version)
If you find the text sound annoying, you can use arguments to dampen it out (available arguments as of now):

`--disable-statter: exactly what it says on the tin - lets your character have statter-free days`

`--disable-emotes: for those annoyed by emoticons your character says out, this is PARADISE!`

To pass them, you need to run the program in CMD that works SPECIFICALLY in the program path, as dictionary files are needed to run the program... or you can just run CMD files (as for prebuilt)

## Running
There are various ways of running the program:

#### 1) Directly via .py script (you also need to install Python for this to work (a bit harder, but gives you a lot more flexibility for passing arguments in the future)):
Download the code as ZIP (or you can also "git clone" the repo to omit extracting the files), extract it somewhere and run `python uwuify.py [optional arguments]` and of course it has to be run SPECIFICALLY in the program path (where you unpacked it).
#### 2) Prebuilt (Windows only)
Find the 7Z-archive in the latest release (https://github.com/BedrockDotWebp/Uwuifier/releases/latest), and download it to extract somewhere. After this, you can either run the program in that extracted folder or pass arguments via CMD files that are included.

## Inspiration
Initial inspiration by https://github.com/anstropleuton for his C++ version of UwU~ifier. Also thanks for inspiration for arguments to https://github.com/StarrFox.
