from django.urls import path
from . import views

urlpatterns = [
    path('new_remind/',views.post_data),
    path('remainders/',views.get_data),

]