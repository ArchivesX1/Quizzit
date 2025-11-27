import csv
import random
import os
import sys


DEFAULT_QUESTION_FILE = "questions.tsv"


def load_questions(filename: str):
    if not os.path.exists(filename):
        print(f"Question file '{filename}' not found.")
        print("Make sure it's in the same folder and named correctly.")
        raise SystemExit(1)

    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        questions = list(reader)

    if not questions:
        print("No questions found in the file.")
        raise SystemExit(1)

    return questions


def ask_question(q: dict) -> bool:
    """
    Ask a single question.
    Returns True if user answered correctly, False otherwise.
    """

    print()
    print(f"Q{q['id']}: {q['question']}")
    print("  A)", q["a"])
    print("  B)", q["b"])
    print("  C)", q["c"])
    print("  D)", q["d"])
    print()

    valid_choices = {"a", "b", "c", "d"}
    choice = None

    while choice not in valid_choices:
        user_input = input("Your answer (A/B/C/D, or Q to quit): ").strip().lower()
        if user_input == "q":
            raise KeyboardInterrupt
        if user_input in valid_choices:
            choice = user_input
        else:
            print("Please enter A, B, C, D or Q.")

    choice_letter = choice.upper()
    correct_letter = q["correct"].strip().upper()

    # Map letter -> fields
    option_field = {
        "A": "a",
        "B": "b",
        "C": "c",
        "D": "d",
    }
    exp_field = {
        "A": "exp_a",
        "B": "exp_b",
        "C": "exp_c",
        "D": "exp_d",
    }

    chosen_text = q[option_field[choice_letter]]
    chosen_exp = q.get(exp_field[choice_letter], "")

    correct_text = q[option_field[correct_letter]]
    correct_exp = q.get(exp_field[correct_letter], "")

    print()
    print(f" You chose {choice_letter}) {chosen_text}")

    if choice_letter == correct_letter:
        print(" ✅ Correct!")
        if chosen_exp:
            print("   Why:", chosen_exp)
        return True
    else:
        print(" ❌ Incorrect.")
        if chosen_exp:
            print("   Why your choice is incorrect:", chosen_exp)
        print()
        print(f"   Correct answer: {correct_letter}) {correct_text}")
        if correct_exp:
            print("   Why this is correct:", correct_exp)
        return False


def main():
    # Decide which question file to use
    if len(sys.argv) > 1:
        question_file = sys.argv[1]
    else:
        question_file = DEFAULT_QUESTION_FILE

    print(f"Using question file: {question_file}")
    questions = load_questions(question_file)

    # Optional: shuffle questions each run
    random.shuffle(questions)

    total = 0
    correct = 0

    print("=== Networking Quiz ===")
    print(f"Loaded {len(questions)} questions from {question_file}.")
    print("Press Q at any time to quit.")
    print("-" * 50)

    try:
        for q in questions:
            is_correct = ask_question(q)
            total += 1
            if is_correct:
                correct += 1
            print()
            print(
                f"Score so far: {correct}/{total} correct "
                f"({(correct / total * 100):.1f}%)"
            )
            print("-" * 50)
    except KeyboardInterrupt:
        print("\nExiting quiz...")

    if total > 0:
        print()
        print("=== Final Results ===")
        print(f"Answered: {total}")
        print(f"Correct:  {correct}")
        print(f"Score:    {(correct / total * 100):.1f}%")
    else:
        print("No questions answered.")


if __name__ == "__main__":
    main()
