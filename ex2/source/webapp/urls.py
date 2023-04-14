from django.urls import path

from webapp.views.example import subtract, add, get_token_view, multiply, divide, index


urlpatterns =[
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
    path('token/', get_token_view, name='token'),
    path('', index, name='index'),
]
