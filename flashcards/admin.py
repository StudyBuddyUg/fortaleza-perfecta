from django.contrib import admin
from .models import LowerGrade, UpperGrade, ThemeCard, ThemePack, TopicCard, TopicPack

# Register your models here.
class ThemeCardInLine(admin.TabularInline):
    model = ThemeCard
    extra = 10


class ThemePackAdmin(admin.ModelAdmin):
    inlines = [ThemeCardInLine]
admin.site.register(ThemePack, ThemePackAdmin)


class LowerGradeAdmin(admin.ModelAdmin):
    list_display = ('lower_grade_name',)
admin.site.register(LowerGrade, LowerGradeAdmin)


class TopicCardInLine(admin.TabularInline):
    model = TopicCard
    extra = 10


class TopicPackAdmin(admin.ModelAdmin):
    inlines = [TopicCardInLine]
admin.site.register(TopicPack, TopicPackAdmin)


class UpperGradeAdmin(admin.ModelAdmin):
    list_display = ('upper_grade_name',)
admin.site.register(UpperGrade, UpperGradeAdmin)
