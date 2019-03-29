from django.contrib import admin
# Register your models here.

class PostAdmin(admin.ModelAdmin):

	list_display = ['id','title', 'updated']
	list_display_links = [ 'title', 'updated']
	list_filter = ['title', 'updated']
	search_fields = ['title', 'content']
	date_hierarchy = 'updated'
	ordering = ('-updated',)

admin.site.register(Post, PostAdmin)