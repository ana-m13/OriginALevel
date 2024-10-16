from django.urls import path
from OriginALevel_app import views
from .views import (
    login_view,
    logout_view,
    register_view,
)

urlpatterns = [
    path('', views.index_view),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    # path('forgot_password/', views.register_view, name='forgot_password')

]












# #  urls.py is where the mapping between URLs and views is defined.
# from django.urls import path
# from OriginALevel_app import views
# from .views import (
#     login_view,
#     logout_view,
#     register_view,
# )

# urlpatterns = [
#     path('', views.index_view),
#     path('login/',login_view, name='login'),
#     path('logout/',logout_view, name='logout'),
#     path('register/',register_view, name='register')

# ]

