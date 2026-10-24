# Flet Secret Birthday App 🎉

A small interactive Python application built using **Flet**, featuring a password-based login screen, animated confetti, and a hidden birthday surprise.

This project was created as a learning exercise to explore Python GUI development, event handling, animations, and navigation between screens.

## Features

- **Password input:** Users can enter a password to access the application.
- **Input validation:** Incorrect passwords display an error message.
- **Welcome screen:** The normal password opens a welcome screen with animated confetti.
- **Secret birthday surprise:** A special password combined with a long press on the Submit button reveals a hidden birthday message.
- **Confetti animation:** Uses a Lottie JSON animation.
- **Logout functionality:** Returns the user to the login screen.
- **Web support:** The app can run directly in a web browser.

## Technologies Used

- Python
- [Flet](https://flet.dev/)
- [Flet Lottie](https://pypi.org/project/flet-lottie/)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/flet-secret-birthday-app.git
cd flet-secret-birthday-app
```

Replace `YOUR_USERNAME` with the repository owner's GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install "flet[all]" flet-lottie
```

### 4. Run the application

```bash
flet run --web src/main.py
```

The application will open in your web browser.

## How It Works

1. The application starts with a password input field.
2. Entering the normal demo password and clicking Submit opens the welcome screen.
3. The welcome screen displays a confetti animation.
4. Entering the special demo password and long pressing Submit reveals the hidden birthday message.
5. Incorrect passwords display an error.
6. The user can return to the login screen using Log out.

## Project Structure

```text
src/
    main.py
    assets/
        Confetti.json
        icon.png
tests/
README.md
pyproject.toml
```

## What I Learned

Through this project, I practiced:

- Creating user interfaces with Flet.
- Using text fields, buttons, and containers.
- Handling user interactions with Python functions.
- Detecting normal clicks and long presses.
- Building multiple screens within one application.
- Adding Lottie animations.
- Organizing and documenting a Python project.

## Notes

This application is intended for learning and demonstration purposes. Its hardcoded passwords are not suitable for real authentication or protecting sensitive information.

The confetti animation is a third-party asset and remains subject to its original license.

## Future Improvements

- More animations and transitions.
- Improved user interface design.
- Better handling of different screen sizes.
- Additional interactive surprises.

## Author

Mohammad Baidossi

Built with Python and Flet.