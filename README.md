# 📘 Day 28: RegEx, Patterns, and Intro to Databases | HackerRank 30 Days of Code

This repository contains the Python solution for Day 28 of the HackerRank 30 Days of Code challenge, focusing on using **regular expressions** to filter and sort email addresses ending in `@gmail.com`.

## 🚀 Challenge Summary

You are required to use **RegEx** to filter a list of email addresses that end with `@gmail.com` and return a list of the corresponding **first names** in **alphabetical order**.

## 📝 Problem Statement

Complete the solution to:

- Read `N` lines of input containing `FirstName` and `EmailID`
  
- Use a regular expression to find only the email addresses ending with `@gmail.com`.
  
- Print the first names associated with those Gmail IDs, sorted in alphabetical order.

## ✅ Constraints

        - 2 ≤ N ≤ 30
          
        - First name: lowercase English letters, max 20 chars
          
        - Email ID: lowercase English letters, numbers, and must end with `@gmail.com`
          
        - Email ID max length: 50 chars

## 🔢 Sample Input

          6
          riya riya@gmail.com
          julia julia@julia.me
          julia julia@gmail.com
          tanya tanya@gmail.com
          samantha samantha@gmail.com
          julia julia@julia.com

## ✅ Sample Output

          julia
          riya
          samantha
          tanya

## 💡 Explanation

- The valid Gmail addresses are:  
  `riya@gmail.com`, `julia@gmail.com`, `tanya@gmail.com`, `samantha@gmail.com`
  
- Extract the corresponding first names.
  
- Sort them alphabetically and print one per line.

## 🧠 Concepts Practiced

- Regular Expressions / RegEx
  
- String Matching
  
- Input Filtering
  
- List Sorting
  
- Basic Python Programming
  
- HackerRank Input Format Handling

## 🛠 How to Run

Option 1: With input file

Create a file named `input.txt` with the required input and run:

        python3 regex_filter.py < input.txt
        
Option 2: Manual input

        python3 regex_filter.py
        
### 🔗 HackerRank Challenge Link

        HackerRank – Day 28: RegEx, Patterns, and Intro to Databases

🏆 Challenge Completed

✅ Problem Solved

🎯 Points Earned: 30

### 📅 Completed On

        9th June 2025

### 🔖 Tags

#Python #HackerRank #RegEx #30DaysOfCode #ProblemSolving #Day28Challenge #StringMatching #Sorting #CleanCode

### ✍ Author

        Harsha M
        
        GitHub: @Harshaharika7
        
        LinkedIn: Harsha M
