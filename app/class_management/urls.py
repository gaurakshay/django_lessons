from django.conf.urls import url, include

from class_management import views
from class_management.views import StudentListView, StudentDetailView, StudentEditView, InstructorListView, \
    InstructorEditView, StudentAddView, InstructorAddView, CourseListView, CourseQueryView, WelcomeView, CourseView, \
    InstructorFormView, CourseUpdateAjax

urlpatterns = [
    url(r'^mgmt/', include([
        # url(r'^$', views.welcome, name='welcome'),
        url(r'^$', WelcomeView.as_view(), name='welcome'),
        url(r'^students/', include([
            url(r'^$', StudentListView.as_view(), name='student_list'),
            url(r'^add/$', StudentAddView.as_view(), name='student_add'),
            url(r'^(?P<pk>\d+)/', include([
                url(r'^$', StudentDetailView.as_view(), name='student_details'),
                url(r'^edit/$', StudentEditView.as_view(), name='student_edit'),
            ])),
        ])),

        url(r'^instructors/', include([
            url(r'^$', InstructorListView.as_view(), name='instructor_list'),
            url(r'^add/$', InstructorAddView.as_view(), name='instructor_add'),
            url(r'^(?P<pk>\d+)/$', InstructorEditView.as_view(), name='instructor_edit'),
            # url(r'^(?P<pk>\d+)/$', InstructorFormView.as_view(), name='instructor_edit'),
        ])),


        # url(r'^instructors/$', InstructorListView.as_view(), name='instructor_list'),
        # # url(r'^mgmt/instructors/details/(?P<pk>\d+)/$', InstructorDetailView.as_view(), name='instructor_details'),
        # url(r'^instructors/(?P<pk>\d+)/$', InstructorEditView.as_view(), name='instructor_edit'),

        url(r'^courses/$', CourseListView.as_view(), name='courses'),
        # url(r'^courses/$', views.courses, name='courses'),
        # url(r'^courses/$', CourseView.as_view(), name='courses'),
        url(r'^ajax_courses/$', CourseQueryView.as_view(), name='ajax_courses'),
        url(r'^course_update_ajax/$', CourseUpdateAjax.as_view(), name='course_update_ajax')



    ])),
]
