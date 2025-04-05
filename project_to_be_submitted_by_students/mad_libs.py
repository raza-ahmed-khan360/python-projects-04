def get_input(prompt):
    return input(prompt)

def generate_story(noun, verb, adjective, adverb):
    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."
    return story

def main():
    noun = get_input("Enter a noun: ")
    verb = get_input("Enter a verb: ")
    adjective = get_input("Enter an adjective: ")
    adverb = get_input("Enter an adverb: ")

    story = generate_story(noun, verb, adjective, adverb)
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()
