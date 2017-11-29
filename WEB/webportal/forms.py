from django.core.validators import RegexValidator
from django import forms
from .models import USER,Student,Department
from django.forms import ModelForm

class SignupForm(forms.ModelForm):
  email=forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)
  contact = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  class Meta:
    model=USER
    fields=('firstname','lastname','username','email','password','gender',
		'user_type','address','contact','image')

# class UpdateForm(forms.ModelForm):
#   email=forms.EmailField()
#   password = forms.CharField(widget=forms.PasswordInput)
#   contact = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#   class Meta:
#     model=USER
#     fields=('firstname','lastname','username','email','password','address','contact')
  

class StudentForm(forms.ModelForm):

  class Meta:
    model=Student
    #fields=('firstname','lastname','username','email','password','user_id')
    fields=('user','department','year','semester','std_id','session')
	


	#class Meta:
    #model=Student
    #fields=('year','semester','std_id','session','user_id','dept_id')












"""class DepartmentForm(forms.ModelForm):

  	class Meta:
    	model=Department
    	fields=('name','description')"""








"""class TeacherForm(forms.ModelForm):
  	class Teacher:
    	model=OfferedCourse
    	fields=('user_id','dept_id','designation')"""


"""class AssesmentForm(forms.ModelForm):
  	class Meta:
    	model=Assesment
    	fields=('id','title','type','offered_course_id','teacher_id','comment')"""


"""class AssesmentMarkForm(forms.ModelForm):
  	class Meta:
    	model=AssesmentMark
   	fields=('id','assesment_id','student_id','mark',)"""


"""class CoursesForm(forms.ModelForm):
  	class Meta:
    	model=Courses
    	fields=('code','title','type','Credit','year','semester','description')"""


"""class OfferedCourseForm(forms.ModelForm):
  	class Meta:
    	model=OfferedCourse
    	fields=('course_id','session','year','semester','startind_date')"""

"""class CourseMaterialForm(forms.ModelForm):
  	class Meta:
    	model=CourseMaterial
    	fields=('title','description','offered_course_id','teacher_id','created_date','updated_date')"""


