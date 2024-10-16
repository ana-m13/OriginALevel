from django.contrib import admin
from .models import OriginALevel_ProfileModel
from .models import OriginALevel_ReplyModel
from .models import OriginALevel_PostModel
from .models import OriginALevel_SettingsModel
from .models import OriginALevel_RatingModel

class OriginALevel_PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified_at', 'published', 'post_type', )
    readonly_fields= ['created_at', 'modified_at',]


admin.site.register(OriginALevel_PostModel, OriginALevel_PostModelAdmin)
admin.site.register(OriginALevel_ProfileModel)
admin.site.register(OriginALevel_ReplyModel)
admin.site.register(OriginALevel_SettingsModel)
admin.site.register(OriginALevel_RatingModel)












# from django.contrib import admin
# from .models import OriginALevel_ProfileModel
# from .models import OriginALevel_PostModel
# from .models import OriginALevel_ReplyModel
# from .models import OriginALevel_SettingsModel

# #allows admin to see the database tables in a more organised manner
# class OriginALevel_PostModelAdmin(admin.ModelAdmin):
#     list_display = ('title', 'modified_at', 'published', 'post_type', )
#     readonly_fields= ['created_at', 'modified_at',]


# admin.site.register(OriginALevel_PostModel, OriginALevel_PostModelAdmin)
# admin.site.register(OriginALevel_ProfileModel)
# admin.site.register(OriginALevel_ReplyModel)
# admin.site.register(OriginALevel_SettingsModel)

