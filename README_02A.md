# **Engeto Python Academy - Project 2A**
### The second project for Engeto Python Academy BULLS & COWS
---
## **Project description**
This project is a simple number guessing game. In every new game there is a random 4 digit number generated. 
You attempt to guess it by suggesting numbers. For each correct digit in the correct position, the guessing player receives a "bull," 
and for each correct digit in the wrong position, they receive a "cow." The goal of the game is for the guessing player to correctly guess 
the secret number with as few guesses as possible.
## **Roles for the 4 digit guess number**
You need to enter:
- 4 digit number
- can not start with 0
- can not have a duplicates inside number
## **Evaluation**
After every game you get results:
- number of your guesses
- your game time
- will ask you for your name and save these results to statistics.txt

You can find statistics.txt file saved in your folder.
## **Project preview**
Welcome text:
```
------------------------------------------------
Hi there!
------------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
------------------------------------------------
Enter a number: 
------------------------------------------------
(3847)
>>> 
```
Number guessing:
```
Enter a number: 
------------------------------------------------
(3847)
>>> 2345
1 Bull, 2 Cows
------------------------------------------------
(3847)
>>> 
```
Evaluation:
```
(3847)
>>> 3847 
Correct, you've guessed the right number 
in 2 guesses!
------------------------------------------------
That is amazing!
------------------------------------------------
Your game time: 00:06:04
Please enter your name for statistics: Tom
Find your game staistics in file statistics.txt
```
### Statistics preview:
```
Name: Tom, gueses: 2, time: 364.8 s
Name: Eva, gueses: 4, time: 15.0 s
Name: Radim, gueses: 8, time: 19.8 s
...
```
