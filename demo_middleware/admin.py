from django.contrib import admin
from .models import newstats


@admin.register(newstats)
class NewStatsAdmin(admin.ModelAdmin):
    pass
    # list_display = ('win', 'mac', 'iph', 'android', 'oth')