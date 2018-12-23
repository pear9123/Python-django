from django.contrib import admin
from hello_app.models import Question, Choice

# Register your models here.
# admin 페이지에 어플리케이션을 사용할수있도록 등록
admin.site.register(Question)
admin.site.register(Choice)
