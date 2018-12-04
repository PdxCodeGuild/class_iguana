import random

# Program fails if user does not input correct amount of commas during multi-responses
# Solution: Compare list length to number of expected values. Ask for additional values in the quantity of: (expected values - list length)

def get_words():
      words = []

      print("Please separate words with commas")
      adjectives = (str.split(input("Enter two adjectives: "), ","))
      nouns = (str.split(input("Enter five nouns: "), ","))
      verbs = (str.split(input("Enter two verbs ending in 'ing': "), ","))
      words.append(input("Enter a room in a house: "))
      words.append(input("Enter a verb (past tense): "))
      words.append(input("Enter a verb (present tense): "))
      words.append(input("Enter a relatives name: "))
      words.append(input("Enter a body part (plural): "))

      random.shuffle(adjectives)
      random.shuffle(nouns)
      random.shuffle(verbs)

      i = True
      while i == True:
            story = input("\n\nWould you like to hear the story? y/n\t")

            if story == "y":
                  get_story(adjectives, nouns, verbs, words)
            elif story == "n":
                  i = False
            else:
                  print("Not a valid response. Type 'y' or 'n' ")

def get_story(adjectives, nouns, verbs, words):
      print("\nIt was a " + adjectives[0] + ", cold December day. I woke up to the " + adjectives[1].replace(" ", "") +
            " smell of " + nouns[0] + " roasting in the " + words[0] + " downstairs.\nI " + words[1].replace(" ", "") +
            " down the stairs to see if I could help " + words[2].replace(" ", "") + " the dinner. My mom said, 'See if "
            + words[3].replace(" ", "") + " needs a fresh " + nouns[1].replace(" ", "") + "'.\nSo I carried a tray of "
            "glasses full of " + nouns[2].replace(" ", "") + " into the room. When I got there, I couldn't believe my " +
            words[4].replace(" ", "") + "! \nThere were " + nouns[3].replace(" ", "") + "s " + verbs[1].replace(" ", "") +
            " on the " + nouns[4].replace(" ", "") + "!\n")

      i = True
      while i == True:
            story = input("\n\nWould you like to hear the story again? y/n\t")

            if story == "y":
                  get_story(adjectives, nouns, verbs, words)
            elif story == "n":
                  i = False
            else:
                  print("Not a valid response. Type 'y' or 'n' ")

      j = True
      while j == True:
            story = input("\n\nWould you like to create another story? y/n\t")

            if story == "y":
                  get_words()
            elif story == "n":
                  exit()
            else:
                  print("Not a valid response. Type 'y' or 'n' ") 

get_words()

