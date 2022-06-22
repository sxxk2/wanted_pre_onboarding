from django.urls import path

from recruitings.views import RecruitingView

urlpatterns = [
    path('', RecruitingView.as_view()),
]
