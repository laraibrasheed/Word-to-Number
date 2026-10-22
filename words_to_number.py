ONES = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
}
TENS = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
}
MULTIPLIERS = {
    "thousand": 1000, "million": 1000000, "billion": 1000000000,
}

def words_to_number(text: str) -> int:
    words = text.lower().replace("-", " ").split()
    if not words:
        raise ValueError("Input cannot be empty.")

    total = 0
    current = 0
    has_number = False

    for word in words:
        if word in ONES:
            value = ONES[word]
            if value == 0 and len(words) > 1:
                raise ValueError("Invalid placement of 'zero'.")
            if value >= 10 and current % 100 != 0:
                raise ValueError(f"Unexpected number sequence at '{word}'.")
            if value < 10 and (current % 10 != 0 or 10 <= current % 100 <= 19):
                raise ValueError(f"Unexpected number sequence at '{word}'.")
            current += value
            has_number = True

        elif word in TENS:
            if current % 100 != 0:
                raise ValueError(f"Unexpected number sequence at '{word}'.")
            current += TENS[word]
            has_number = True

        elif word == "hundred":
            if current == 0 or current >= 100:
                raise ValueError("'hundred' must follow a valid number below 100.")
            current *= 100

        elif word in MULTIPLIERS:
            if current == 0:
                raise ValueError(f"'{word}' must be preceded by a number.")
            current *= MULTIPLIERS[word]
            total += current
            current = 0

        elif word == "and":
            continue

        else:
            raise ValueError(f"Unknown word: {word}")

    if not has_number:
        raise ValueError("No valid number words found.")

    return total + current

if __name__ == "__main__":
    try:
        text = input("Enter number in words: ")
        print(f"Number: {words_to_number(text)}")
    except ValueError as e:
        print(f"Error: {e}")