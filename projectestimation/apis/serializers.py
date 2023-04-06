from rest_framework import serializers
from estimations import models

#  Django Serializers
class DjangoEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.DjangoProjectEstimation


#  PHP Serializers
class PHPEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.PHPProjectEstimation


#  Wordpress Serializers
class WordpressEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.WordpressProjectEstimation


# DOTNET Serializers
class DotNetEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.DOTNetProjectEstimation


#  Spring Boot Serializers
class SpringBootEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.SpringBootProjectEstimation


# FastAPI Serializers
class FastAPIEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.FastAPIProjectEstimation


# Flask Serializers
class FlaskEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.FlaskProjectEstimation


# Node Serializers
class NodeEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.NodeProjectEstimation


# React Serializers
class ReactEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.ReactProjectEstimation


# Vue Serializers
class VueEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.VueProjectEstimation


# Angular Serializers
class AngularEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.AngularProjectEstimation


# NextJS Serializers
class NextJSEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.NextJSProjectEstimation


# Native Android Serializers
class NativeAndroidEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.NativeAndroidProjectEstimation


# Native iOS Serializers
class NativeIOSEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.NativeIOSProjectEstimation


# Flutter Serializers
class FlutterEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.FlutterProjectEstimation


# React Native Serializers
class ReactNativeEstimationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feature',
            'estimation'
        )
        model = models.ReactNativeProjectEstimation


