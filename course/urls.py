from django.urls import path, re_path
from course.views import *


urlpatterns = [
    # path('show_course/<str:course_name>', show_course),
    # path('show_course/<int:year>/<slug:slug>', show_course),
    re_path(r'show_course/(?P<year>[0-9]{4,6})', show_course),
    path('add_course/', AddCourse.as_view()),
    path('number_of_courses/', NumberOfCourses.as_view()),
    path('sum_course_duration/', SumCourseDuration.as_view()),
    path('show_course_category/', ShowCourseCategory.as_view()),
    path('comments/<int:pk>', CommentRelatedToCourse.as_view()),
    path('comments/<int:pk>/vote', VoteCreate.as_view()),
    path('list/<int:pk>', course_list, name='course-list')
]
