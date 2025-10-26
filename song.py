import time
import sys

def type_lyrics(text, speed=0.05):
    """Prints text like typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # new line after each lyric

def print_lyrics():
    lyrics = [
        "Haathon ko sambhale mere haathon mai",
        "Kaise haathon ko sambhale mere haathon mein",
        "jab tak neend na aaye in laakeron mai",
        "Baatein hon....",

        "Haayeeee...."
    ]

    delays = [2.0, 1.8, 2.1, 2.4,1.7
              ]
    print('')
    print('Arz kiya hai lyrics:\n')
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        type_lyrics(line)
        time.sleep(delays[i])

# Call function
print_lyrics()