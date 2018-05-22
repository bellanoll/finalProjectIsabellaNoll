my project will be a movie database with different movie titles, producers, and release dates.

Database design:

There are 2 tables.  In the first table (movie datesdescription) there is a column of the movie titles and the date the movie came out in theatres and a description.  In the second table (movie producersGenre) are movie titles and producers and genre.

instruction:

use Python version 2.7.x.
Install virtualenv if needed.
$ virtualenv venv
Then activate the virtual environment
$ source venv/bin/activate
Install packages
$ pip install -r requirements.txt
To initialize the database:
$ python manage.py deploy
To run the development server (use -d to enable debugger and reloader):
$ python manage.py runserver -d
# finalProjectIsabellaNoll
