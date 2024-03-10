
from django.contrib import admin
from django.urls import path
from techtest.sampleAPI.views import ClientView, ClientListView



urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("client/", ClientListView.as_view(), name = "client-list" ),

    path("client/<int:client_id>", ClientView.as_view(), name= "client" ),

]
