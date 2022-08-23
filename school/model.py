
from school import db


class student(db.Model): 
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Enum('male', 'female'), nullable=False)

    def __init__(self, student_id, student_name, address,gender):
        self.student_id = student_id
        self.student_name = student_name
        self.address = address
        self.gender=gender

    def create(student_id, student_name,address,gender):
        me = student(student_id,student_name,address,gender)
        db.session.add(me)
        db.session.commit()

    def __repr__(self):
        students = {"studentid":self.student_id,"student name":self.student_name,"Address":self.address,"Gender":self.gender}
        return f"{students}"

    @property
    def serialize(self):
        return {"studentid":self.student_id,"student name":self.student_name,"Address":self.address,"Gender":self.gender}
   



# class student(db.Model): 
#     student_id = db.Column(db.Integer, primary_key=True)
#     student_name = db.Column(db.String(100), nullable=False)
    # DOB = db.Column(db.DateTime, nullable=False)
    # address = db.Column(db.String(100), nullable=False)
    # gender = db.Column(db.Enum('male', 'female'), nullable=False)
    
    # def __init__(self, student_id: int, student_name: str):
    #     self.student_id = student_id
    #     self.student_name = student_name

    # def create(student_id, student_name):
    #     me = student(student_id,student_name)
    #     db.session.add(me)
    #     db.session.commit()




    # def __repr__(self):
    #     return f"Id :{student.student_id} , student_name : {student.student_name} , Date of birth:{student.DOB}, address:{student.address},gender:{student.gender}"



# class student_class(db.Model):
#     class_student_id = db.Column(db.Integer, primary_key=True, nullable=False)
#     class_id = db.Column(db.Integer, db.ForeignKey('casses.class_id'), nullable=False)
#     student_id = db.Column(db.String(100), db.ForeignKey('student.student_id'),unique=True, nullable=False)
    
#     def __repr__(self):
#         return f"current classes:{student_class.class_id}, class id:{student_class.class_id},student id:{student_class.student_id}"


# class classes(db.Model):
#     class_id = db.Column(db.Integer, primary_key=True)
#     class_name = db.Column(db.String(100), nullable = False)
#     subject_id = db.Column(db.Integer, db.ForeignKey('subject.subject_id'), nullable = False)
#     teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable = False)
#     classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.classroom_id'), nullable = False)
    
#     def __repr__(self):
#         return f"class id:{classes.class_id}, class name:{classes.class_name}, classroom:{classes.classroom_id},subject:{classes.subject_id},teacher:{classes.teacher_id}"



# class subject(db.Model):
#     subject_id = db.Column(db.Integer, primary_key=True)
#     subject_name = db.Column(db.String(100), nullable = False)
#     subject_teacher = db.Column(db.String(100), nullable=False)
#     passing_mark = db.Column(db.Integer ,nullable=False)
    
#     def __repr__(self):
#         return f"subject id:{subject.subject_id}, subject name:{subject.subject_name, }subject teacher:{subject.subject_teacher}, passing mark:{subject.passing_mark}"


# class teachers(db.Model):
#     teacher_id = db.Column(db.Integer, primary_key=True)
#     teacher_name = db.Column(db.String(100), nullable=False)
#     teacher_address = db.Column(db.Integer,  nullable=False)
#     gender = db.Column(db.Enum('male', 'female'), nullable=False)
#     DOB = db.Column(db.DateTime, nullable = False)
#     working_days = db.Column(db.String(200), nullable=False)
#     join_date= db.Column(db.DateTime, nullable = False)
#     teaching_subject = db.Column(db.String(100), nullable=False)

#     def __repr__(self):
#         return f"{teachers.teacher_id},{teachers.teacher_name},{teachers.teacher_address},{teachers.gender},{teachers.DOB},{teachers.working_days},{teachers.join_date},{teachers.teaching_subject}"


# class classroom(db.Model):
#     classroom_id = db.Column(db.Integer,primary_key=True, nullable=False)
#     stu_capacity = db.Column(db.Integer, nullable=False)
#     room_type = db.Column(db.Enum('small', 'meduim' , 'stage'), nullable=False)
    
#     def __repr__(self):
#         return f"{classroom.classroom_id}{classroom.stu_capacity}{classroom.room_type}"
        




# def dump_datetime(value):
#     """Deserialize datetime object into string form for JSON processing."""
#     if value is None:
#         return None
#     return [value.strftime("%Y-%m-%d")]

