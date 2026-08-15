# ⚔️ Murim World CLI RPG

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-black?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A robust, turn-based Command Line Interface (CLI) Role-Playing Game built with Python, featuring MVC architecture, persistent save states, and OOP principles.

## 📖 About The Project

**Murim World** is a text-based RPG set in a martial arts fantasy world. The player explores different regions, battles mythical creatures, collects items, and grows stronger. 

This project was developed to demonstrate mastery of **Object-Oriented Programming (OOP)** and **Software Architecture** patterns in Python without relying on external game libraries.

### Key Features
* **Pure Python:** Built using only standard libraries (`os`, `json`, `time`, `shutil`).
* **MVC Architecture:** Clean separation of concerns between Logic (`models`), UI (`view`), and Game Flow (`manager`).
* **Persistence System:** Full Save/Load functionality using JSON serialization/deserialization.
* **Monster AI:** Enemies act based on health states (Berserk mode, Self-Healing).
* **Puzzle Elements:** Locked room mechanics requiring specific keys found in the world.

## ⚙️ Architecture

The project is structured using the **Model-View-Controller (MVC)** pattern to ensure scalability and code maintainability:

```text
├── main.py             # Entry point
├── config.py           # Game constants & balancing data
├── manager/            # CONTROLLER
│   └── engine.py       # Game loop, combat logic, save/load handler
├── models/             # MODEL
│   ├── creatures.py    # Player & Monster classes
│   ├── items.py        # Item & Inventory logic
│   └── world.py        # Room graph & navigation logic
└── view/               # VIEW
    └── view.py         # Console rendering & UI effects
```

## 🚀 Getting Started

### Prerequisites

  * Python 3.6 or higher.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/hafidzrafi/CLI-RPG.git
    ```
2.  Navigate to the directory:
    ```bash
    cd CLI-RPG
    ```
3.  Run the game:
    ```bash
    python main.py
    ```

## 🎮 How to Play

### Controls

Type commands into the terminal to interact with the world:

  * `go [direction]` : Move North, South, East, or West.
  * `look` : Inspect the current room, enemies, and items.
  * `take [item]` : Pick up an item from the ground.
  * `inventory` : Check your current status and bag.
  * `use potion` : Heal your character.
  * `exit` : Save your progress and quit the game.

### Combat System

When you encounter a monster, the game enters **Combat Mode**. You can choose to **FIGHT** or **FLEE**.

  * **Victory:** You gain stats (Max HP & Damage) based on the monster's level.
  * **Defeat:** Your save file is deleted, and you must start over (Permadeath).

## 🧠 Technical Highlights

### 1\. Serialization (JSON)

The game uses a custom `to_dict()` method implemented across all models (`Player`, `Room`, `Item`) to serialize complex objects into JSON format for storage.

### 2\. Recursive Data Loading

The `load_game` method reconstructs the entire object graph (World -\> Rooms -\> Monsters/Items) from the saved JSON file, ensuring the exact game state is restored.

### 3\. OOP Polymorphism

The `Creature` abstract base class defines the contract for `attack` and `take_damage`, which are implemented differently by `Player` (standard attack) and `Monster` (includes Berserk/Heal logic).

## 📝 License

Distributed under the MIT License.

-----

*Created by Fizz*
