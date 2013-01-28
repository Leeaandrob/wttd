# coding: utf-8

from django.contrib import admin
from eventex.subscriptions.models import Subscription
from django.utils.datetime_safe import datetime
from django.utils.translation import ungettext, gettext as _

class SubscriptionAdmin(admin.ModelAdmin):
        list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribed_today', 'paid')
        date_hierarchy = 'created_at'
        search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
        list_filter = ['created_at']
        actions = ['mark_as_paid']

        def subscribed_today(self, obj):
            return obj.created_at.date() == datetime.today().date()

        def mark_as_paid(self, request, queryset):
            count = queryset.update(paid = True)
            msg = ungettext(
                u'%d Incrição marcada como Paga!',
                u'%d Inscrições marcadas como Paga!',
                count
            )
            self.message_user(request, msg % count)

        mark_as_paid.short_description = _('Marcar como Pago')

        subscribed_today.boolean = True
        subscribed_today.short_description = _(u'Inscrito Hoje?')

admin.site.register(Subscription, SubscriptionAdmin)