from django.contrib import admin
from django.urls import path, include
from codes.views import lists
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lists, name="home"),
    path('accounts/', include('accounts.urls')),
    path('code/', include('codes.urls')),
    # path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'adv104.views.custom_page_not_found_view'
handler500 = 'adv104.views.custom_error_view'
handler403 = 'adv104.views.custom_permission_denied_view'
handler400 = 'adv104.views.custom_bad_request_view'


