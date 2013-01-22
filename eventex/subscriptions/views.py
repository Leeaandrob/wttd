# Create your views here.

# coding: utf-8
from django.views.generic.simple import direct_to_template
from eventex.subscriptions.forms import SubscriptionForm
from django.http import HttpResponseRedirect, HttpResponse
from eventex.subscriptions.models import Subscription
from django.shortcuts import get_object_or_404

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
	   return new(request)

def success(request, id):
    subscription = get_object_or_404(Subscription, pk=id)
    return direct_to_template(request, 
        'subscriptions/subscription_detail.html',
        {'subscription': subscription})

def new(request):
    return direct_to_template(request, 
        'subscriptions/subscription_form.html',
        {'form': SubscriptionForm()})

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
            return direct_to_template(request, 
                'subscriptions/subscription_form.html',
                {'form': form})
    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' % obj.pk)