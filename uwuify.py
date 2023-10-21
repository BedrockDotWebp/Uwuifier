import random
import pyperclip
import os
import io
import sys

# Set terminal size
cmd = 'mode 128,4'
os.system(cmd)
program_version = "v1.1"


def loopback():
    # Very rare occasion makes the character deadlocked
    # if given number is 1/1000, give it infinite stutter, so it'll get banned for spamming (just joking)

    # Check for arguments
    argumental = sys.argv
    if "--help" in argumental:
        cmd = 'mode 120,30'
        os.system(cmd)
        print("UwU~ifier", program_version)
        print("Made by Bedrock")
        print("Arguments:")
        print("--disable-statter: exactly what it says on the tin - lets your character have statter-free days")
        print("--disable-emotes: for those annoyed by emoticons your character says out, this is PARADISE!")
        os.system('pause')
        quit()

    if "--disable-statter" in argumental:
        statter = 0
    else:
        statter = 1
    if "--disable-emotes" in argumental:
        emotes = 0
    else:
        emotes = 1

    # Instantiate the sentence and save the original
    sentence = input("Enter message?: \n")
    sentence_original = sentence

    # Various checks

    if len(sentence) == 0:
        print("Empty text.")
        loopback()

    if sentence[0] == "\\":
        print("Illegal symbol.")
        loopback()

    # lowercasing the damn thing
    sentence = sentence.lower()

    # synonymizing the speech
    f = io.open("words", encoding="utf-8")
    lines = f.read()
    words = lines.split("\n")
    f.close()

    f = io.open("synonyms", encoding="utf-8")
    lines = f.read()
    synonyms = lines.split("\n")
    f.close()

    for x in range(0, len(words)):
        sentence = sentence.replace(words[x], synonyms[x])

    # wepwacing wettews

    f = io.open("letter", encoding="utf-8")
    lines = f.read()
    letter = lines.split("\n")
    f.close()

    f = io.open("replacement", encoding="utf-8")
    lines = f.read()
    replacement = lines.split("\n")
    f.close()

    for x in range(0, len(letter)):
        sentence = sentence.replace(letter[x], replacement[x])

    # s- s- statter
    repetitions = random.randrange(0, 4)
    scat = sentence[0] + '- '

    # emoticon s-so cute uwu
    f = io.open("ending", encoding="utf-8")
    lines = f.read()
    ending = lines.split("\n")
    f.close()

    end_index = random.randrange(0, len(ending))

    f = io.open("emoticon", encoding="utf-8")
    lines = f.read()
    emoticon = lines.split("\n")
    f.close()

    variation = random.randrange(0, len(emoticon))

    # convert result to variable for both "print" and "copy"
    result = (statter * scat * repetitions) + sentence + ending[end_index] + "\n" + (emotes * (emoticon[variation]))

    print(result)
    pyperclip.copy(result + "\n(Original: " + sentence_original + ")")
    loopback()


loopback()
