from django.conf.urls import include, url

from rest_framework import routers

from .views import HomeView
from .viewsets import BookViewSet, FavouriteViewSet

router = routers.SimpleRouter()
router.register(r'libros', BookViewSet)
router.register(r'favoritos', FavouriteViewSet)


urlpatterns = [
	url(r'^api/', include(router.urls)),

	url(r'^$', HomeView.as_view(), name="home"),
]
