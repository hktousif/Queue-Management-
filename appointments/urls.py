from rest_framework import routers

from appointments.views import AppointmentView

router = routers.DefaultRouter()
router.register('', AppointmentView)
urlpatterns = router.urls
