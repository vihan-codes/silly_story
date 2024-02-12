import streamlit as st
import random

def generate_silly_story():
    nouns = ["dog", "wizard", "banana", "treehouse", "robot"]
    verbs = ["ran", "jumped", "exploded", "sang", "teleported"]
    adjectives = ["grumpy", "sparkly", "fuzzy", "gigantic", "invisible"]

    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)

    story = f"The {adjective} {noun} {verb} down the street!"
    return story

def main():
    st.title("Silly Story Generator")
    st.button("Generate a Story", on_click=display_story)

def display_story():
    story = generate_silly_story()
    st.write(story)

if __name__ == "__main__":
    main()
