from django.contrib import admin
from profiles_api import models

# Register UserProfile models.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
