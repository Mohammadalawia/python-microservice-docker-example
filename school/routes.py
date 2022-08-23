from flask import jsonify
from flask import current_app as app
from .model import student



@app.route('/', methods=['GET'])
def index():
    try:
        return jsonify(students_table=[i.serialize for i in student.query.all()])
    except Exception as e:
        return f"coudn't connect to database :{e}"


@app.route('/hello', methods=['GET'])
def hello():
    return "hello"




# @app.route('/teachers')
# def teachers():
#     return jsonify(teachers_table=)

# @app.route('/classes')
# def classes():
#     return jsonify(classes_table=)

# @app.route('/student_class')
# def student_class():
#     return jsonify(student_class=)

# @app.route('/subject')
# def subject():
#     return jsonify(subject=)

# @app.route('/classroom')
# def classroom():
#     return jsonify(classroom=)

