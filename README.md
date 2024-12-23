# love_score_python
Creative Python 🐍 developer who loves solving problems with fun projects! Built a Love Calculator that calculates compatibility scores based on letter frequencies in "TRUE" and "LOVE." Demonstrates logic building, condition handling, and string manipulation skills. Check out this and more projects here
Separate true and love counts:

The original code mistakenly reused true for the final score, resulting in an incorrect calculation.
Logical conditions in elif:

The condition love_score >= 40 or love_score <= 50 always evaluates as True because any number is either greater than or equal to 40 or less than or equal to 50.
This is corrected to 40 <= love_score <= 50.
Input handling:

The names are converted to lowercase to ensure the count method works correctly regardless of case.
How It Works:
The program calculates scores based on the letters in the words "TRUE" and "LOVE" found in the combined names.
It then creates a score by concatenating the two numbers and checks the score against specific conditions to print the appropriate message.
