# 🔢 Smart Number Guesser

A Python mini project where the computer guesses the number you're thinking of using the **Binary Search** algorithm.

## 📌 Features

* Computer guesses a number between 1 and 100.
* Uses Binary Search for efficient guessing.
* Interactive command-line game.
* Finds the correct number in very few attempts.

## 🛠️ Technologies Used

* Python 3

## 🚀 How to Run

1. Clone the repository.
2. Navigate to the project folder.
3. Run the program:

```bash
python guesser.py
```

4. Think of a number between **1 and 100**.
5. Respond with:

   * **h** → Your number is higher.
   * **l** → Your number is lower.
   * **c** → Correct!

## 📂 Project Structure

```
Number-Guesser/
├── guesser.py
└── README.md
```

## 📸 Example

```
Think of a number between 1 and 100 and I will try to guess it!

My guess is: 50
Higher, Lower, or Correct? (h/l/c): h

My guess is: 75
Higher, Lower, or Correct? (h/l/c): l

My guess is: 62
Higher, Lower, or Correct? (h/l/c): c

Yay! I guessed your number 62 in 3 attempts!
```

## 🧠 Algorithm

This project uses the **Binary Search** algorithm, which repeatedly halves the search range to identify the correct number efficiently.

## 🔮 Future Improvements

* Add difficulty levels.
* Allow custom number ranges.
* Build a graphical interface using Tkinter or Streamlit.
* Track the best score and number of attempts.
