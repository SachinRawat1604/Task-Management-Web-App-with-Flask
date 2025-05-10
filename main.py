from flask import Flask, render_template, request, redirect, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user,current_user

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "mysecretkey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


login_manger = LoginManager()
login_manger.login_view = 'login'
login_manger.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column (db.String(200), default='pending')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@login_manger.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username = username).first():
            flash('Username taken! Try another.', 'error')
            return redirect(url_for('register'))
        
        new_user = User(
            username = username,
            password = generate_password_hash(password, method='pbkdf2:sha256')
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Account Created! Login Now', 'Success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password,password):
            flash('Invalid credentials', 'error')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', tasks=tasks)

@app.route('/add_task',methods=['GET','POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        new_task = Task(
            title = title,
            description = description,
            user_id = current_user.id
        )

        db.session.add(new_task)
        db.session.commit()
        flash('Task added!','success')

        return redirect(url_for('dashboard'))
    return render_template('add_edit_task.html', task=None)
           
@app.route('/edit_task/<int:task_id>',methods=['GET','POST'])
@login_required
def edit_task(task_id):  
    task = Task.query.get_or_404(task_id)

    if task.user_id!= current_user.id:
        flash('Access Denied', 'error')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.status = request.form['status']

        db.session.commit()
        flash('Task Updated!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add_edit_task.html', task=task)

@app.route('/delete_task/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        flash("Unauthorized!", 'error')
        return redirect(url_for('dashboard'))
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted', 'Success')
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
