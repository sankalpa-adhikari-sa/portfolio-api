from django.urls import(
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from projects import views

router= DefaultRouter()
router.register('projects', views.ProjectsViewSet)
router.register('tags', views.TagsViewSet)
app_name= 'projects'

urlpatterns = [
    path('', include(router.urls)),
]