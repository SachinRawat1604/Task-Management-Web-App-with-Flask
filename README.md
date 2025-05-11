# Task Management Web App with Flask

A simple and intuitive task management web application built using Flask. This application allows users to add, view, and manage their tasks efficiently.

## Features

* **Add Tasks**: Users can add new tasks to their task list.
* **View Tasks**: Display all existing tasks in a structured format.
* **Delete Tasks**: Remove tasks that are no longer needed.
* **Responsive Design**: User-friendly interface that works across various devices.

## Technologies Used

* **Backend**: [Flask](https://flask.palletsprojects.com/) - A lightweight WSGI web application framework.
* **Frontend**: HTML, CSS
* **Database**: SQLite - A lightweight disk-based database.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/SachinRawat1604/Task-Management-Web-App-with-Flask.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Task-Management-Web-App-with-Flask
   ```

3. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   ```

   -TaskManagement is virtual environment of this project.

4. **Activate the virtual environment**:

   * On Windows:

     ```bash
     venv\Scripts\activate
     ```

   * On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:

   ```bash
   python main.py
   ```

2. **Access the application**:

   Open your web browser and navigate to `http://localhost:5000`.

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
├── TaskManagement  (venv)
├── database.db
├── requirements.txt
└── README.md
```

* **static/**: Contains static files like CSS.
* **templates/**: Contains HTML templates.
* **main.py**: The main Flask application file.
* **database.db**: SQLite database file.
* **requirements.txt**: Lists the Python dependencies.
* **README.md**: Project documentation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/SachinRawat1604/Task-Management-Web-App-with-Flask/blob/main/LICENSE) file for details.
