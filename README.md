# Monty-Hall-Game-and-Simulation
## The Monty Hall Dilemma

The Monty Hall problem is a famous probability puzzle based on an old American game show. It's a classic example of how our intuition about odds can be misleading.

## The Setup

1. Imagine you are on a game show. There are three closed doors.
2. Behind one door is a brand new car (the prize). Behind the other two doors are goats (the booby prizes).
3. You are asked to **pick one door**. You don't know what's behind it yet.
4. The host, Monty Hall, **who knows where the car is**, then opens one of the *other two doors* to reveal a goat.
5. Two doors remain closed: your original choice and one other door.

## The Dilemma

The host gives you a choice:

**Do you stick with your original door, or do you switch to the other unopened door?**

## The Counter-Intuitive Solution

You should **always switch**. Switching your choice doubles your chances of winning the car.

* **Sticking** with your first choice gives you a **1/3** chance of winning.
* **Switching** to the other door gives you a **2/3** chance of winning.

## The Simulation

For the simulation program, I have two functions. One function models the player that will always choose to switch their box. The other function models a player that chooses to not switch their box. 

The program then simulates 10,000 simulations of each play style. The win percentage for each playstyle is calculated and presented to the user to reveal why the strategy that maximizes the chance of winning the prize is to always switch boxes.
