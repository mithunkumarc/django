from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    print('type', type(request.GET.get('id')))
    if int(request.GET.get('id')) == 100:
        return HttpResponse("student id : 100, name : vinay")
    else:
        # uncomment below line to run with exception
        # raise ObjectDoesNotExist()
        # below to handles exception

        # comment for first case and uncomment for second case
        try:
            raise ObjectDoesNotExist()
        except ObjectDoesNotExist:
            return HttpResponse('student id ' + request.GET.get('id') + " doesn't exist")