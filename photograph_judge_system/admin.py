from django.contrib import admin

from .models import Judge
from .models import Entry
from .models import Photo


admin.site.register(Judge)
admin.site.register(Entry)
admin.site.register(Photo)
