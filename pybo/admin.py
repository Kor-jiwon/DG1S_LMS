from django.contrib import admin
from .models import *
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from django.utils import timezone

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['num', 'name']
    list_display = ['num', 'name']

class CardAdmin(admin.ModelAdmin):
    search_fields = ['stu', 'to', 'why', 'moving_date']
    list_display = ['stu', 'to', 'moving_date']
    list_filter = ('to', ('moving_date', DateRangeFilter))

class PreCardAdmin(admin.ModelAdmin):
    search_fields = ['stu', 'time', 'to', 'why', 'moving_date']
    list_display = ['stu', 'to', 'time', 'moving_date']
    list_filter = ('to', 'time', ('moving_date', DateRangeFilter))

    @admin.action(description="Approve the request")
    def approve(self, request, queryset):
        for pcard in queryset:
            a = Card(stu=pcard.stu, to=pcard.to, why=pcard.why, moving_date=timezone.now())
            a.save()
        self.message_user(request, "이동 요청이 승인되어 이동 현황에 올라갑니다.")

    actions = [approve]



admin.site.register(Student, StudentAdmin)
admin.site.register(PreCard, PreCardAdmin)
admin.site.register(Card, CardAdmin)
admin.site.index_title = 'DG1S LMS'
admin.site.site_header = 'DG1S LMS Admin'
admin.site.site_title = 'Administration'

# Register your models here.
