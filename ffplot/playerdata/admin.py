from django.contrib import admin

from playerdata.models import RbPlayer, RbSeason, RbGame

class PlayerAdmin(admin.ModelAdmin):
# 	prepopulated_fields = {'urlslug': ('position', 'first_name', 'last_name')}
	pass
	
admin.site.register(RbPlayer, PlayerAdmin)
admin.site.register(RbSeason)
admin.site.register(RbGame)