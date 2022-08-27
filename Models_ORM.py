from peewee import *

con = SqliteDatabase("brunoyam.db")


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = con
        order_by = 'id'


class Student(BaseModel):
    name = CharField()
    surname = CharField()
    age = IntegerField()
    city = CharField()

    class Meta:
        db_table = "Students"


class Course(BaseModel):
    name = CharField()
    time_start = DateField()
    time_end = DateField()

    class Meta:
        db_table = "Courses"


class StudentCourse(BaseModel):
    student_id = ForeignKeyField(Student)
    course_id = ForeignKeyField(Course)

    class Meta:
        db_table = "Student_courses"
