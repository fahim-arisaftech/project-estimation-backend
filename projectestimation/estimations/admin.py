from django.contrib import admin

# Register your models here.
from .models import DjangoProjectEstimation, PHPProjectEstimation, WordpressProjectEstimation, DOTNetProjectEstimation, SpringBootProjectEstimation, FastAPIProjectEstimation, FlaskProjectEstimation, NodeProjectEstimation, ReactProjectEstimation, VueProjectEstimation, AngularProjectEstimation, NextJSProjectEstimation, NativeAndroidProjectEstimation, NativeIOSProjectEstimation, FlutterProjectEstimation, ReactNativeProjectEstimation

@admin.register(DjangoProjectEstimation)
class DjangoAdmin(admin.ModelAdmin):
    list_display = ("feature", "estimation")

# admin.site.register(DjangoProjectEstimation)
admin.site.register(PHPProjectEstimation)
admin.site.register(WordpressProjectEstimation)
admin.site.register(DOTNetProjectEstimation)
admin.site.register(SpringBootProjectEstimation)
admin.site.register(FastAPIProjectEstimation)
admin.site.register(FlaskProjectEstimation)
admin.site.register(NodeProjectEstimation)
admin.site.register(ReactProjectEstimation)
admin.site.register(VueProjectEstimation)
admin.site.register(AngularProjectEstimation)
admin.site.register(NextJSProjectEstimation)
admin.site.register(NativeAndroidProjectEstimation)
admin.site.register(NativeIOSProjectEstimation)
admin.site.register(FlutterProjectEstimation)
admin.site.register(ReactNativeProjectEstimation)
