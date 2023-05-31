
from django.contrib import admin
from django.urls import path,include
from library_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
     path("accounts/", include("django.contrib.auth.urls")),
    path('index/', index),
    path('form/', form),
    path('display/', display),
    path('display_update/', display_update),
    path('update/<int:j>/', update),
    path('delete/<int:j>/', delete),
    path('display_delete/', display_delete),
    path('signin/', signin),
    path('signup/', signup),
    path('logout/', logout),
    path('display_stu/', display_students),
    path('delete_stu/', delete_student),
    path('delete_s/<int:j>/', delete_s),
    path('issue_book/<int:s_id>/<str:b_name>/<str:s_name>/', issue_b),
    path('display_iss_b/<int:s_id>', display_iss_b),
    path('dispaly_s_iss_b/<int:v>', dispaly_s_iss_b),
    path('accept_req/<int:s_id>/<str:s_name>/<str:b_name>/', accpeted_data),
    path('display_acc_req/', dis_accpeted_data),
    path('del_accpeted_data/<str:b_name>/<int:s_id>/', del_accpeted_data),
]
