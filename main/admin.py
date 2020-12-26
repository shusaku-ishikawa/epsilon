
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from main.models import *

class MyUserChangeForm(UserChangeForm):
  class Meta:
    model = User
    fields = '__all__'
class MyUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('email', )

class MyUserAdmin(UserAdmin):
  fieldsets = (
    (None, {'fields': ('email', 'company_name', 'company_name_furigana', 'password')}),
    (_('Personal info'), {'fields': ('short_description', 'description')}),
    (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    (_('Important dates'), {'fields': ('last_login',)}),
  )
  add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'company_name', 'company_name_furigana', 'password1', 'password2', 'is_active', 'is_superuser', 'is_staff'),
    }),
  )
  form = MyUserChangeForm
  add_form = MyUserCreationForm
  ordering = ('email',)
  list_display = ('email', 'company_name', 'company_name_furigana', 'thumbnail', 'is_staff', 'is_active', 'is_superuser')

admin.site.site_title = '管理' 
admin.site.site_header = 'Epsilon Admin ' 
admin.site.index_title = 'Menu'
admin.site.register(User, MyUserAdmin)