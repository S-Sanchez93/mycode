from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []  # List to store the tasks

@app.route('/', methods=['GET', 'POST'])
def todolist():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append({'content': task, 'completed': False})
        return redirect(url_for('todolist'))
    return render_template('todolist.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.pop(task_id)
    return redirect(url_for('todolist'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    tasks[task_id]['completed'] = True
    return redirect(url_for('todolist'))

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=2224)

