from django.contrib import admin
from django.urls import path, include

# Static settings
from django.conf import settings
from django.conf.urls.static import static

# Views
from main_app.views import home_page
from contact_app.views import contact_page, me_page
from more_app.views import communal_page, gaz_page

urlpatterns = [
    path('admin/', admin.site.urls),

    # Views
    path('', home_page, name='home_page'),

    path('courses/', include('course_app.urls')),

    path('contact/', contact_page, name='contact_page'),
    path('me/', me_page, name='me_page'),

    # More
    path('oqituvchi/', include('more_app.urls')),

    path('actions/communal/', communal_page, name='communal_page'),
    path('actions/gaz/', gaz_page, name='gaz_page'),

    # Quiz
    path('quiz/', include('quiz_app.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)