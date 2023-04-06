from django.contrib import admin

# Register your models here.
from .models import DjangoProjectEstimation, PHPProjectEstimation, WordpressProjectEstimation, DOTNetProjectEstimation, SpringBootProjectEstimation, FastAPIProjectEstimation, FlaskProjectEstimation, NodeProjectEstimation, ReactProjectEstimation, VueProjectEstimation, AngularProjectEstimation, NextJSProjectEstimation, NativeAndroidProjectEstimation, NativeIOSProjectEstimation, FlutterProjectEstimation, ReactNativeProjectEstimation

@admin.register(DjangoProjectEstimation)
class DjangoAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]

@admin.register(PHPProjectEstimation)
class PHPAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]

@admin.register(WordpressProjectEstimation)
class WordpressAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]

@admin.register(DOTNetProjectEstimation)
class DOTNetAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]


@admin.register(SpringBootProjectEstimation)
class SpringBootAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]


@admin.register(FastAPIProjectEstimation)
class FastAPIAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]


@admin.register(FlaskProjectEstimation)
class FlaskAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]


@admin.register(NodeProjectEstimation)
class NodeAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]


@admin.register(ReactProjectEstimation)
class ReactAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]


@admin.register(VueProjectEstimation)
class VueAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]


@admin.register(AngularProjectEstimation)
class AngularAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]


@admin.register(NextJSProjectEstimation)
class NextJSAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]


@admin.register(NativeAndroidProjectEstimation)
class NativeAndroidAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]


@admin.register(NativeIOSProjectEstimation)
class NativeIOSdAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]

@admin.register(FlutterProjectEstimation)
class FlutterdAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]

@admin.register(ReactNativeProjectEstimation)
class ReactNativeAdmin(admin.ModelAdmin):
    list_display = ("id", "feature", "estimation")
    search_fields = ["feature"]
    ordering = ["-id"]
