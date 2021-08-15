from django.urls import path

from assessment import views

urlpatterns = [
    path('tags/', views.TagsAPIView.as_view()),
    path('assessment/list', views.AssessmentDetailListView.as_view()),
    path('assessment/create/', views.AssessmentCreateView.as_view()),
    path('assessment/view/<int:pk>/', views.AssessmentDetailView.as_view())
]
