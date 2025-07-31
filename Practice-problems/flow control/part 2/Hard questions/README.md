Hard Questions - If, Elif, Else (q1.py to q17.py)
This folder contains a series of Python exercises designed to challenge your understanding and application of if, elif, and else conditional statements. These problems require careful use of nested conditions, logical operators, and scenario-based thinking to arrive at a correct solution.
The questions are organized by file name from q1.py to q17.py.
Questions
1. ATM Simulation
Write a program that asks the user to enter a 4-digit PIN (as a number) and an account balance (as a number), then a withdrawal amount. If the PIN is correct (assume the correct PIN is 1234) and the withdrawal amount is less than or equal to the balance, print "Withdrawal approved"; if the PIN is correct but the withdrawal amount is greater than the balance, print "Insufficient funds"; otherwise, print "Invalid PIN".
2. Cinema Ticket Checker
Write a program that asks the user if they have a ticket ("yes" or "no") and if they have the exact change ("yes" or "no"). If the user has a ticket and exact change, print "Enter cinema"; elif the user has a ticket but not exact change, print "Need exact change"; elif the user has no ticket but has exact change, print "No entry without ticket"; otherwise (no ticket and no change), print "No entry".
3. Count True Values
Write a program that asks the user to input three boolean values (True or False). If all three are True, print "All true"; elif exactly two of them are True, print "Two true"; elif exactly one is True, print "One true"; otherwise (none true), print "None true".
4. Number Classification
Write a program that asks the user for an integer. Use nested if statements to classify it: if it is greater than zero, check if it is even or odd and print "Positive even" or "Positive odd"; elif it is less than zero, check if it is even or odd and print "Negative even" or "Negative odd"; otherwise, if it is zero, print "Zero".
5. Rock-Paper-Scissors
Write a program that asks two players to enter their choices for Rock-Paper-Scissors (each enters "rock", "paper", or "scissors"). Determine the winner: print "Player 1 wins" or "Player 2 wins" accordingly, or print "Tie" if both players chose the same.
6. FizzBuzz Variation
Write a program that asks the user for an integer. If the number is divisible by 3 and 5, print "FizzBuzz"; elif it is only divisible by 3, print "Fizz"; elif it is only divisible by 5, print "Buzz"; otherwise, print the number itself.
7. Overtime Pay Calculator
Write a program that asks the user for their hourly wage (float) and hours worked in a week (float). If the hours are greater than 40, calculate overtime pay for the hours above 40 at 1.5 times the hourly wage and print "Overtime pay is X" where X is the overtime pay; otherwise, print "No overtime".
8. Simple Calculator
Write a program that asks the user for two numbers and then for a mathematical operator (enter "+", "-", "*", or "/"). Use if/elif to perform the correct operation and print the result. If the operator is not one of these four, print "Invalid operator".
9. Leap Year Check
Write a program that asks the user for a year (e.g., 2024). Print "Leap year" if the year is a leap year according to these rules: it is divisible by 4, except years divisible by 100 are not leap years unless they are also divisible by 400. Otherwise, print "Not a leap year".
10. Stay Indoors or Go Out
Write a program that asks the user for the current hour (0–23) and whether it is raining ("yes" or "no"). If it is 6 PM or later (hour >= 18) or if it is raining, print "Stay indoors"; otherwise, print "Enjoy the day".
11. BMI Calculator & Classifier
Ask the user for their weight (in kg, float) and height (in meters, float). Calculate BMI using the formula: BMI = weight / (height * height). Then, classify and print:
 * "Underweight" if BMI < 18.5
 * "Normal weight" if 18.5 <= BMI < 25
 * "Overweight" if 25 <= BMI < 30
 * "Obese" if BMI >= 30
12. Ticket Price based on Age & Day
Ask the user for their age (integer) and the day of the week (string, e.g., "Monday", "Sunday").
 * If age is less than 5 or greater than 60, ticket price is 0.
 * If it's "Tuesday", ticket price is 10 (discount day).
 * Otherwise, if age is between 5 and 18 (inclusive), ticket price is 12.
 * Otherwise (for adults), ticket price is 15. Print the final ticket price.
13. Valid Email Format (Simplified)
Ask the user for an email address (string). Print True if the email:
 * Contains @ AND
 * Contains . AND
 * The @ symbol appears before the . symbol. Otherwise, print False.
14. Password Strength Indicator (Partial)
Ask the user for a password (string). Print "Strong" if the password:
 * Has a length of 8 or more characters AND
 * Contains both lowercase and uppercase letters. Otherwise, print "Weak".
15. Text Case Classifier
Ask the user for a word (string). Print:
 * "ALL CAPS" if the word is entirely uppercase.
 * "all lowercase" if the word is entirely lowercase.
 * "Mixed Case" if it has both upper and lower characters.
16. Shipping Cost Calculator
Ask the user for the item's weight (float, in kg) and distance (float, in km). Calculate and print the shipping cost based on the following rules:
 * If weight is less than 1 kg:
   * If distance is less than 50 km, cost is 5.
   * Otherwise, cost is 10.
 * If weight is 1 kg or more:
   * If distance is less than 50 km, cost is 15.
   * Otherwise, cost is 20.
17. Counter-Style Problem (Counting Numbers Meeting a Condition)
Prompt the user to enter three integer values. Constraint: Use only if/elif/else (no loops or lists). Initialize a counter variable count = 0. For each of the three numbers, use an if statement to check if it is greater than 10 and even. If it is, increment count by 1. After checking all numbers, print the value of count.