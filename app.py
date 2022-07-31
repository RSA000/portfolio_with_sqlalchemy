from flask import (render_template,
                 url_for, request, redirect)
from models import db, Projects, app

app.static_folder = 'static'
@app.route('/')
def index():
    projects = Projects.query.all()
    return render_template("index.html", projects=projects)


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
    return render_template('projectform.html')


@app.route('/projects/<id>')
def projects_id(id):
    project = Projects.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.route('/projects/<id>/edit')
def edit():
    return render_template('projectform.html')

@app.route('/projects/<id>/delete')
def delete():
    pass
    




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')