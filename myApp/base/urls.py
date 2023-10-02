from django.urls import path
from .views import PaginaPrincipalaView
from .views import CustomDetailView1
from .views import CustomCreateView1
from .views import CustomUpdateView1
from .views import CustomDeleteView1
from .views import CustomLoginView
from .views import CustomRegisterView
from .views import PaginaWorkoutView
from .views import CustomCreateView2
from .views import CustomUpdateView2
from .views import CustomDeleteView2
from .views import PaginaUserView
from .views import CustomWorkoutView
from .views import CustomAttendanceListView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    # 1) PAGINA PRINCIPALA:
    path('', PaginaPrincipalaView.as_view(), name='paginaPrincipala'),

    # 2) LOGIN:
    path('login/', CustomLoginView.as_view(), name='login'),

    # 3) LOGOUT:
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # 4) REGISTER:
    path('register/', CustomRegisterView.as_view(), name="register"),

    # 5) AFISARE(DETAIL):
    path('afisare/<int:pk>/', CustomDetailView1.as_view(), name='afisare'),

    # 6) CREARE:
    path('creare/', CustomCreateView1.as_view(), name='creare'),

    # 7) UPDATE:
    path('update/<int:pk>', CustomUpdateView1.as_view(), name='update'),

    # 8) DELETE:
    path('delete/<int:pk>', CustomDeleteView1.as_view(), name='delete'),

    # 9) PAGINA PRINCIPALA WORKOUT:
    path('workoutPage/', PaginaWorkoutView.as_view(), name='workoutPage'),

    # 10) CREARE WORKOUT:
    path('creareWorkout/', CustomCreateView2.as_view(), name='creareWorkout'),

    # 11) UPDATE WORKOUT:
    path('updateWorkout/<int:pk>', CustomUpdateView2.as_view(), name='updateWorkout'),

    # 12) DELETE WORKOUT:
    path('deleteWorkout/<int:pk>', CustomDeleteView2.as_view(), name='deleteWorkout'),

    # 13) PAGINA PRINCIPALA USER:
    path('user/', PaginaUserView.as_view(), name='paginaPrincipalaUser'),

    # 14) PAGINA VIEW WORKOUT USER:
    path('viewWorkout/<int:pk>', CustomWorkoutView.as_view(), name='viewWorkout'),

    # 15) BUTONUL DE RESERVE:
    path(r'^reserveSpot/(?P<block_id>\d+)/$', CustomWorkoutView.reserveSpot, name='reserveSpot'),

    # 16) BUTONUL DE VIEW ATTENDANCE LIST:
    path('viewClassAttendanceList/', CustomAttendanceListView.as_view(), name='viewClassAttendanceList'),

    # 17) BUTONUL DE CANCEL RESERVATION:
    path(r'^cancelReservation/(?P<block_id>\d+)/$', CustomWorkoutView.cancelReservation, name='cancelReservation'),

]