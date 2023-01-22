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
You can find statistics.txt file saved in your folder
## **Project preview**
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

### Run the program in terminal:
```
python3 election-scraper.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'results-prostejov.csv'
```
### Processing:
```
DOWNLOADING DATA FROM URL: 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
SAVING TO FILE: results-prostejov.csv
ENDING election-scraper
```
### Result preview:
```
code,location,registred,envelopes,valid,Občanská demokratická strana,...
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
...
```
