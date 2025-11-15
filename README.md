# Modern Calculator

A sleek, CustomTkinter-based calculator built in Python. Inspired by modern calculator designs, it supports basic arithmetic, keyboard input, and a clean GUI with outlined buttons with a translucent background.

## Features

- Basic operations: +, -, *, /

- Keyboard input support (0-9, +, -, *, /, Enter for =)

- Clear button to reset the screen

- Maximum of 21 characters on screen to prevent overflow

- Modern button design with outlines, hover effects, and fixed sizes

- Resizable font size for the display screen (Arial 40)

## Screenshots

![Screenshot](Translucent.png)


## Installation

#### Clone this repository:

```bash
git clone https://github.com/CoolGuy158-Git/ModernCalculator/
```

#### Navigate to the project folder:

```bash
cd ModernCalculator
```

#### Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
```

#### Activate the virtual environment:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```
#### Install customtkinter
```bash
pip install customtkinter
```

#### Run the calculator with Python:

```bash
python ModernCalc.py
```

#### **Optional** turn it into an executable

```bash
pip install pyinstaller
```

```bash
pyinstaller ModernCalc.py --onefile --noconsole
```

## CONTROLS
- Click the buttons or use the keyboard to input numbers and operations.

- Press Enter or = to calculate.

- Press Clear or the c key to reset the screen.

## Notes

- The calculator currently supports basic arithmetic only.

- Maximum characters on the screen is 21 to prevent overflow.

- The design uses CustomTkinter for a modern UI look.

## Future Improvements

**Add dynamic font resizing when the display reaches max characters**

**Add decimal point support and floating point calculations**

**Include keyboard shortcuts for Clear (Esc) and backspace**



