from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []  # List to store the tasks

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['task']
        task_description = request.form['description']
        
        # Limit the description to 250 characters or less
        task_description = task_description[:250]

        tasks.append({'content': task_content, 'description': task_description, 'completed': False})
        return redirect(url_for('todolist2'))
    return render_template('todolist2.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.pop(task_id)
    return redirect(url_for('todolist2'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    tasks[task_id]['completed'] = True
    return redirect(url_for('todolist2'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)

