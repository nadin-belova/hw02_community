from django.contrib import admin

# Из модуля models импортируем модель Post
from .models import Group, Post


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    list_editable = ('group',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
    )
    search_fields = ('title',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('title',)
    list_editable = ('slug',)
    empty_value_display = '-пусто-'


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)


# from django.contrib import admin
# from .models import Post, Group


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'text', 'pub_date', 'author')
#     search_fields = ('text',)
#     list_filter = ('pub_date',)
#     #Это свойство сработает для всех колонок:
#             где пусто — там будет эта строка
#     empty_value_display = '-пусто-'


# # При регистрации модели Post источником конфигурации для неё назначаем
# # класс PostAdmin
# admin.site.register(Post, PostAdmin)
# admin.site.register(Group)
