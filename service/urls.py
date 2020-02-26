from rest_framework.routers import DefaultRouter

from service.views import FileMetadataViewSet

router = DefaultRouter()
router.register(
    prefix=r"metadata",
    viewset=FileMetadataViewSet,
)

urlpatterns = router.urls
