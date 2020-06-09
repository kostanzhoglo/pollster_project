from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# Change header in Admin pages. Default is "Django Administration"
admin.site.site_header = "Pollster Admin"
# This is the browser tab text
admin.site.site_title = "Pollster Admin Area"
# Default is "Site administration"
admin.site.index_title = "Welcome to the Pollster admin area"

# in admin, this [TABULAR INLINE] lets admin-user see Choice options underneath Question on Question page
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)