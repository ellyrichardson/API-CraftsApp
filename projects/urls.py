from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('profile/', views.ListProfilePosts.as_view(), name="list_profile_posts"),
    path('home/', views.ListHomePosts.as_view(), name="list_home_posts"),
    path('<int:pk>/', views.DetailPosts.as_view(), name="detail_posts"),
    #path('rest_auth/', include('rest_auth.urls')),
    #path('auth/login/', views.LoginView.as_view(), name="auth_login"),
    path('login/', obtain_jwt_token),
    path('register/', views.RegisterUserView.as_view(), name="register_user"),
    path('userinfo/', views.GetUserInfo.as_view(), name="get_user_info"),
    # path('search/<username>/', views.SearchBoxResults.as_view(),
    #     name="get_search_results"),
    path('search/', views.SearchBoxResults.as_view(), name="get_search_results"),
]
