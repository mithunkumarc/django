# pages/urls.py
from django.urls import path

from .views import homePageView,subPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('sub', subPageView, name='subPage')
]
#
# The last part, name='subPage',
# is the name of the URL that will be used to identify the view.
# This can be the same as the name of the view but
# it can also be something completely different.
# (
# it is important to name each URL in the app.
# We should also try to keep the names of URLs unique and easy to remember.
# )
