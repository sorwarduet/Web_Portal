
from django.db import models

class USER(models.Model):
	id = models.AutoField(primary_key=True)
	firstname=models.CharField(max_length=25)
	lastname=models.CharField(max_length=25)
	username=models.CharField(max_length=25)
	email=models.EmailField()
	password=models.CharField(max_length=25)
	gender=models.CharField(max_length=2)
	user_type=models.CharField(max_length=2)
	address=models.TextField(null=True)
	contact=models.CharField(max_length=15,null=True)
	image=models.FileField(upload_to='user/images/',null=True,blank=True)

	def __str__(self):
		return self.username

class Department(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, blank=False)
	description = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name

class Courses(models.Model):
	
	id = models.AutoField(primary_key=True)
	code=models.CharField(max_length=10)
	title=models.CharField(max_length=50)
	course_type=models.CharField(max_length=10)
	Credit=models.FloatField(max_length=10)
	year=models.IntegerField(max_length=2)
	semester=models.IntegerField(max_length=2)
	description=models.CharField(null=True,max_length=50)

	def __str__(self):
		return self.code

class OfferedCourse(models.Model):
	course = models.ForeignKey(Courses)
	session=models.CharField(max_length=20)#This may be changed
	year = models.IntegerField(max_length=2)#This may be changed
	semester = models.IntegerField(max_length=2)#This may be changed
	starting_date = models.DateField()
	
	
	#("Date"), default=datetime.date.today"""
	def __str__(self):
		return self.course.title

class Student(models.Model):
	#id = models.AutoField(primary_key=True)
	user= models.ForeignKey(USER)
	department = models.ForeignKey(Department)
	year = models.CharField(max_length=50, blank=True)
	semester = models.CharField(max_length=50, blank=True)
	std_id = models.CharField(max_length=15, blank=True)
	session = models.CharField(max_length=20, blank=True)
	#studentCourseEnrollment = models.ManyToManyField(OfferedCourse)

	def __str__(self):
		return self.std_id

 


class Teacher(models.Model):
	user = models.ForeignKey(USER)
	department = models.ForeignKey(Department)
	designation = models.IntegerField(max_length=2,blank=True)
	#courseTeacher = models.ManyToManyField(OfferedCourse)
	def __str__(self):
	  	return self.user.username


   
class StudentCourseEnrollment(models.Model):
	id = models.AutoField(primary_key=True)
	student = models.ForeignKey(Student) 
	offeredcourse = models.ForeignKey(OfferedCourse)
	status=models.IntegerField(max_length=2)
	def __str__(self):
		return self.student.std_id

class CourseTeacher(models.Model):
	id = models.AutoField(primary_key=True)
	teacher = models.ForeignKey(Teacher) 
	offeredcourse = models.ForeignKey(OfferedCourse)
	status = models.IntegerField(max_length=2)
	def __str__(self):
		return self.teacher.user.username

class Files(models.Model):
	id = models.AutoField(primary_key=True)
	title=models.CharField(null=True, max_length=50)
	name=models.FileField(upload_to='CourseMaterial/')

	def __str__(self):
		return self.title



class Assesment(models.Model):
	id = models.AutoField(primary_key=True)
	title=models.CharField(max_length=50)
	asses_type=models.CharField(max_length=10)
	offeredcourse = models.ForeignKey(OfferedCourse)
	teacher = models.ForeignKey(Teacher)
	comment=models.CharField(null=True,max_length=50)

	def __str__(self):
		return self.title



class CourseMaterial(models.Model):
	title=models.CharField(max_length=100)
	description=models.CharField(null=True,max_length=100)
	offeredcourse = models.ForeignKey(OfferedCourse)
	teacher = models.ForeignKey(Teacher)
	created_date = models.DateField()
	updated_date = models.DateField()
	files=models.ForeignKey(Files)

	def __str__(self):
		return self.title


class AssesmentMark(models.Model):
	assesment = models.ForeignKey(Assesment)
	student = models.ForeignKey(Student)
	mark=models.IntegerField(max_length=20)
	def __str__(self):
		return self.student.user.firstname