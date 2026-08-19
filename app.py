from flask import Flask, render_template, request, redirect
from manager import StudentManager

app = Flask(__name__)
manager = StudentManager()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        sid = request.form['sid']
        name = request.form['name']
        course = request.form['course']

        manager.add_student(sid, name, course)
        return redirect('/students')

    return render_template('add_student.html')

@app.route('/students')
def view_students():
    students = manager.get_all_students()
    return render_template('view_students.html', students=students)

if __name__ == "__main__":
    app.run(debug=True)