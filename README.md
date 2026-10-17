# Words to Number Converter 

A simple Python project that converts numbers written in English words into their corresponding integer values.

## About
This project takes a number written as a string, such as:"Two Thousand"
and converts it into:2000
It supports basic numbers, tens, hundreds, and larger number units such as thousand, million, and billion.

### Some working Examples
#### Example 1
Input: Two Thousand
Output: 2000

#### Example 2
Input: Eight Million
Output: 8000000

#### Example 3
Input: Three Hundred Twenty Five
Output: 325

## How It Works
The program uses Python dictionaries to map English number words to their numerical values.
For example:
"two" → 2
"twenty" → 20
"hundred" → 100
"thousand" → 1000
"million" → 1000000

### The input string is:
Converted to lowercase.
Split into individual words.
Processed word by word.
Combined using the appropriate mathematical operations.
Returned as an integer.

## For example:
"Two Thousand Five Hundred"
is processed as:
Two       → 2
Thousand  → ×1000
Adding it to
Five      → 5
Hundred   → ×100

Result:
2500

### Author
Laraib Rasheed
Built as a personal Python project while learning programming and problem solving.

#### Feedback welcome.
