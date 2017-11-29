from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings

from . import views



urlpatterns = [

	url(r'^$',views.Index,name='index'),
	url(r'^index$',views.Home,name='Home'),
	url(r'^signUp$',views.signUp,name='signUp'),
	url(r'^Login$',views.Login,name='Login'),
	url(r'^Logout$',views.Logout,name='Logout'),



#HomePage URL
	url(r'^AcademicsPage$',views.AcademicsPage, name='AcademicsPage'),
	url(r'^FacultyMember$',views.FacultyMember,name='FacultyMember'),
	url(r'^ResearchPage$',views.ResearchPage,name='ResearchPage'),
	url(r'^ActivitesPage$',views.ActivitesPage,name='ActivitesPage'),
	url(r'^BlogsPage$',views.BlogsPage,name='BlogsPage'),
	url(r'^ForumPage$',views.ForumPage,name='ForumPage'),
	url(r'^OnlineExam$',views.OnlineExam,name='OnlineExam'),
	url(r'^GalleryPage$',views.GalleryPage,name='GalleryPage'),
	url(r'^ContactUsPage$',views.ContactUsPage,name='ContactUsPage'),
	url(r'^ForgetPass$',views.ForgetPass,name='ForgetPass'),





	#Students URL

	# url(r'^index',views.index,name='index'),
	# url(r'^StudentsDashboard',views.StudentsDashboard,name='StudentsDashboard'),
	# url(r'^studentsProfile',views.studentsProfile,name='studentsProfile'),
	# url(r'^allCourse',views.allCourse,name='allCourse'),
	# url(r'^currentcourse',views.currentcourse,name='currentcourse'),
	# url(r'^prevCourse',views.prevCourse,name='prevCourse'),
	# url(r'^studentsforum',views.studentsforum,name='studentsforum'),
	# url(r'^studentsBLogs',views.studentsBLogs,name='studentsBLogs'),
	# url(r'^updateStudentProfile',views.updateStudentProfile,name='updateStudentProfile'),
	url(r'^index$',views.index,name='index'),
	url(r'^StudentsDashboard$',views.StudentsDashboard,name='StudentsDashboard'),
	url(r'^studentsProfile$',views.studentsProfile,name='studentsProfile'),
	url(r'^studentsAllCourse$',views.studentsAllCourse,name='studentsAllCourse'),
	url(r'^studentsCurrentcourse$',views.studentsCurrentcourse,name='studentsCurrentcourse'),
	url(r'^studentsPrevCourse$',views.studentsPrevCourse,name='studentsPrevCourse'),
	url(r'^studentsforum$',views.studentsforum,name='studentsforum'),
	url(r'^studentsBLogs$',views.studentsBLogs,name='studentsBLogs'),
	url(r'^studentProfileUpdate$',views.studentProfileUpdate,name='studentProfileUpdate'),
	url(r'^stdCourseMaterials$',views.stdcoursematerials,name='stdCourseMaterials'),
	url(r'^studentviewFinalAssesments$',views.studentviewfinalAssesments,name='studentviewFinalAssesments'),
	url(r'^RegistrationStatus$',views.registrationstatus,name='RegistrationStatus'),







	#Teachers URL
	url(r'^teacher$',views.teacher,name='teacher'),
	url(r'^teacherProfile$',views.teacher_profile,name='teacherProfile'),
	url(r'^updateTeacherProfile$',views.updateTeacherprofile,name='updateTeacherProfile'),
	url(r'^teacherForum$',views.teacherforum,name='teacherForum'),
	url(r'^teacherBlogs$',views.teacherblogs,name='teacherBlogs'),
	url(r'^teacherAllCourse$',views.teacherAllcourse,name='teacherAllCourse'),
	url(r'^teacherCurrentCourse$',views.teachercurrentcourse,name='teacherCurrentCourse'),
	url(r'^teacherPrevCourse$',views.teacherprevcourse,name='teacherPrevCourse'),
	url(r'^teacherCourseMaterials$',views.teachercoursematerials,name='teacherCourseMaterials'),
	url(r'^teachercurrentCourseMaterials$',views.teachercurrentcoursematerials,name='teachercurrentCourseMaterials'),
	url(r'^teacherPCourse$',views.teacherPCourse,name='teacherPCourse'),
	url(r'^teacherAddCourseMaterials$',views.teacheraddcoursematerials,name='teacherAddCourseMaterials'),
	url(r'^teachersAssesment$',views.teachersassesment,name='teachersAssesment'),
	url(r'^teachersNewAssesment$',views.teachersnewassesment,name='teachersNewAssesment'),
	url(r'^teachersCurrentAssesment$',views.teacherscurrentassesment,name='teachersCurrentAssesment'),
	url(r'^prevTeachersAssesment$',views.prevteachersassesment,name='prevTeachersAssesment'),
	url(r'^teacherFinalAssesment$',views.teacherfinalassesment,name='teacherFinalAssesment'),
	url(r'^viewFinalAssesments$',views.viewfinalassesments,name='viewFinalAssesments'),
	url(r'^assesmentsList$',views.assesmentsList,name='assesmentsList'),
	url(r'^assesments$',views.assesments,name='assesments'),
	url(r'^currentTeachersAssesmentFinal$',views.currentteachersassesmentFinal,name='currentTeachersAssesmentFinal'),
	url(r'^prevFinalTeachersAssesment$',views.prevteachersassesmentfinal,name='prevFinalTeachersAssesment'),
	url(r'^courseMaterial$',views.coursematerial,name='courseMaterial'),
	url(r'^single$',views.single,name='single'),




	#Admin URL

	url(r'^adminpage$',views.adminpage,name='adminpage'),
	url(r'^addCourseInformation$',views.addCourseInformation,name='addCourseInformation'),
	url(r'^adminHeader$',views.adminHeader,name='adminHeader'),
	url(r'^adminProfile$',views.adminProfile,name='adminProfile'),
	url(r'^allCourse_admin$',views.allCourse_admin,name='allCourse_admin'),
	url(r'^currentCourse_admin$',views.currentCourse_admin,name='currentCourse_admin'),
	url(r'^offeredCourse$',views.offeredCourse,name='offeredCourse'),
	url(r'^prevCourse_admin$',views.prevCourse_admin,name='prevCourse_admin'),
	url(r'^studentList$',views.studentList,name='studentList'),
	url(r'^teacherList$',views.teacherList,name='teacherList'),
	url(r'^updateAdminProfile$',views.updateAdminProfile,name='updateAdminProfile'),
	url(r'^viewFinalAssesments$',views.viewFinalAssesments,name='viewFinalAssesments'),
	url(r'^showallFinalAssesmentsforteacher$',views.showallfinalasesmentsforteacher,name='showallFinalAssesmentsforteacher'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

