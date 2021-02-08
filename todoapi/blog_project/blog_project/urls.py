from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view 
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls 

API_TITLE = "Blog API"
API_DESCRIPTION = "A Web API for creating and editing blog posts"

core_schema_view = get_schema_view(title=API_TITLE)
swagger_schema_view = get_swagger_view(title=API_TITLE) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')),
    path('schema/', core_schema_view),   #CoreAPI
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('swagger-docs/', swagger_schema_view),   #OpenAPI   
]
