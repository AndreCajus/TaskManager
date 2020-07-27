from django.contrib import admin
from django.urls import path, include

# swagger 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Accounts and Tasks API",
      default_version='v1',
      description="At this page it is possible to use my API. There are CRUD operations for accounts and tasks.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),                 # admin enabled
    path('api/tasks/', include('taskmanager.urls')), # task creation API
    path('api/accounts/', include('account.urls')),  # account creation API
]