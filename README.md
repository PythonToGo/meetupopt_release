# Meeting Scheduler

A simple web app built with **Flask** and **SQLite** for scheduling meetings by finding common available times among participants.

## Features

- Select available times (09:00 AM to 06:00 PM).
- Submit availability by entering your name.
- Best meeting time calculated based on common available slots.

## Feature Exclusion Note

This repository contains only the public components of the project. Due to security and privacy concerns, certain features and functionality have been intentionally excluded from the code and are not included in this public release.

Please ensure to configure your own environment variables and private files as necessary when setting up the project locally.

## Notes on Excluded Features

- Certain features have been removed from the code to ensure security and privacy.
- The full functionality is available in a separate, secured environment for private use.


## Installation

1. Clone the repo.
2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running Locally

1. Run the app:
    ```bash
    python app.py
    ```
2. Visit http://127.0.0.1:5000/.


## Deployment

Deploy using Vercel. Ensure the following files are set up:
- `Procfile` to run the app using Gunicorn.
- `requirements.txt` for dependencies.
- `runtime.txt` for the Python version (if needed).

## Technologies Used

- Flask
- SQLite
- Tailwind CSS


## License

MIT License.


This version focuses on the essentials while leaving out more detailed instructions.