from rest_framework import generics

from estimations import models
from .serializers import DjangoEstimationSerializers, PHPEstimationSerializers, WordpressEstimationSerializers, DotNetEstimationSerializers, SpringBootEstimationSerializers, FastAPIEstimationSerializers, FlaskEstimationSerializers, NodeEstimationSerializers, ReactEstimationSerializers, VueEstimationSerializers, AngularEstimationSerializers, NextJSEstimationSerializers, NativeAndroidEstimationSerializers, NativeIOSEstimationSerializers, FlutterEstimationSerializers, ReactNativeEstimationSerializers


#  Django
class DjangoList(generics.ListCreateAPIView):
    queryset = models.DjangoProjectEstimation.objects.all()
    serializer_class = DjangoEstimationSerializers


class DjangoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DjangoProjectEstimation.objects.all()
    serializer_class = DjangoEstimationSerializers


#  PHP
class PHPList(generics.ListCreateAPIView):
    queryset = models.PHPProjectEstimation.objects.all()
    serializer_class = PHPEstimationSerializers


class PHPDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PHPProjectEstimation.objects.all()
    serializer_class = PHPEstimationSerializers


#  Wordpress
class WordpressList(generics.ListCreateAPIView):
    queryset = models.WordpressProjectEstimation.objects.all()
    serializer_class = WordpressEstimationSerializers


class WordpressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.WordpressProjectEstimation.objects.all()
    serializer_class = WordpressEstimationSerializers



#  DOT NET
class DotNetList(generics.ListCreateAPIView):
    queryset = models.DOTNetProjectEstimation.objects.all()
    serializer_class = DotNetEstimationSerializers


class DotNetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DOTNetProjectEstimation.objects.all()
    serializer_class = DotNetEstimationSerializers



#  Spring Boot
class SpringBootList(generics.ListCreateAPIView):
    queryset = models.SpringBootProjectEstimation.objects.all()
    serializer_class = SpringBootEstimationSerializers


class SpringBootDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SpringBootProjectEstimation.objects.all()
    serializer_class = SpringBootEstimationSerializers



#  FastAPI
class FastAPIList(generics.ListCreateAPIView):
    queryset = models.FastAPIProjectEstimation.objects.all()
    serializer_class = FastAPIEstimationSerializers


class FastAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FastAPIProjectEstimation.objects.all()
    serializer_class = FastAPIEstimationSerializers



#  Flask
class FlaskList(generics.ListCreateAPIView):
    queryset = models.FlaskProjectEstimation.objects.all()
    serializer_class = FlaskEstimationSerializers


class FlaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FlaskProjectEstimation.objects.all()
    serializer_class = FlaskEstimationSerializers



#  Node
class NodeList(generics.ListCreateAPIView):
    queryset = models.NodeProjectEstimation.objects.all()
    serializer_class = NodeEstimationSerializers


class NodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NodeProjectEstimation.objects.all()
    serializer_class = NodeEstimationSerializers



#  React
class ReactList(generics.ListCreateAPIView):
    queryset = models.ReactProjectEstimation.objects.all()
    serializer_class = ReactEstimationSerializers


class ReactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ReactProjectEstimation.objects.all()
    serializer_class = ReactEstimationSerializers




#  Vue
class VueList(generics.ListCreateAPIView):
    queryset = models.VueProjectEstimation.objects.all()
    serializer_class = VueEstimationSerializers


class VueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.VueProjectEstimation.objects.all()
    serializer_class = VueEstimationSerializers



#  Angular
class AngularList(generics.ListCreateAPIView):
    queryset = models.AngularProjectEstimation.objects.all()
    serializer_class = AngularEstimationSerializers


class AngularDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AngularProjectEstimation.objects.all()
    serializer_class = AngularEstimationSerializers




#  NextJS
class NextJSList(generics.ListCreateAPIView):
    queryset = models.NextJSProjectEstimation.objects.all()
    serializer_class = NextJSEstimationSerializers


class NextJSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NextJSProjectEstimation.objects.all()
    serializer_class = NextJSEstimationSerializers



#  Native Android
class NativeAndroidList(generics.ListCreateAPIView):
    queryset = models.NativeAndroidProjectEstimation.objects.all()
    serializer_class = NativeAndroidEstimationSerializers


class NativeAndroidDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NativeAndroidProjectEstimation.objects.all()
    serializer_class = NativeAndroidEstimationSerializers




#  Native iOS
class NativeIOSList(generics.ListCreateAPIView):
    queryset = models.NativeIOSProjectEstimation.objects.all()
    serializer_class = NativeIOSEstimationSerializers


class NativeIOSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NativeIOSProjectEstimation.objects.all()
    serializer_class = NativeIOSEstimationSerializers



#  Flutter
class FlutterList(generics.ListCreateAPIView):
    queryset = models.FlutterProjectEstimation.objects.all()
    serializer_class = FlutterEstimationSerializers


class FlutterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FlutterProjectEstimation.objects.all()
    serializer_class = FlutterEstimationSerializers




#  React Native
class ReactNativeList(generics.ListCreateAPIView):
    queryset = models.ReactNativeProjectEstimation.objects.all()
    serializer_class = ReactNativeEstimationSerializers


class ReactNativeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ReactNativeProjectEstimation.objects.all()
    serializer_class = ReactNativeEstimationSerializers
