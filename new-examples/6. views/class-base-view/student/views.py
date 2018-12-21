from django.http import HttpResponse
from django.views import View

class MyView(View):
    greeting = "Good Day"
    def get(self, request):
    # <view logic>
        return HttpResponse(self.greeting)