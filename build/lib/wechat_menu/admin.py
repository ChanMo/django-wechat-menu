from django.utils.translation import ugettext_lazy as _
from django.contrib import admin, messages
from mptt.admin import DraggableMPTTAdmin
from django.http import HttpResponseRedirect
from django.conf.urls import url
from .models import Menu
from .api import Menu as MenuApi


class MenuAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'type', 'value')
    list_display_links = ('indented_title',)

    def get_urls(self):
        urls = super(MenuAdmin, self).get_urls()
        return [url(r'^sync/$', self.sync_menu),] + urls

    def sync_menu(self, request):
        wx = MenuApi()
        result = wx.sync_menu()
        if result['errcode'] == 0:
            messages.add_message(request, messages.SUCCESS, _('sync success'))
        else:
            messages.add_message(request, messages.ERROR, _('sync error'))
        return HttpResponseRedirect('/admin/wechat_menu/menu/')


admin.site.register(Menu, MenuAdmin)
