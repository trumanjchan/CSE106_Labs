from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
dictionary = {'Hello':'Hi'}


@app.route('/grades/<student>', methods=['GET'])
def getStudent(student):
    return dictionary['%s' % student]


@app.route('/grades', methods=['GET'])
def getGrades():
    return dictionary


@app.route('/<student>/<grade>', methods=['GET', 'POST'])
def postNew(student, grade):
    dictionary[student] = grade
    return dictionary


@app.route('/<student>/<grade>', methods=['GET', 'PUT'])
def putGrade(student, grade):
    dictionary[student] = grade
    return dictionary


@app.route('/<student>', methods=['GET', 'DELETE'])
def deleteStudent(student):
    del dictionary['%s' % student]
    return dictionary

@app.route('/')
def index():
    return render_template("index6.html", result = dictionary)


if __name__ == '__main__':
    app.run()
