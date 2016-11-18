from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

@python_2_unicode_compatible
class Menu(MPTTModel):
    TYPE_CHOICES = (
        ('view', _('view menu')),
        ('click', _('click menu')),
    )
    name = models.CharField(_('name'), max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, db_index=True,\
                            related_name='children', verbose_name=_('parent'))
    type = models.CharField(_('type'), max_length=100, choices=TYPE_CHOICES,\
                            blank=True, null=True)
    value = models.CharField(_('value'), max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta(object):
        verbose_name = _('wechat menu')
        verbose_name_plural = _('wechat menu')
