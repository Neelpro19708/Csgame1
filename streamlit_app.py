import streamlit as st
import random

# A simple list of words to pick from
word_bank = (
    "apple", "planet", "guitar", "castle", "jungle",
    "puzzle", "rocket", "dragon", "bridge", "island",
    "shadow", "thunder", "diamond", "rainbow", "volcano",
    "penguin", "dolphin", "elephant", "kangaroo", "cheetah",
    "whisper", "mystery", "treasure", "adventure", "journey",
    "library", "blanket", "candle", "bicycle", "backpack",
    "chocolate", "sandwich", "popcorn", "pancake", "spaghetti",
    "tornado", "hurricane", "earthquake", "avalanche", "blizzard",
    "triangle", "rectangle", "octagon", "cylinder", "pyramid",
    "computer", "keyboard", "headphones", "internet", "satellite",
    "astronaut", "galaxy", "universe", "meteor", "eclipse",
    "flamingo", "peacock", "squirrel", "hedgehog", "octopus",
    "crocodile", "butterfly", "ladybug", "grasshopper", "firefly",
    "mountain", "waterfall", "desert", "glacier", "canyon",
    "football", "basketball", "baseball", "volleyball", "badminton",
    "kingdom", "wizard", "vampire", "monster", "phantom",
    "curious", "fantastic", "invisible", "mysterious", "brilliant",
    "oxygen", "gravity", "magnet", "energy", "electricity",
    "sandcastle", "lighthouse", "skyscraper", "submarine", "helicopter",
    "calendar", "envelope", "scissors", "thermometer", "telescope"
)

def reset_game():
    st.session_state.word = random.choice(word_bank)
    st.session_state.guessed_letters = set()
    st.session_state.lives = 6
    st.session_state.status = "playing"

if "word" not in st.session_state or "status" not in st.session_state:
    reset_game()

def guess_letter(letter):
    if st.session_state.status != "playing":
        return

    if letter in st.session_state.guessed_letters:
        return

    st.session_state.guessed_letters.add(letter)

    if letter not in st.session_state.word:
        st.session_state.lives -= 1

    if st.session_state.lives <= 0:
        st.session_state.status = "lost"
    elif all(l in st.session_state.guessed_letters for l in st.session_state.word):
        st.session_state.status = "won"

st.title("🎯 Streamlit Hangman")
st.write("Guess the word by clicking the buttons below. You have 6 lives!")

display = [l if l in st.session_state.guessed_letters else "_" for l in st.session_state.word]
st.header(" ".join(display))
st.write(f"❤️ Lives left: **{st.session_state.lives}**")

if st.session_state.status == "won":
    st.success(f"🎉 You won! The word was '{st.session_state.word}'!")
elif st.session_state.status == "lost":
    st.error(f"💀 Game over! The word was '{st.session_state.word}'.")

# 3-row side-by-side alphabet grid (9 buttons per row)
alphabet = "abcdefghijklmnopqrstuvwxyz"
cols = st.columns(9)

for index, letter in enumerate(alphabet):
    col = cols[index % 9]
    col.button(
        letter,
        key=letter,
        disabled=(letter in st.session_state.guessed_letters) or (st.session_state.status != "playing"),
        on_click=guess_letter,
        args=(letter,),
        use_container_width=True
    )

st.write("---")
st.button("Reset Game", on_click=reset_game)