from django.contrib import admin
from blog.models import Post
# Register your models here.
admin.site.register(Post)



# admin interface will directly interact with blog model(Post)/blog_post table
#open localhost:8000/admin : 
#you will find blog project title under this, you will find a link to interact with blog_post table
