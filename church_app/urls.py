"""
URL configuration for churchpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login_user',views.login_user,name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('about',views.about,name='about'),
    path('Event_Details/<int:id>',views.Event_Details,name='Event_Details'),
    path('admin_add_events',views.admin_add_events,name='admin_add_events'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('bishop_message',views.bishop_message,name='bishop_message'),
    path('vicar_message',views.vicar_message,name='vicar_message'),
    path('image_shadow',views.image_shadow,name='image_shadow'),
    path('admin_event_view',views.admin_event_view,name='admin_event_view'),
    path('admin_delete_events/<int:id>', views.admin_delete_events, name='admin_delete_events'),
    path('admin_update_events/<int:id>',views.admin_update_events,name='admin_update_events'),
    path('january',views.january,name='january'),
    path('event_registration',views.event_registration,name='event_registration'),

    path('admin_add_ministries',views.admin_add_ministries,name='admin_add_ministries'),
    path('admin_ministries_view',views.admin_ministries_view,name='admin_ministries_view'),
    path('admin_update_ministries/<int:id>',views.admin_update_ministries,name='admin_update_ministries'),
    path('admin_delete_ministries/<int:id>',views.admin_delete_ministries,name='admin_delete_ministries'),

    path('mass_times',views.mass_times,name='mass_times'),
    path('admin_add_mass_times',views.admin_add_mass_times,name='admin_add_mass_times'),
    path('admin_daily_mass_view',views.admin_daily_mass_view,name='admin_daily_mass_view'),
    path('admin_update_mass_times/<int:id>',views.admin_update_mass_times,name='admin_update_mass_times'),
    path('admin_delete_mass_times/<int:id>',views.admin_delete_mass_times,name='admin_delete_mass_times'),

    path('admin_add_special_masses',views.admin_add_special_masses,name='admin_add_special_masses'),
    path('admin_special_mass_view',views.admin_special_mass_view,name='admin_special_mass_view'),
    path('admin_update_special_mass/<int:id>',views.admin_update_special_mass,name='admin_update_special_mass'),
    path('admin_delete_special_mass/<int:id>',views.admin_delete_special_mass,name='admin_delete_special_mass'),

    path('obituary',views.obituary,name='obituary'),
    path('admin_add_obituary',views.admin_add_obituary,name='admin_add_obituary'),
    path('admin_update_obituary/<int:id>',views.admin_update_obituary,name='admin_update_obituary'),
    path('admin_delete_obituary/<int:id>',views.admin_delete_obituary,name='admin_delete_obituary'),
    path('admin_obituary_view',views.admin_obituary_view,name='admin_obituary_view'),

    path('gallery',views.gallery,name='gallery'),
    path('admin_add_gallery',views.admin_add_gallery,name='admin_add_gallery'),
    path('admin_gallery_view',views.admin_gallery_view,name='admin_gallery_view'),
    path('admin_update_gallery/<int:id>',views.admin_update_gallery,name='admin_update_gallery'),
    path('admin_delete_gallery/<int:id>',views.admin_delete_gallery,name='admin_delete_gallery'),
    path('blog_single',views.blog_single,name='blog_single'),
    path('admin_add_blog',views.admin_add_blog,name='admin_add_blog'),
    path('admin_blog_view',views.admin_blog_view,name='admin_blog_view'),
    path('admin_update_blog/<int:id>',views.admin_update_blog,name='admin_update_blog'),
    path('admin_delete_blog/<int:id>',views.admin_delete_blog,name='admin_delete_blog'),

]
