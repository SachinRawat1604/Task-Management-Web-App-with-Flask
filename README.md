# Task Management Web App with Flask

A simple and intuitive web application for managing daily tasks, built using Flask. This app enables users to add, view, and delete tasks efficiently through a clean, responsive interface.

## Features

- **Add Tasks:** Easily create new tasks to organize your work.
- **View Tasks:** See all your tasks in a structured, user-friendly dashboard.
- **Delete Tasks:** Remove completed or unnecessary tasks.
- **User Authentication:** (If implemented) Register and log in to manage personal tasks.
- **Responsive Design:** Works seamlessly across desktop and mobile devices.

## Technologies Used

- **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SachinRawat1604/Task-Management-Web-App-with-Flask.git
   cd Task-Management-Web-App-with-Flask
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Access the web app:**
   - Open your browser and go to [http://localhost:5000](http://localhost:5000)

## Project Structure

```
Task-Management-Web-App-with-Flask/
├── static/
│   └── style.css
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── base.html
│   ├── dashboard.html
│   └── add_edit_task.html
├── main.py
├── database.db
├── requirements.txt
└── README.md
```

- **static/**: CSS and other static assets
- **templates/**: HTML templates for UI
- **main.py**: Main Flask app
- **database.db**: SQLite database
- **requirements.txt**: Python dependencies

## Screenshots

*(Add screenshots of the dashboard and key features here)*

## Contributing

Contributions are welcome! Please fork the repo and submit a pull request for enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
