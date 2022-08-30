from django.urls import path
from listings import views

urlpatterns = [
    path('listings', views.ListApiView.as_view()),
    path('listings/<int:id>', views.ListApiView.as_view()),
    path('listings/<int:id>', views.update_listing, name='update_listing'),
    path('listings/<int:id>/delete', views.delete_listing, name='delete_listing'),
]