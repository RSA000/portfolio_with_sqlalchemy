from crypt import methods
from flask import (render_template, session,
                 url_for, request, redirect)
from models import db, Projects, app
import os

projects = Projects.query.all()

@app.route('/')
def index():
    return render_template("index.html", projects=projects)


@app.route('/about')
def about():
    return render_template('about.html', projects=projects)


@app.route('/projects/add', methods=['GET', 'POST'])
def add_project():
    if request.form:
        print(request.form)
        new_project = Projects(
                        title=request.form['title'], date=request.form['date'],
                        description=request.form['desc'], skills=request.form['skills'],
                        url=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


@app.route('/projects/<id>')
def projects_id(id):
    project = Projects.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    project = Projects.query.get_or_404(id)
    if request.form:
        project.title = request.form['title']
        project.date = request.form['date']
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.url = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', project=project)

@app.route('/projects/<id>/delete')
def delete(id):
        project = Projects.query.get_or_404(id)
        db.session.delete(project)
        db.session.commit()
        return redirect(url_for('index'))

    


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')