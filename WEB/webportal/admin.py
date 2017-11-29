from django.contrib import admin

from .models import USER,Department,Student,Teacher,Courses,OfferedCourse,Files,Assesment,CourseMaterial,AssesmentMark,StudentCourseEnrollment,CourseTeacher

class USERAdmin(admin.ModelAdmin):
    search_fields=['username','user_type']
    list_display=['username','email','user_type','gender','contact','address','image']
    #list_editable=['firstname','lastname']
    class Meta:
        model=USER

class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'description',]

    class Meta:
        model = Department


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['std_id']
    list_display = ['std_id', 'user','department','year','semester','session']

    class Meta:
        model = Student



class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['id','user_id','designation']
    list_display = ['user', 'department','designation']

    class Meta:
        model = Teacher


class CoursesAdmin(admin.ModelAdmin):
    search_fields = ['code']
    list_display = ['code','title', 'course_type','Credit','year','semester']

    class Meta:
        model = Courses

class OfferedCourseAdmin(admin.ModelAdmin):
    search_fields = ['course_id','year']
    list_display = ['course_id','year', 'semester','session','starting_date']

    class Meta:
        model = OfferedCourse


class FilesAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'name']

    class Meta:
        model = Files



class AssesmentAdmin(admin.ModelAdmin):
    search_fields = ['teacher','title']
    list_display = ['offeredcourse', 'teacher','title','asses_type','comment']

    class Meta:
        model = Assesment

class AssesmentMarkAdmin(admin.ModelAdmin):
    
    list_display = ['student', 'mark','assesment']

    class Meta:
        model = AssesmentMark


class CourseMaterialAdmin(admin.ModelAdmin):
    search_fields = ['offeredcourse','teacher']
    list_display = ['title', 'offeredcourse','teacher','created_date','updated_date']

    class Meta:
        model = CourseMaterial





class StudentCourseEnrollmentAdmin(admin.ModelAdmin):
    search_fields = ['student']
    list_display = ['student','offeredcourse','status']

    class Meta:
        model = StudentCourseEnrollment



class CourseTeacherAdmin(admin.ModelAdmin):
    search_fields = ['teacher']
    list_display = ['teacher','offeredcourse','status']

    class Meta:
        model = CourseTeacher


admin.site.register(USER,USERAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Courses,CoursesAdmin)
admin.site.register(OfferedCourse,OfferedCourseAdmin)
admin.site.register(Files,FilesAdmin)
admin.site.register(Assesment,AssesmentAdmin)
admin.site.register(CourseMaterial,CourseMaterialAdmin)
admin.site.register(AssesmentMark,AssesmentMarkAdmin)
admin.site.register(StudentCourseEnrollment,StudentCourseEnrollmentAdmin)
admin.site.register(CourseTeacher,CourseTeacherAdmin)




