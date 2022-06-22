from django.urls import path

from recruitings.views import RecruitingView, RecruitingDetailView, ApplicationView

urlpatterns = [
    path('', RecruitingView.as_view()),
    path('/<int:recruiting_id>', RecruitingDetailView.as_view()),
    path('/application>', ApplicationView.as_view()),
]
