from django.contrib import admin

from .models import Candidate, Poll
from .models import Candidate
# Register your models here.


admin.site.register(Candidate)
admin.site.register(Poll)
