#### source : 
  
        https://www.django-rest-framework.org/tutorial/quickstart/


#### creating new folder

        mithun@linux:~$ cd Documents/djrest/
        mithun@linux:~/Documents/djrest$ mkdir tutorial
        mithun@linux:~/Documents/djrest$ cd tutorial


#### creating virtual env

        mithun@linux:~/Documents/djrest/tutorial$ virtualenv env
        mithun@linux:~/Documents/djrest/tutorial$ source env/bin/activate

#### install django library, django rest needs django library

        (env) mithun@linux:~/Documents/djrest/tutorial$ pip3 install django

#### install django rest

        (env) mithun@linux:~/Documents/djrest/tutorial$ pip3 install djangorestframeworkCollecting djangorestframework
        
#### creating project , *note : include dot at the end 

        (env) mithun@linux:~/Documents/djrest/tutorial$ django-admin startproject mytutorial .
        (env) mithun@linux:~/Documents/djrest/tutorial$ cd mytutorial/

#### creating app :

        (env) mithun@linux:~/Documents/djrest/tutorial/mytutorial$ django-admin startapp quickstart

#### migration : done where manage.py exists

        (env) mithun@linux:~/Documents/djrest/tutorial/mytutorial$ cd -
        (env) mithun@linux:~/Documents/djrest/tutorial$ python3 manage.py migrate


#### create admin user

        (env) mithun@linux:~/Documents/djrest/tutorial$ python3 manage.py createsuperuser --email admin@example.com --username admin
        Password: 
        Password (again): 
        Superuser created successfully.
        
        * passwrod : lenovo123

#### include rest framework in settings.py

        INSTALLED_APPS = (
            ...
            'rest_framework',
        )

#### pagination : optional , add in settings.py

        REST_FRAMEWORK = {
            'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
            'PAGE_SIZE': 10
        }

#### run app

        (env) mithun@linux:~/Documents/djrest/tutorial$ python3 manage.py runserver




#### add code in following files

#### mytutorial/quickstart/serializers.py : converting python datatype to json/xml and viceversa
        
        
            from django.contrib.auth.models import User, Group
            from rest_framework import serializers


            class UserSerializer(serializers.HyperlinkedModelSerializer):
                class Meta:
                    model = User
                    fields = ('url', 'username', 'email', 'groups')


            class GroupSerializer(serializers.HyperlinkedModelSerializer):
                class Meta:
                    model = Group
                    fields = ('url', 'name')
        
        
        
#### mytutorial/quickstart/views.py

            from django.contrib.auth.models import User, Group
            from rest_framework import viewsets
            from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


            class UserViewSet(viewsets.ModelViewSet):
                """
                API endpoint that allows users to be viewed or edited.
                """
                queryset = User.objects.all().order_by('-date_joined')
                serializer_class = UserSerializer


            class GroupViewSet(viewsets.ModelViewSet):
                """
                API endpoint that allows groups to be viewed or edited.
                """
                queryset = Group.objects.all()
                serializer_class = GroupSerializer

#### mytutorial/urls.py

          from django.conf.urls import url, include
          from rest_framework import routers
          from tutorial.quickstart import views

          router = routers.DefaultRouter()
          router.register(r'users', views.UserViewSet)
          router.register(r'groups', views.GroupViewSet)

          # Wire up our API using automatic URL routing.
          # Additionally, we include login URLs for the browsable API.
          urlpatterns = [
              url(r'^', include(router.urls)),
              url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
          ]
