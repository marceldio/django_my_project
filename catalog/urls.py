from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import index, contact
app_name = NewappConfig.name

urlpatterns = [
    path('', index, name='home'),

    path('contacts', contact, name='contacts')
]
