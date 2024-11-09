from django.urls import include, path
from rest_framework import routers

from surveys.questions import views as questions_views
from surveys.participants import views as participants_views
from surveys.responses import views as responses_views

router = routers.DefaultRouter()
router.register(r'surveys', questions_views.SurveyViewSet)
router.register(r'locations', participants_views.LocationViewSet)
router.register(r'occupations', participants_views.OccupationViewSet)
router.register(r'answers', responses_views.SurveyAnswerViewSet)
router.register(r'responses', responses_views.SurveyResponseViewSet)

urlpatterns = [
    path('brands', questions_views.BrandList.as_view()),
    path('question_types', questions_views.QuestionTypesList.as_view()),
    path('questions', questions_views.QuestionList.as_view()),
    path('', include(router.urls)),
]
