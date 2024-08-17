from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuration
DATABASE ='database.db'
TABLE_NAME = 'tasks'

# Create a table to store tasks if it doesn’t exist
def create_table():
    conn = sqlite3.connect(DATABASE)
    conn.execute(f'''CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL,
             description TEXT,status INTEGER DEFAULT 0)''')
    conn.close()

# Create the table when the app starts
create_table()

# Home page — Display tasks
@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Add new task
@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    description = request.form['description']
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO {TABLE_NAME} (title, description) VALUES (?, ?)', (title, description))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Update task status
@app.route('/update/<int:task_id>/<int:status>', methods=['GET'])
def update(task_id, status):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f'UPDATE {TABLE_NAME} SET status=? WHERE id=?', (status, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Delete task
@app.route('/delete/<int:task_id>', methods=['GET'])
def delete(task_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id=?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)