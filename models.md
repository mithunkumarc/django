#### models : 

      A model is the single, definitive source of data about your data. 
      It contains the essential fields and behaviors of the data you’re storing. 
      Generally, each model maps to a single database table.

      1.Each model is a Python class that subclasses django.db.models.Model.
      2.Each attribute of the model represents a database field.
      3.With all of this, Django gives you an automatically-generated database-access API; see Making queries.




#### example : model defines a Person, which has a first_name and last_name:

        from django.db import models

        class Person(models.Model):
            first_name = models.CharField(max_length=30)
            last_name = models.CharField(max_length=30)

        first_name and last_name are fields of the model. 
        Each field is specified as a class attribute, and each attribute maps to a database column.

        The above Person model would create a database table like this:

        CREATE TABLE myapp_person (
            "id" serial NOT NULL PRIMARY KEY,
            "first_name" varchar(30) NOT NULL,
            "last_name" varchar(30) NOT NULL
        );



#### table name

        The name of the table, myapp_person, is automatically derived from some model metadata but can be overridden. 

          use class meta : 
            db_table = "table name"


#### primary key

          An id field is added automatically, but this behavior can be overridden. See Automatic primary key fields.


#### using models : include app in settngs.py file

          Once you have defined your models, you need to tell Django you’re going to use those models. 
          Do this by editing your settings file and changing the INSTALLED_APPS setting to add the name of the module 
          that contains your models.py.


            INSTALLED_APPS = [
                #...
                'myapp',
                #...
            ]

            # myapp : app name where model has been defined


#### Fields ; 

            the list of database fields it defines. 
            Fields are specified by class attributes. 
            Be careful not to choose field names that conflict with the models API like clean, save, or delete.


            example : 

                from django.db import models

                class Musician(models.Model):
                    first_name = models.CharField(max_length=50)
                    last_name = models.CharField(max_length=50)
                    instrument = models.CharField(max_length=100)

                class Album(models.Model):
                    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)	# reference from musician table
                    name = models.CharField(max_length=100)
                    release_date = models.DateField()
                    num_stars = models.IntegerField()


#### Field type :

            The column type, which tells the database what kind of data to store (e.g. INTEGER, VARCHAR, TEXT).

            eg : 

            DateField
            charField
            IntegerField


to be completed : 
source : 

## https://docs.djangoproject.com/en/2.2/topics/db/models/
