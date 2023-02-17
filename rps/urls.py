from django.urls import path

from . import views


# URLconf
urlpatterns = [
    path("", views.home_view, name="home"),
    path("students/", views.students_view, name="students"),
    path("teachers/", views.teachers_view, name="teachers"),
    path("results/", views.results_view, name="result"),
    path("results/edit", views.edit_results_view, name="edit-results"),
    path("results/view", views.view_results_view, name="view-results"),
    path("results/upload/csv/", views.upload_csv, name="csv_upload"),
    path("institute/department/", views.department_view, name="department"),
    path("institute/teacher/", views.institute_teacher_view, name="institute_teacher"),
    path("institute/staff/", views.staff_view, name="institute_staff"),
    path("institute/info/", views.institute_info_view, name="institute_info"),
    path("institute/noticeboard/", views.notice_board_view, name="notice_board"),
    path("institute/students/", views.institute_students_view, name="institute_student"),
    path("students/edit_profile/", views.edit_students_profile_view, name="edit_students_profile"),
    path("teachers/edit_profile/", views.edit_teachers_profile_view,name="edit_teachers_profile"),
    path("studnets/enrollment/", views.enrollment_view,name="enrollment"),
    path("studnets/ranklist/", views.ranklist_view,name="ranklist"),
    path("studnets/downloadpdf/", views.GeneratePdf_view.as_view(),name="download"),
    path("teachers/downloadpdf/", views.GeneratePdfTeachers_view.as_view(),name="download_teachers"),
]