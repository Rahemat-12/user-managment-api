from django.urls import path
from .views import CreateUser, RetrieveAllUser, RetrieveUser, UpdateUser, DeleteUser
urlpatterns = [
    path('users/', RetrieveAllUser, name='RetrieveAllUser'),
    path('users/create/', CreateUser, name='CreateUser'),
    path('users/<int:user_id>/', RetrieveUser, name='RetrieveUser'),
    path('users/<int:user_id>/update/', UpdateUser, name='UpdateUser'),
    path('users/<int:user_id>/delete/', DeleteUser, name='DeleteUser'),

]