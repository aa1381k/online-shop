from django.urls import path
from .views import articleslist, articledetailview

urlpatterns =[
    path('',articleslist.as_view(),name='articles_list'),
    path('cat/<str:category>',articleslist.as_view(),name='cat_articles_list'),
    path('<pk>',articledetailview.as_view(),name='articles_detail'),
]