from __future__ import unicode_literals

from picklefield.fields import PickledObjectField
from django.contrib.postgres import fields as pg_fields
from django.db.models import fields
from django.utils.translation import ugettext_lazy as _
from ...models.field import FieldDefinition, FieldDefinitionManager

class _PostgresMeta:
    defined_field_category = _('Postgres')

class ArrayFieldDefinition(FieldDefinition):
    base_field = PickledObjectField(_('base field'))
    size = fields.PositiveSmallIntegerField(_('size'), blank=True, null=True)
    
    class Meta(_PostgresMeta):
        app_label = 'postgres'
        defined_field_class = pg_fields.ArrayField
        defined_field_options = ('base_field', 'size')


class JSONFieldDefinition(FieldDefinition):
    class Meta(_PostgresMeta):
        app_label = 'postgres'
        proxy = True
        defined_field_class = pg_fields.JSONField