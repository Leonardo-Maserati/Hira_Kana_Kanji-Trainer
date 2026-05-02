import random

# Character dictionaries
HIRAGANA = {
    "a": "あ", "i": "い", "u": "う", "e": "え", "o": "お",
    "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
    "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ",
    "ta": "た", "chi": "ち", "tsu": "つ", "te": "て", "to": "と",
    "na": "な", "ni": "に", "nu": "ぬ", "ne": "ね", "no": "の",
    "ha": "は", "hi": "ひ", "fu": "ふ", "he": "へ", "ho": "ほ",
    "ma": "ま", "mi": "み", "mu": "む", "me": "め", "mo": "も",
    "ya": "や", "yu": "ゆ", "yo": "よ",
    "ra": "ら", "ri": "り", "ru": "る", "re": "れ", "ro": "ろ",
    "wa": "わ", "wo": "を", "n": "ん"
}

KATAKANA = {
    "a": "ア", "i": "イ", "u": "ウ", "e": "エ", "o": "オ",
    "ka": "カ", "ki": "キ", "ku": "ク", "ke": "ケ", "ko": "コ",
    "sa": "サ", "shi": "シ", "su": "ス", "se": "セ", "so": "ソ",
    "ta": "タ", "chi": "チ", "tsu": "ツ", "te": "テ", "to": "ト",
    "na": "カ", "ni": "ニ", "nu": "ヌ", "ne": "ネ", "no": "ノ",
    "ha": "ハ", "hi": "ヒ", "fu": "フ", "he": "ヘ", "ho": "ホ",
    "ma": "マ", "mi": "ミ", "mu": "ム", "me": "メ", "mo": "モ",
    "ya": "ヤ", "yu": "ユ", "yo": "ヨ",
    "ra": "ラ", "ri": "リ", "ru": "ル", "re": "レ", "ro": "ロ",
    "wa": "ワ", "wo": "ヲ", "n": "ン"
}

KANJI = {
    "日": "hi / nichi - day, sun",
    "月": "tsuki / getsu - moon, month",
    "人": "hito / jin - person"
}


def choose_mode():
    print("=== JP SCRIPT TRAINER ===")
    print("1) Hiragana")
    print("2) Katakana")
    print("3) Basic Kanji (3 characters)")
    print("4) Exit")
    return input("Choose a mode (1-4): ").strip()


def quiz(char_dict, mode_name):
    print(f"\nMode: {mode_name}")
    print("Type 'exit' to return to the menu.\n")

    romaji_list = list(char_dict.keys())
    correct = 0
    total = 0
    last_char = None  # prevents repetition

    while True:
        # pick a new character different from the previous one
        romaji = random.choice(romaji_list)
        while romaji == last_char:
            romaji = random.choice(romaji_list)

        last_char = romaji
        character = char_dict[romaji]

        answer = input(f"Character: {character} -> reading: ").strip().lower()

        if answer == "exit":
            break

        total += 1

        if answer == romaji:
            print("Correct!\n")
            correct += 1
        else:
            print(f"Wrong. Correct reading: {romaji}\n")

    if total > 0:
        accuracy = (correct / total) * 100
        print(f"Result: {correct}/{total} ({accuracy:.1f}% correct)\n")
    else:
        print("No answers given.\n")


def quiz_kanji():
    print("\nMode: Basic Kanji")
    print("Press Enter to reveal meaning, or type 'exit' to return.\n")

    kanji_list = list(KANJI.keys())
    last_kanji = None

    while True:
        kanji = random.choice(kanji_list)
        while kanji == last_kanji:
            kanji = random.choice(kanji_list)

        last_kanji = kanji

        user = input(f"Kanji: {kanji}\nReveal meaning? ")

        if user.lower() == "exit":
            break

        print(f"Meaning/reading: {KANJI[kanji]}\n")

    print("Kanji practice finished.\n")


def main():
    while True:
        choice = choose_mode()

        if choice == "1":
            quiz(HIRAGANA, "Hiragana")
        elif choice == "2":
            quiz(KATAKANA, "Katakana")
        elif choice == "3":
            quiz_kanji()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
