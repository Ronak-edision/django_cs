from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('html/blog.html', views.blog, name='blog'),
    path('html/aboutus.html', views.aboutus, name='aboutus'),
    path('html/product_camera.html', views.product_camera, name='product_camera'),
    path('html/research.html', views.research, name='research'),
    path('html/product_cart.html', views.product_cart, name='product_cart'),
    path('html/launch.html', views.launch, name='launch'),
    path('html/product_camera', views.product_camera, name='product_camera'),  # Add this pattern
    path('html/product_lens', views.product_lens, name='product_lens'),  # Add this pattern
    path('html/product_equipment', views.product_equipment, name='product_equipment'),  # Add this pattern
    path('html/product_accessories', views.product_accessories, name='product_accessories'),  # Add this pattern
    path('html/cv_sushant', views.cv_sushant, name='cv_sushant'),  # Add this pattern
    path('html/cv_nischal', views.cv_nischal, name='cv_nischal'),  # Add this pattern
    path('html/cv_ronak', views.cv_ronak, name='cv_ronak'),  # Add this pattern
    path('html/cv_aakarshan', views.cv_aakarshan, name='cv_aakarshan'),  # Add this pattern
    path('html/cv_tsewang', views.cv_tsewang, name='cv_tsewang'),  # Add this pattern
    path('html/form2', views.form2, name='form2'),  # Add this pattern for the 'form2' view
    path('html/form1', views.form1, name='form1')  # Add this pattern for the 'form2' view


]
