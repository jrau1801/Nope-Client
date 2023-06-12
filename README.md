Nope-Client README
-
Learning Journal:
[Learning Journal](https://hallowed-cattle-810.notion.site/Softwareprojekt-Lerntagebuch-e4d82e95510a4af7b133aa02e8aba444?pvs=4)



<!-- Table of Contents -->
# Table of Contents

- [About the Project](#about-the-project)
  * [Tech Stack](#tech-stack)
  * [Features](#features)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Run Locally](#run-locally)
- [Usage](#usage)
  * [Screenshots](#screenshots)

  

<!-- About the Project -->
## About the Project

### Architecture
<div align="center"> 
  <img src="assets/architecture.png" alt="screenshot" />
</div>

### Project Structure

```txt
.
│ 
├── assets                  Assets
├── build                   Builds website for Sphinxdoc
│    ├── _static            CSS and JS Files   
│    └── rst                HTML Files
├── gui
│    ├── login_gui.py       Login GUI
│    ├── main_menu.py       Main menu GUI
│    └── register_gui.py    Register GUI
├── rst
│    ├── aiplayer.rst       reStructuredText Files Sphinxdoc
│    └── ...
└── .py files               All scripts
    ├── aiplayer.py         AI-Player
    ├── conf.py             config for Sphinxdoc
    ├── events.py           SocketIO events
    ├── format.py           Better output
    ├── logger.py           Logging
    ├── main.py             Main menu
    └── urls.py             Rest-API URLs
```

The browser documentation of the code can be found at:
``../build/index.html``
or under: [Documentation](https://nope-client-doc-sp.w3spaces.com/)

The documentation was created using Sphinx: [Sphinx](https://www.sphinx-doc.org/en/master/)

<!-- Knockout Card Game - Semester Project -->
### Nope Card Game - Semester Project
### Introduction
Welcome to our semester project on the Nope Card Game! In this project, we explore the exciting and entertaining world of card games, focusing specifically on the rules and mechanics of the Nope Card Game. Our aim is to provide a comprehensive overview of the game, its components, setup, gameplay, and objectives.

### Components
To begin, let's explore the components of the Nope Card Game. The game comprises a total of 104 cards, each serving a unique purpose. These cards include:

- 4 Joker cards
- 14 Action cards
- 4 Restart cards
- 4 Insight cards
- 6 Choice cards
- 66 Two-color cards (24 cards with numbers 1, 2, and 3 in each color combination)
- 20 Solid color cards (8 cards with numbers 1 and 2, and 4 cards with the number 3 in Red, Green, Blue, and Yellow)

### Objective
In the Nope Card Game, your objective is simple: be the last player standing with cards in hand. It requires strategy, cunning, and a bit of luck to outmaneuver your opponents and secure victory. Keep your wits about you and eliminate your opponents one card at a time.


<!-- TechStack -->
### Tech-Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://de.wikipedia.org/wiki/Hypertext_Markup_Language">HTML</a></li>
    <li><a href="https://de.wikipedia.org/wiki/Cascading_Style_Sheets">CSS</a></li>
    <li><a href="https://de.wikipedia.org/wiki/JavaScript">JavaScript</a></li>
    <li><a href="https://socket.io/">SocketIO</a></li>

  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://azure.microsoft.com/de-de">Microsoft Azure</a></li>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
    <li><a href="https://socket.io/">SocketIO</a></li>
    <li><a href="https://www.prisma.io/">Prisma</a></li>    

  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.mysql.com/">MySQL</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
  </ul>
</details>

<!-- Features -->
### Features

- Easy to use
- Readable Code
- Play Online
- Play locally
- Documentation

### AI-Player
This game is played automatically with an ai-player. 
To build a set and make a move, the ai-player has to follow some conditions:

- Play ``Two-Color cards`` first, ``One-Color cards`` second and ``Action cards`` last.
- If only ``Action cards`` left, play ``see-through`` if possible, play ``reboot next``, play ``joker`` last
- If ``top-card`` has value 3 and I can build a set but i have a ``reboot`` on hand, play ``reboot``
- Only play ``see-through`` or ``joker`` if other cards on hand don't fit ``top-card`` color
- Must play ``joker`` if ``action cards`` only ones left and they can fill a set
- Must play ``reboot`` if ``see-through`` can't be played and ``joker`` can't fill a set
- If opponents cards number >= 4 sort move ascending so highest value card will be ``top-card``
- If opponents cards number < 4 sort move descending so lowest value will be ``top-card``
- ``Joker-weight = 50``, ``Two-Colored-weight = 30``, ``Single-Colored weight = 20``
- Set with highest weight will be played
- Since I only play ``see-through`` if i have to and ``reboot`` if a special case is needed, they don't have weights
### Prerequisites

This project uses the SocketIO-Client package

```bash
 pip install "python-socketio[client]"
```

<!-- Run Locally -->
### Run Locally

Clone the project

```bash
  git clone https://github.com/jrau1801/Nope-Client
```

Go to the project directory

```
  Search for either main.py or login_gui.py and run them
```
```
  Login or Register and create or join a tournament
```

For Rest-API URLs
```
  Run urls.py
```
or
[Rest-API Swagger Documentation](https://nope-server.azurewebsites.net/docs/)


<!-- Usage -->
## Usage



<!-- Screenshots -->
### Screenshots

```
To run the game by yourself you'll probably have to change some settings.
In IntelliJ IDEA this is necessary.
```
```
-> Run -> Edit Configurations -> Allow Multiple instances
```


<div align="center"> 
  <img src="assets/settings.png" alt="screenshot" />
</div>

```
Run main.py two times and split them Left/Right for better usage.
```

### Documentation
```
As mentioned before, this project has been documented with Sphinx.
The landing page looks like this:
```
<div align="center"> 
  <img src="assets/sphinxdoc.png" alt="screenshot" />
</div>

```
Every method and class has been documented.
This is the place to go if you want to understand the code better.
```

```
To run Sphinx you'll need the following command.
And changes to conf.py are needed sometimes, when working with different directories.
Here we added syspaths for the directories we are working in.
```

<div align="center"> 
  <img src="assets/conf.png" alt="screenshot" />
</div>

```bash
sphinx-build -b html . build
```
```
"html" is the format, "." is the source dir and "build" is the target dir
```
