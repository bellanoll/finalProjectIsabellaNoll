import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class title(db.Model):
    __tablename__ = 'Movie titles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    songs = db.relationship('Song', backref='titles', cascade="delete")

@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')

@app.route('/movies')
def show_all_movie():
    artists = Artist.query.all()
    return render_template('movies-all.html', artists=artists)


@app.route('/movies/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'GET':
        return render_template('movies-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        about = request.form['about']

        # insert the data into the database
        artist = Movie(name=name, about=about)
        db.session.add(movies)
        db.session.commit()
        return redirect(url_for('show_all_movies'))

@app.route('/api/movies/add', methods=['POST'])
def add_ajax_movie():
    # get data from the form
    name = request.form['name']
    about = request.form['about']

    # insert the data into the database
    artist = Artist(name=name, about=about)
    db.session.add(movies)
    db.session.commit()
    # flash message type: success, info, warning, and danger from bootstrap
    flash('Artist Inserted', 'success')
    return jsonify({"id": str(movie.id), "name": movie.name})

    @app.route('/movies/edit/<int:id>', methods=['GET', 'POST'])
    def edit_movie(id):
        artist = movies.query.filter_by(id=id).first()
        if request.method == 'GET':
            return render_template('artist-edit.html', movie=movie)
        if request.method == 'POST':
            # update data based on the form data
            artist.name = request.form['name']
            artist.about = request.form['about']
            # update the database
            db.session.commit()
            return redirect(url_for('show_all_movies'))


@app.route('/movies/delete/<int:id>', methods=['GET', 'POST'])
def delete_movie(id):
    artist = Artist.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('artist-delete.html', movie=movie)
    if request.method == 'POST':
        # delete the artist by id
        # all related songs are deleted as well
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/api/movies/<int:id>', methods=['DELETE'])
def delete_ajax_movies(id):
    artist = Artist.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"id": str(movie.id), "name": movie.name})

    @app.route('/songs')
    def show_all_songs():
        songs = Song.query.all()
        return render_template('song-all.html', songs=songs)


    @app.route('/year/add', methods=['GET', 'POST'])
    def add_songs():
        if request.method == 'GET':
            artists = movies.query.all()
            return render_template('year-add.html', movie=movie)
        if request.method == 'POST':
            # get data from the form
            name = request.form['name']
            year = request.form['year']
            about = request.form['about']
            artist = Artist.query.filter_by(name=movie_name).first()
            song = title(name=name, year=year, about=about)

            # insert the data into the database
            db.session.add(year)
            db.session.commit()
            return redirect(url_for('show_all_years'))


    @app.route('/year/edit/<int:id>', methods=['GET', 'POST'])
    def edit_song(id):
        song = year.query.filter_by(id=id).first()
        artists = movie.query.all()
        if request.method == 'GET':
            return render_template('year-edit.html', movie=movie, year=year)
        if request.method == 'POST':
            # update data based on the form data
            year.name = request.form['name']
            year.year = request.form['year']
            song.lyrics = request.form['about']
            movie = movie.query.filter_by(name=movie_name).first()
            year.movie=movie
            # update the database
            db.session.commit()
            return redirect(url_for('show_all_years'))


    @app.route('/year/delete/<int:id>', methods=['GET', 'POST'])
    def delete_song(id):
        song = year.query.filter_by(id=id).first()
        artists = movie.query.all()
        if request.method == 'GET':
            return render_template('year-delete.html', year=year, movies=movies)
        if request.method == 'POST':
            # use the id to delete the song
            # song.query.filter_by(id=id).delete()
            db.session.delete(years)
            db.session.commit()
            return redirect(url_for('show_all_years'))


    @app.route('/api/year/<int:id>', methods=['DELETE'])
    def delete_ajax_year(id):
        song = year.query.get_or_404(id)
        db.session.delete(year)
        db.session.commit()
        return jsonify({"id": str(year.id), "name": year.year})


    @app.route('/about')
    def about():
        return render_template('about.html')


    @app.route('/users')
    def show_all_users():
        return render_template('user-all.html')


    @app.route('/form-demo', methods=['GET', 'POST'])
    def form_demo():
        # how to get form data is different for GET vs. POST
        if request.method == 'GET':
            first_name = request.args.get('name')
            if first_name:
                return render_template('form-demo.html', name=name)
            else:
                return render_template('form-demo.html', name=session.get('name'))
        if request.method == 'POST':
            session['name'] = request.form['name']
            # return render_template('form-demo.html', first_name=first_name)
            return redirect(url_for('form_demo'))


    @app.route('/user/<string:name>/')
    def get_user_name(name):
        # return "hello " + name
        # return "Hello %s, this is %s" % (name, 'administrator')
        return render_template('user.html', name=name)


    @app.route('/year/<int:id>/')
    def get_song_id(id):
        # return "This song's ID is " + str(id)
        return "Hi, this is %s and the song's id is %d" % ('administrator', id)



    if __name__ == '__main__':
        app.run(debug=True)
