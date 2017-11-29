from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from django.http import *
from .models import USER,Student,Courses,StudentCourseEnrollment,Assesment,AssesmentMark,OfferedCourse,CourseTeacher,Teacher,CourseMaterial
from .forms import SignupForm,StudentForm
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .context_processors import user_information
from django.template import loader
from django.template import RequestContext



def Index(request):
    try:
        return render(request,'homepage/index.html')
    except:
        raise Http404
def Home(request):
    try:
        return render(request,'homepage/index.html')
    except:
        raise Http404
def signUp(request):
    try:
        form=SignupForm()
        student_form=StudentForm()
        if request.method=="POST":
            form=SignupForm(request.POST or None, request.FILES or None)
            std_form=StudentForm(request.POST or None)
            if form.is_valid():
                username=request.POST.get('username',None)         
                usertype=request.POST.get('user_type',None)
                if username is not None and username != '':
                    user_list=USER.objects.all()
                    for i in user_list:
                        user=username==i.username
                        if user:
                            u_list = USER.objects.filter(username=username)
                            return HttpResponse('<script> alert("Already Exists"); </script>') 
                    signUp_save = form.save(commit=False)
                    signUp_save.save()
                    #std=Student(id=signUp_save.id)
                    u = USER.objects.filter(username=username)
                    #std=Student(user_id=u.id)
                    if std_form.is_valid():
                        #std_save.user_id=signUp_save
                        std_save = std_form.save(commit=False)
                        std_save.save()
                        #std_form.save()
                    #if usertype=='1':

                return redirect("Login")
            else:
                form=SignupForm()
                return  render(request,'homepage/signUp.html')
        return  render(request,'homepage/signUp.html')
   
    except:
        raise Http404

     


def Login(request):
    if request.method=='POST':
        username=request.POST.get('username',None)
        password=request.POST.get('password', None)
        if username is not None and password is not None and username != '' and password != "":
            student_list=USER.objects.all()
            for id in student_list:
                user=username==id.username and password==id.password
                if user:
                    s_list = USER.objects.filter(username=username)
                    request.session['student_username']=id.username
                    if id.user_type=='1':    
                        context={}
                        text={}
                        context['u_list']=request.session['student_username']
                        text = {'info_list': s_list,'u_list': context['u_list']}
                        return render(request, 'student/students.html',text)                       
                    else:
                        context={}
                        text={}
                        context['u_list']=request.session['student_username']
                        text = {'info_list': s_list,'u_list': context['u_list']}
                        return render(request, 'teacher/teacher_home.html', text)

        else:
            return HttpResponse('<script> alert("Empty Filed") </script>')
    return render(request,'homepage/login.html')

def Logout(request):
    del request.session['student_username']
    return redirect('/')
    #return  render(request,'homepage/index.html')








#Students Views
def registrationstatus(request):
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id3 = article.id
    s_list = Student.objects.filter(user=id3)
    for article in s_list:
        id = article.id
    sce_list = StudentCourseEnrollment.objects.filter(student=id,status=2)
    c=0

    for i in sce_list:
        p=i.offeredcourse.course.Credit
        c=c+p
    current_list = StudentCourseEnrollment.objects.filter(student=id,status=1)
    r=0
    
    for i in current_list:
        p=i.offeredcourse.course.Credit
        r=r+p
    #print c
    text = {'u_list': request.session['student_username'],'c':c,'r':r}
    template=loader.get_template('student/RegistrationStatus.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))


def index(request):
    context={}
    context['u_list']=request.session['student_username']
    template=loader.get_template('student/students.html')
    data=RequestContext(request,context)
    return HttpResponse(template.render(data))
    #return render(request,'student/students.html')

def studentsProfile(request):
    context={}
    text={}
    s_data=[]
    s_list = USER.objects.filter(username=request.session['student_username'])
    for i in s_list:
        uid=i.id

    s_info= Student.objects.filter(user=uid)
    for ip in s_info:
        s_data.append(ip)
    
    text = {'info_list': s_list,'u_list': request.session['student_username'],'s_data':s_data}
    template=loader.get_template('student/studentsProfile.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))

def StudentsDashboard(request):
    context={}
    text={}
    s_list = USER.objects.filter(username=request.session['student_username'])
    text = {'info_list': s_list,'u_list': request.session['student_username']}
    template=loader.get_template('student/students.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))
    

def studentsAllCourse(request):
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id
    s_list = Student.objects.filter(user=id)
    for article in s_list:
        id = article.id
    sce_list = StudentCourseEnrollment.objects.filter(student=id)
    m=len(sce_list)

    text = {'info_list': sce_list,'u_list': request.session['student_username'],'m':m }
    template=loader.get_template('student/allCourse.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))

def studentsCurrentcourse(request):
    context={}

    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id
    s_list = Student.objects.filter(user=id)
    for article in s_list:
        id = article.id
    sce_list = StudentCourseEnrollment.objects.filter(student=id,status=1)
    m=len(sce_list)

    text = {'info_list': sce_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('student/currentcourse.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))



def studentsPrevCourse(request):
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id
    s_list = Student.objects.filter(user=id)
    for article in s_list:
        id = article.id
    sce_list = StudentCourseEnrollment.objects.filter(student=id,status=2)
    m=len(sce_list)

    text = {'info_list': sce_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('student/prevCourse.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))
    

def stdcoursematerials(request):

    id2=request.GET.get('id')

    context={}

    mat_list=CourseMaterial.objects.filter(offeredcourse=id2)
    m=len(mat_list)

    offeredcourse_list=OfferedCourse.objects.filter(id=id2)
    #print offeredcourse_list

    text = {'info_list': mat_list,'of_list':offeredcourse_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('student/stdCourseMaterials.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data)) 

def studentsforum(request):
    context={}
    context['u_list']=request.session['student_username']
    template=loader.get_template('student/studentsForum.html')
    data=RequestContext(request,context)
    return HttpResponse(template.render(data))


def studentsBLogs(request):
    context={}
    context['u_list']=request.session['student_username']
    template=loader.get_template('student/studentsBLogs.html')
    data=RequestContext(request,context)
    return HttpResponse(template.render(data))
    return render(request,'student/studentsBLogs.html')


def studentProfileUpdate(request):
    context={}
    text={}
    s_data=[]
    s_list = USER.objects.filter(username=request.session['student_username'])
    for i in s_list:
        uid=i.id

    s_info= Student.objects.filter(user=uid)
    for ip in s_info:
        s_data.append(ip)

    text = {'info_list': s_list,'u_list': request.session['student_username'],'s_data':s_data}
    template=loader.get_template('student/updateStudentProfile.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))

# def studentProUpdate(request):
#     id=request.GET.get('id')
#     user=USER.objects.get(id=id)
#     form=UpdateForm()
#     if request.method=="POST":
#         form=UpdateForm(request.POST or None, request.FILES or None)
#         if form.is_valid:
#             signUp_save = form.save(commit=False)
#             signUp_save.save()





def studentviewfinalAssesments(request):
    id2=request.GET.get('id')
    context={}
    arr_list=[]
    temp=[]
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id3 = article.id

    s_data=Student.objects.filter(user=id3)
    for ar in s_data:
        ids = ar.id
        arr_list.append(ar.std_id)

    sc_list= StudentCourseEnrollment.objects.filter(offeredcourse=id2)
    mat_list=Assesment.objects.filter(offeredcourse=id2)
    for article in mat_list:
        id=article.id
        #print id
        assesment_marks=AssesmentMark.objects.filter(assesment=id,student=ids)
        for i in assesment_marks:
            idss=i.mark
            #print idss
            arr_list.append(i.mark)
    temp=[0]*6
    for i in arr_list:
        temp.append(i)
    temp.sort(reverse=True)
    a = temp[1]+temp[2]+temp[3]+temp[4]
    offeredcourse_list=OfferedCourse.objects.filter(id=id2)
    text = {'info_list': mat_list,'arr_list': arr_list,'of_list':offeredcourse_list,'u_list': request.session['student_username'],'a':a}
    template=loader.get_template('student/studentviewFinalAssesments.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))


def viewfinalassesments(request):
    id2=request.GET.get('id')
    context={}
    arr_list=[]
    g=[]
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id
    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id
    sc_list= StudentCourseEnrollment.objects.filter(offeredcourse=id2)
    mat_list=Assesment.objects.filter(offeredcourse=id2,teacher=id)
    c=0
    for item in sc_list:
        p=item.student
        arr_list.append([])
        arr_list[c].append(item.student)
        for article in mat_list:
            id=article.id
            assesment_marks=AssesmentMark.objects.filter(assesment=id,student=p)
            for i in assesment_marks:
                arr_list[c].append(i.mark)
        c=c+1        
    #print arr_list
    #print m 
    m=len(mat_list)
    ct_list=CourseTeacher.objects.filter(teacher=id,status=1)
    offeredcourse_list=OfferedCourse.objects.filter(id=id2)
    text = {'info_list': mat_list,'arr_list': arr_list,'g_list': g,'of_list':offeredcourse_list,'ct_list':ct_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/viewFinalAssesments.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))


def showallfinalasesmentsforteacher(request):
    id2=request.GET.get('id')
    context={}
    arr_list=[]
    marks=[]   
    temp=[]
    offeredcourse_list=OfferedCourse.objects.filter(id=id2)
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        idt = article.id
    sc_list= StudentCourseEnrollment.objects.filter(offeredcourse=id2)
    mat_list=Assesment.objects.filter(offeredcourse=id2)
    m=len(mat_list)
    #print m
    c=0
    for item in sc_list:
        p=item.student
        arr_list.append([])
        arr_list[c].append(item.student)
        temp=[0]*6
        marks=[0]*6
        for article in mat_list:
            id=article.id
            assesment_marks=AssesmentMark.objects.filter(assesment=id,student=p)
            for i in assesment_marks:
                arr_list[c].append(i.mark)
            marks.append(i.mark)
        
        for k in marks:
                #print k
                temp.append(k)        
        
        temp.sort(reverse=True,key=int)
        #print temp
        a = temp[0]+temp[1]+temp[2]+temp[3]
        arr_list[c].append(a)
        #print a
        c=c+1

    #print arr_list
    text = {'of_list':offeredcourse_list,'info_list': mat_list,'u_list': request.session['student_username'],'arr_list':arr_list}
    template=loader.get_template('teacher/showallFinalAssesmentsforteacher.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))



#HomePage
def AcademicsPage(request):
    return  render(request,'homepage/academicsPage.html')

def FacultyMember(request):
    return  render(request,'homepage/facultyMembers.html')

def ResearchPage(request):
    return render(request,'homepage/researchPage.html')

def ActivitesPage(request):
    return render(request,'homepage/activitiesPage.html')

def BlogsPage(request):
    return render(request,'homepage/blogsPage.html')

def ForumPage(request):
    return render(request,'homepage/forumPage.html')

def OnlineExam(request):
    return render(request,'homepage/onlineExamPage.html')

def GalleryPage(request):
    return render(request,'homepage/galleryPage.html')

def ContactUsPage(request):
    return render(request,'homepage/contactUsPage.html')
def ForgetPass(request):
    return render(request,'homepage/forgetPage.html')


#Teacher Views

def teacher(request):
    context={}
    text={}
    s_list = USER.objects.filter(username=request.session['student_username'])
    text = {'info_list': s_list,'u_list': request.session['student_username']}
    template=loader.get_template('teacher/teacher_home.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))

    #context={}
    #context['u_list']=request.session['student_username']
    #mplate=loader.get_template('teacher/teacher_home.html')
    #data=RequestContext(request,context)
    #return HttpResponse(template.render(data))
        
def teacher_profile(request):
    context={}
    text={}
    s_list = USER.objects.filter(username=request.session['student_username'])
    for i in s_list:
        id=i.id
    t_data=Teacher.objects.filter(user=id)

    for j in t_data:
        p=j.designation

    if(p==4):
        t="Lecturer"
    elif(p==1):
        t="Professor"
    elif(p==2):
        t="Associate Professor"
    elif(p==3):
        t="Assistant Professor"

    text = {'info_list': s_list,'u_list': request.session['student_username'],'t':t}
    template=loader.get_template('teacher/teachersProfile.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))


def teacherAllcourse(request):
    # context={}
    # context['u_list']=request.session['student_username']
    # template=loader.get_template('teacher/teacherAllCourse.html')
    # data=RequestContext(request,context)
    # return HttpResponse(template.render(data))
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id
    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id
    sce_list = CourseTeacher.objects.filter(teacher=id)
    m=len(sce_list)
    text = {'info_list': sce_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/teacherAllCourse.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))

def updateTeacherprofile(request):
    context={}
    text={}
    s_list = USER.objects.filter(username=request.session['student_username'])
    text = {'info_list': s_list,'u_list': request.session['student_username']}
    template=loader.get_template('teacher/updateTeacherProfile.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))

def teacherforum(request):
    context={}
    context['u_list']=request.session['student_username']
    template=loader.get_template('teacher/teacherForum.html')
    data=RequestContext(request,context)
    return HttpResponse(template.render(data))

def teacherblogs(request):
    context={}
    context['u_list']=request.session['student_username']
    template=loader.get_template('teacher/teacherBlogs.html')
    data=RequestContext(request,context)
    return HttpResponse(template.render(data))

def teachercurrentcourse(request):
    # context={}
    # context['u_list']=request.session['student_username']
    # template=loader.get_template('teacher/teacherCurrentCourse.html')
    # data=RequestContext(request,context)
    # return HttpResponse(template.render(data))
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id

    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id

    sce_list = CourseTeacher.objects.filter(teacher=id,status=1)
    m=len(sce_list)

    text = {'info_list': sce_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/teacherCurrentCourse.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))

def teacherprevcourse(request):
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id
    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id
    sce_list = CourseTeacher.objects.filter(teacher=id,status=2)
    m=len(sce_list)
    text = {'info_list': sce_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/teacherPrevCourse.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))


def teachercoursematerials(request):
    # context={}
    # context['u_list']=request.session['student_username']
    # template=loader.get_template('teacher/teacherCourseMaterials.html')
    # data=RequestContext(request,context)
    # return HttpResponse(template.render(data))
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id

    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id

    sce_list = CourseMaterial.objects.filter(teacher=id)
    for article in sce_list:
        id = article.id
    m=len(sce_list)
    text = {'info_list': sce_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/teacherCourseMaterials.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))   


def teachercurrentcoursematerials(request):
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id

    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id

    sce_list = CourseMaterial.objects.filter(teacher=id)
    for article in sce_list:
        id = article.id
    m=len(sce_list)
    text = {'info_list': sce_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/teachercurrentCourseMaterials.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))    


def single(request):
    id=request.GET.get('id')
    #print id
    mat_list=CourseMaterial.objects.filter(offeredcourse=id)
    text = {'info_list': mat_list}
    template=loader.get_template('teacher/single.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))
    #return HttpResponse("Hello")

def coursematerial(request):
    id2=request.GET.get('id')
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id

    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id

    mat_list=CourseMaterial.objects.filter(offeredcourse=id2,teacher=id)
    m=len(mat_list)

    offeredcourse_list=OfferedCourse.objects.filter(id=id2)
    #print offeredcourse_list

    text = {'info_list': mat_list,'of_list':offeredcourse_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/courseMaterials.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data)) 



def assesments(request):
    id2=request.GET.get('id')

    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id

    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id

    mat_list=Assesment.objects.filter(id=id2,teacher=id)
    for article in mat_list:
        id= article.id

    assesment_marks=AssesmentMark.objects.filter(assesment=id2)

    m=len(mat_list)

    offeredcourse_list=OfferedCourse.objects.filter(id=id2)
    #print offeredcourse_list

    text = {'info_list': assesment_marks,'mat_list': mat_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/assesments.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data)) 


def teacheraddcoursematerials(request):
    # context={}
    # context['u_list']=request.session['student_username']
    # template=loader.get_template('teacher/teacherAddCourseMaterials.html')
    # data=RequestContext(request,context)
    # return HttpResponse(template.render(data))
     #   return render(request,'teacher/teacherAddCourseMaterials.html')
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id

    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id

    sce_list = CourseTeacher.objects.filter(teacher=id,status=1)
    for article in sce_list:
        id = article.id

    m=len(sce_list)
    text = {'info_list': sce_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/teacherAddCourseMaterials.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))

def teachersassesment(request):
    # context={}
    # context['u_list']=request.session['student_username']
    # template=loader.get_template('teacher/teachersAssesment.html')
    # data=RequestContext(request,context)
    # return HttpResponse(template.render(data))
    #    return render(request,'teacher/teachersAssesment.html')
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id

    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id

    sce_list = Assesment.objects.filter(teacher=id)
    for article in sce_list:
        id = article.id

    m=len(sce_list)
    text = {'info_list': sce_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/teachersAssesment.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))

def teachersnewassesment(request):
    # context={}
    # context['u_list']=request.session['student_username']
    # template=loader.get_template('teacher/teachersNewAssesment.html')
    # data=RequestContext(request,context)
    # return HttpResponse(template.render(data))
     #   return render(request,'teacher/teachersNewAssesment.html')
    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id

    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id

    sce_list = CourseTeacher.objects.filter(teacher=id,status=1)
    for article in sce_list:
        id = article.id

    m=len(sce_list)
    text = {'info_list': sce_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/teachersNewAssesment.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))

def teacherscurrentassesment(request):
    context={}
    context['u_list']=request.session['student_username']
    template=loader.get_template('teacher/teachersCurrentAssesment.html')
    data=RequestContext(request,context)
    return HttpResponse(template.render(data))
    #    return render(request,'teacher/teachersCurrentAssesment.html')

def prevteachersassesment(request):
    context={}
    context['u_list']=request.session['student_username']
    template=loader.get_template('teacher/prevTeachersAssesment.html')
    data=RequestContext(request,context)
    return HttpResponse(template.render(data))
    #    return render(request,'teacher/prevTeachersAssesment.html')

def teacherfinalassesment(request):
    context={}
    context['u_list']=request.session['student_username']
    template=loader.get_template('teacher/teacherFinalAssesment.html')
    data=RequestContext(request,context)
    return HttpResponse(template.render(data))
      #  return render(request,'teacher/teacherFinalAssesment.html')

def teacherPCourse(request):
    context={}
    context['u_list']=request.session['student_username']
    template=loader.get_template('teacher/teacherPCourse.html')
    data=RequestContext(request,context)
    return HttpResponse(template.render(data))
        #return  render(request,'teacher/teacherPCourse.html')


def assesmentsList(request):

    context={}
    u_list = USER.objects.filter(username=request.session['student_username'])
    for article in u_list:
        id = article.id

    s_list = Teacher.objects.filter(user=id)
    for article in s_list:
        id = article.id

    sce_list = Assesment.objects.filter(teacher=id)
    for article in sce_list:
        id = article.id

    ass_list = AssesmentMark.objects.filter(assesment=id)
    for article in sce_list:
        id = article.id

    m=len(sce_list)
    text = {'info_list': ass_list,'u_list': request.session['student_username'],'m':m}
    template=loader.get_template('teacher/AssesmentsList.html')
    data=RequestContext(request,text)
    return HttpResponse(template.render(data))


    # context={}
    # context['u_list']=request.session['student_username']
    # template=loader.get_template('teacher/AssesmentsList.html')
    # data=RequestContext(request,context)
    # return HttpResponse(template.render(data))
     #   return  render(request,'teacher/viewFinalAssesments.html')

def currentteachersassesmentFinal(request):
    context={}
    context['u_list']=request.session['student_username']
    template=loader.get_template('teacher/currentTeachersAssesmentFinal.html')
    data=RequestContext(request,context)
    return HttpResponse(template.render(data))
        #return render(request,'teacher/currentTeachersAssesmentFinal.html')

def prevteachersassesmentfinal(request):
    context={}
    context['u_list']=request.session['student_username']
    template=loader.get_template('teacher/prevTeachersAssesmentFinal.html')
    data=RequestContext(request,context)
    return HttpResponse(template.render(data))
        #return render(request,'teacher/prevTeachersAssesmentFinal.html')



#Admin Views

def adminpage(request):
    return render(request,'adminpage/adminHeader.html')

def addCourseInformation(request):
    return render(request,'adminpage/addCourseInformation.html')

def adminHeader(request):
    return render(request,'adminpage/adminHeader.html')

def adminProfile(request):
    return render(request,'adminpage/adminProfile.html')

def allCourse_admin(request):
    return render(request,'adminpage/allCourse.html')

def currentCourse_admin(request):
    return render(request,'adminpage/currentCourse.html')

def offeredCourse(request):
    return render(request,'adminpage/offeredCourse.html')

def prevCourse_admin(request):
    return render(request,'adminpage/prevCourse.html')

def studentList(request):
    return render(request,'adminpage/studentList.html')

def teacherList(request):
    return render(request,'adminpage/teacherList.html')

def updateAdminProfile(request):
    return render(request,'adminpage/updateAdminProfile.html')

def viewFinalAssesments(request):
    return render(request,'adminpage/viewFinalAssesments.html')