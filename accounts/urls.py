from django.urls import path
from . import views
from store.views import product_list


urlpatterns = [
    path("", views.register, name="register"),
    # path("login/", views.login_view, name="login"),
    # path("logout/", views.logout_view, name="logout"),
    path("student/", views.student_home, name="student_home"),
    path("teacher/", views.teacher_home, name="teacher_home"),
    # path("store/", product_list, name="product_list"),
]
