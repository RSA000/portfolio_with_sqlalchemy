from flask import (render_template,
                 url_for, request, redirect)
from models import db, Projects, app


@app.route('/')
def index():
    pass


@app.route('/projects/new')
def new_projects():
    pass


@app.route('/projects/<id>')
def projects_id():
    pass


@app.route('/projects/<id>/edit')
def edit():
    pass

@app.route('/projects/<id>/delete')
def delete():
    pass




if __name__ == '__main__'