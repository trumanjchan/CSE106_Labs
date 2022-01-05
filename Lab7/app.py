from flask import Flask, render_template, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine('sqlite:///testing.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

db = SQLAlchemy(app)


class Students(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, primary_key=True)
    grade = db.Column(db.String, unique=False, nullable=False)

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return "<Student (name='%s', grade='%s')>" % (self.name, self.grade)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route('/grades/<student>', methods=['GET'])
def getStudent(student):
    user = Students.query.filter_by(name='%s' % student).first()
    return str({ user.grade })


@app.route('/grades', methods=['GET'])
def getGrades():
    return str([i.as_dict() for i in Students.query.all()])


@app.route('/<student>/<grade>', methods=['GET', 'POST'])
def postNew(student, grade):
    newEntry = Students(name=student, grade=grade)
    db.session.add(newEntry)
    db.session.commit()

    return f'<h1>Added New User: {newEntry.name, newEntry.grade}</h1>'


@app.route('/<student>/<grade>', methods=['GET', 'PUT'])
def putGrade(student, grade):
    deleteExistingEntry = Students.query.filter_by(name=student).first()
    db.session.delete(deleteExistingEntry)
    db.session.commit()

    newUser = Students(name=student, grade=grade)
    db.session.add(newUser)
    db.session.commit()

    return f'<h1>Changed User Grade: {newUser.name, newUser.grade}</h1>'


@app.route('/<student>', methods=['GET', 'DELETE'])
def deleteStudent(student):
    user = Students.query.filter_by(name='%s' % student).first()
    db.session.delete(user)
    db.session.commit()

    return f'<h1>Deleted User: {user.name}</h1>'


@app.route('/')
def index():
    return render_template("index7.html", students=Students.query.all())


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run()
