---
title: "Building Bear Ninja Cowboy"
slug: bear-ninja-cowboy
---

You might know the game as "Rock, Paper, Scissors"—but for the sake of this tutorial, we will be building a game of Bear, Ninja, Cowboy.

# Getting Started

Bear Ninja Cowboy or BNC will be made out of just one python file. You can tell if a file is python code if it ends in the `.py` document type.

If you don't already have one, navigate to the root of your computer, to the `~` directory, and make a new directory called `code`, then in that directory make a new directory called `cli-games`. We'll put all the games we make in this tutorial in this folder. In that directory make a new file called `bnc.py`.

```bash
$ cd ~
$ mkdir code
$ cd code
$ mkdir cli-games
$ cd cli-games
$ touch bnc.py
```

# Open the Directory in Atom

Using the [atom text editor](https://atom.io/) open the `cli-games` directory using the `atom` command:

```
$ atom .
```

# Getting CLI Input

Our first step is to get some input from players with the command line input.

```py
# cli-games/bnc.py

input = input("Greetings, what is your name? > ")
print(input)
```


> [info]
> **Comments and Psuedocode**: There are two types of
> `#`
