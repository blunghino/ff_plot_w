from django.contrib import admin

from playerdata.models import RbPlayer, RbSeason, RbGame

admin.site.register(RbPlayer)
admin.site.register(RbSeason)
admin.site.register(RbGame)