# 🟥 Python Practice: Hard Questions – Set 2 (q11.py to q20.py)

This set contains 10 hands-on Python coding challenges from Chapter 1 of Automate the Boring Stuff with Python. These are *realistic, **interactive*, and push your logic, variables, and string manipulation skills without using loops, conditionals, or slicing—just what Chapter 1 allows.

Each challenge is stored in its own file: q11.py to q20.py.

---

## 📂 File Breakdown & Descriptions

### q11.py – 💪 BMI Calculator (Basic)
Ask the user for their *weight (kg)* and *height (m)* as floats.  
Calculate their BMI using the formula:  
BMI = weight / (height * height)  
Then print the result.  
🧠 Self-Reflection: Think about what happens if the user enters text (you’ll get a ValueError — but don’t fix it yet).

---

### q12.py – 💶 Currency Converter (USD → EUR)
Ask the user for an *amount in USD* (as a float).  
Convert it to EUR using a fixed rate (e.g., 1 USD = 0.92 EUR).  
Print the converted value, clearly labeled. Handle decimals properly.

---

### q13.py – 🧑‍💻 Dynamic Username Generator
Ask for the user's *first name* and *last name*.  
Generate a username by combining the *first 3 letters of the first name* and the *entire last name*.  
Example: "John" + "Smith" → JohSmith  
Assume the names are long enough.

---

### q14.py – 🛒 Shopping Cart Item Summary
Ask the user for:
- Item name (e.g., “Apples”)
- Quantity (integer)
- Unit price (float)

Then calculate the total cost and print something like:  
Item: Apples | Qty: 5 | Unit Price: $1.20 | Total: $6.00

---

### q15.py – 📅 Age in Days
Ask the user for their age in years.  
Convert it to an approximate number of days (use 365 days/year).  
Print something like:  
👉🏾 “You are approximately 7,300 days old.”

---

### q16.py – 🐸 Interactive Story Fragment
Ask the user for:
- An animal
- A verb
- A number
- An adjective

Then create a silly story like:  
👉🏾 “A 5 fluffy cats decided to dance across the field.”

---

### q17.py – 📏 Rectangle Perimeter and Area
Ask for the *length* and *width* of a rectangle.  
Then calculate and print:
- Area = length × width
- Perimeter = 2 × (length + width)

---

### q18.py – 🎉 Personalized Welcome Banner
Ask for the user's first name.  
Print a welcome banner like this:  
----- Welcome Alice -----  
Use len() and string replication to center the name in a fixed-width message (e.g., 20–30 characters wide).

---

### q19.py – 🧪 Data Type Mix-Up Challenge
Assign the following:
- a = 10 (int)
- b = "5" (str)
- c = 2.5 (float)

Then do and explain:
- a + int(b)
- str(a) + b
- a * c
- float(b) + c  
Add comments to explain the result types.

---

### q20.py – ⏱ Time Conversion (Hours → Minutes & Seconds)
Ask the user for a number of *hours* (int).  
Convert that to:
- Minutes (hours * 60)
- Seconds (hours * 3600)  
Print the results clearly labeled.

---

## 🧠 What You’ll Practice

- input() and print()
- int(), float(), and str() conversions
- Basic arithmetic operations
- Variable naming & assignment
- len() for measuring strings
- Using \n and string formatting creatively

---

## ⚠ Scope Note

These solutions are built *strictly within the limits of Chapter 1* of ATBS.  
No if, for, while, functions, or external libraries used.  
They're beginner-friendly but logic-intensive.

---

## ✅ Next Steps

Once you’re done:
- Try building mini console apps from these challenges
- Move into Chapter 2 to unlock loops and conditionals
- Organize your scripts in GitHub with clear README.md and comments

---

> 💡 Tip: Run the .py files in VS Code terminal or Python shell to test input and outputs interactively.

---