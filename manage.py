from flask_script import Manager
from movielist import

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    Titanic = Title(date='December 14, 1997', about='Titanic is about a sinking boat', genre='drama')
    Jaws = Title(Date='June 20, 1975', about='Jaws is about a shark that attacks humans', genre='horror')
    Rocky = title(Date='November 21, 1976', about='Rocky is about a boxer in Philly', genre='action')
    Grease = title(Date='May 1, 1971', about='Grease is about sumemr love', genre='drama')
    db.session.add(Titanic)
    db.session.add(Jaws)
    db.session.add(Rocky)
    db.session.add(Grease)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
