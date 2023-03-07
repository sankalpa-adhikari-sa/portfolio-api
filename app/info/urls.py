from django.urls import(
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from info import views

router= DefaultRouter()
router.register('education', views.EducationViewSet)
router.register('experience', views.ExperienceViewSet)
router.register('skill', views.SkillViewSet)
router.register('certificate', views.CertificateViewSet)
router.register('sociallink', views.SocialLinkViewSet)
router.register('message', views.MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]