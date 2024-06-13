<div align="center">

<img src="https://static.tildacdn.com/tild3139-6463-4362-a466-643665346661/brain.png" alt="logo" width="270" height="auto" />
<h1>Mind Games</h1>

<p>
Five CLI math games
</p>

### Hexlet tests and linter status:
[![Actions Status](https://github.com/shizomanya/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/shizomanya/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/b862fbdeb3d4fdd4535e/maintainability)](https://codeclimate.com/github/shizomanya/python-project-49/maintainability)

<p>
<a href="#about">About</a> •
<a href="#installation">Installation</a> •
<a href="#usage">Usage</a> 
</p>
</div>

<details>
  <summary style="font-size:larger;"><b>Table of Contents</b></summary>

* [About](#about)
  * [Games](#games)
  * [Built With](#built-with)
  * [Makefile Commands](#makefile-commands)
* [Installation](#installation)
  * [Package](#package)
* [Usage](#usage)
  * [Brain Even](#brain-even)
  * [Brain Calc](#brain-calc)
  * [Brain GCD](#brain-gcd)
  * [Brain Progression](#brain-progression)
  * [Brain Prime](#brain-prime)

</details>

## About:
A "**Mind Games**" is a collection of five simple console games. Each game asks questions that must be answered correctly. After three correct answers, the game is considered completed. Wrong answers end the game and prompt you to play it again.

### Games:
- **Brain-Even**: Determining an even number.
- **Brain-Calc**: Arithmetic expressions to be calculated.
- **Brain-Gcd**: Calculating the greatest common factor.
- **Brain-Progression**: Searching for missing numbers in the arithmetic progression of numbers.
- **Brain-Prime**: Definition of a prime number.

### Built With

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [flake8](https://flake8.pycqa.org/en/latest/)                               | "Flake8: Your Tool For Style Guide Enforcement"         |

### Makefile Commands:

install: ```poetry install```

build: ```poetry build```

package-install: ```python3 -m pip install --user --force dist/*.whl```

lint: ```poetry run flake8```

---

## Installation

#### Python

Before installing the package make sure you have Python version 3.10 or higher installed:

```bash
>> python --version
Python 3.10.12
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

### Package

To use the package, you need to clone the repository to your computer. This is done using the ```git clone``` command. Clone the project:

```bash
>> git clone https://github.com/shizomanya/python-project-lvl1.git
```

Then you have to build the package and install it:

```bash
>> cd python-project-lvl1
```

```bash
>> poetry build
>> python3 -m pip install --user dist/*.whl
```

---

## Usage

### Brain Even
'Answer "yes" if the number is even, otherwise answer "no".'

```bash
>> brain-even

Answer "yes" if the number is even, otherwise answer "no".
Question: 98
Your answer: no
'no' is wrong answer ;(. Correct answer was 'yes'.
```

```bash
>> brain-even

Answer "yes" if the number is even, otherwise answer "no".
Question: 82
Your answer: yes
Correct!
```

[![asciicast](https://asciinema.org/a/Jhkrpypvnd8AyVwtUU4PnlghO.svg)](https://asciinema.org/a/Jhkrpypvnd8AyVwtUU4PnlghO)

### Brain Calc 
'What is the result of the expression?'

```bash
>> brain-calc

What is the result of the expression?
Question: 3 + 15
Your answer: 315
'315' is wrong answer ;(. Correct answer was '18'.
```

```bash
>> brain-calc

What is the result of the expression?
Question: 5 * 15
Your answer: 75
Correct!
```
[![asciicast](https://asciinema.org/a/nDYG4UFN15KXCGalqbZhsgYsA.svg)](https://asciinema.org/a/nDYG4UFN15KXCGalqbZhsgYsA)

### Brain GCD 
'Find the greatest common divisor of given numbers.'

```bash
>> brain-progression

What number is missing in the progression?
Question: 13 22 31 40 49 58 67 76 85 .. 103
Your answer: 100
'100' is wrong answer ;(. Correct answer was '94'.
```

```bash
>> brain-progression

What number is missing in the progression?
Question: 11 16 .. 26 31 36 41 46
Your answer: 21
Correct!
```

[![asciicast](https://asciinema.org/a/eg15BRBnaQqmpyp7v0t3NGtxC.svg)](https://asciinema.org/a/eg15BRBnaQqmpyp7v0t3NGtxC)

### Brain Progression:
- 'What number is missing in the progression?'

```bash
>> brain-progression

Welcome to the Brain Game!
What number is missing in this progression?
May I have your name? Ann
Hello, Ann!
Question: 14 .. 18 20 22 24 26 28
Your answer: 16 # The user enters the answer
Correct!
Question: 5 6 7 8 9 .. 11 12
Your answer: 10 # The user enters the answer
Correct!
Question: 12 15 18 21 .. 27 30 33
Your answer: 24 # The user enters the answer
Correct!
Congratulations, Ann!
```

[![asciicast](https://asciinema.org/a/308i1NcmMmSZC0funt3cEG7GY.svg)](https://asciinema.org/a/308i1NcmMmSZC0funt3cEG7GY)

### Brain Prime
'Answer "yes" if given number is prime. Otherwise answer "no".'

```bash
>> brain-prime

Answer "yes" if given number is prime. Otherwise answer "no".
Question: 66
Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
```

```bash
>> brain-prime

Answer "yes" if given number is prime. Otherwise answer "no".
Question: 22
Your answer: no
Correct!
```

[![asciicast](https://asciinema.org/a/DK77efalNTl9euaeJBfk6erWw.svg)](https://asciinema.org/a/DK77efalNTl9euaeJBfk6erWw)
