from django.contrib import admin
from commonpage.models import UserProfile,PositionTable

#To activate the selected user
def make_user_active(self, request, queryset):
    rows_updated = queryset.update(useractive=True)
    if rows_updated == 1:
            message_bit = "1 user was"
    else:
        message_bit = "%s users were" % rows_updated
    self.message_user(request, "%s successfully activated." % message_bit)
make_user_active.short_description = "Activate the selected user"

#To deactivate the selected user
def make_user_deactive(self, request, queryset):
    rows_updated = queryset.update(useractive=False)
    if rows_updated == 1:
            message_bit = "1 user was"
    else:
        message_bit = "%s users were" % rows_updated
    self.message_user(request, "%s successfully deactivated." % message_bit)
make_user_deactive.short_description = "deactivate the selected user"

#register the above models
class user_action(admin.ModelAdmin):
    list_display = ['user', 'useractive','position','team_name']
    ordering = ['id']
    list_filter = ('useractive','position','team_name')
    list_editable = ['position','team_name']
    actions = [make_user_active,make_user_deactive]

# Register your models here.
admin.site.register(UserProfile,user_action)
admin.site.register(PositionTable)
