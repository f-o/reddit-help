import random

poop = {
    "name": "Katie",
    "age": 21,
    "hobbies": ["some", "hobbies", "you pick"], # Maybe this wont be needed? You decide...
    "emotion": "cheerful",
    "happy_places": ["with Dave"],
    "cuddlebar": "maxed out!"
}
biggestpoop  = {
    "name": "Dave",
    "age": 25,
    "hobbies": ["some", "hobbies", "you pick"], # Maybe this wont be needed? You decide...
    "emotion": "grumpy",
    "happy_places": ["lego", "starwars", "ticklingkatie", "halloween", "scaringkatie"],
    "cuddlebar": "way too low"
}

stages_of_life = ["adult", "slightlywiseradult", "midlifecrisis", "grumpyandgrey", "decrepit", "gengar"]


def always_remember(stage):
    print(stage + "? poop still loves biggestpoop")

def main():
    if biggestpoop["emotion"] == "sad":
        print(random.choice(biggestpoop["happy_places"]))
    elif biggestpoop["cuddlebar"] == "way too low":
        print("give hugs and back strokies")
    else:
        print("booty smack") 

    for stage in stages_of_life:
        always_remember(stage)

if __name__ == "__main__":
    main()