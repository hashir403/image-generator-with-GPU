from django.contrib import admin
from .models import ImagePrompt, Registration, Feedback, Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message') 

@admin.register(Feedback)
class feebackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'feedback') 

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'password', 'email') 

@admin.register(ImagePrompt)
class ImagePromptAdmin(admin.ModelAdmin):
    list_display = ('id', 'prompt_preview', 'prompt_image', 'created_at')
    readonly_fields = ('created_at',)
    search_fields = ('prompt',)
    ordering = ('-created_at',)

    def prompt_preview(self, obj):
        return obj.prompt[:50] + ('...' if len(obj.prompt) > 50 else '')
    prompt_preview.short_description = 'Prompt'
