from django import urls
from . import views

app_name = 'order'

urlpatterns = [
    urls.path('create/', views.order_create, name='order_create'),
]

