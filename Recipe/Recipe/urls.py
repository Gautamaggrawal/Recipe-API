from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Recipe API')


urlpatterns = [
	path('', schema_view),
    path('api/', include("api.urls")),
]