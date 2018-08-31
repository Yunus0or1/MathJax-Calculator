
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
import calculator.views

urlpatterns = [

	path('', calculator.views.home, name ="home"),
	
	path('calculator_main_page', calculator.views.calculator_main_page, name ="calculator_main_page"),
	path('calculator1', calculator.views.calculator1, name ="calculator1"),
	path('calculator2', calculator.views.calculator2, name ="calculator2"),
	
    path('admin/', admin.site.urls),
]
