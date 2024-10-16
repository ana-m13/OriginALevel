from django.urls import path
from OriginALevel_app import views

urlpatterns = [
    path('', views.index_view, name="home"),
    path('contact/', views.contact_view, name='contact'),
    path('post/', views.newpost_view, name='post'),
    path('reply/', views.reply_view, name='reply'),
    path('rate_post/', views.rate_post_view, name='rate_post'),

]










# from django.urls import path
# from OriginALevel_app import views

# urlpatterns = [
#     path('', views.index_view),
#     path('contact/', views.contact_view, name='contact'),
#     path('post/', views.post_view, name='post')
#     # path('login/', views.login_view, name='login'),
#     # path('logout/', views.logout_view, name='logout'),
#     # path('signup/', views.signup_view, name='signup')

# ]

