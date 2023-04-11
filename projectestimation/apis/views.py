from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt

from estimations import models
from .serializers import DjangoEstimationSerializers, PHPEstimationSerializers, WordpressEstimationSerializers, DotNetEstimationSerializers, SpringBootEstimationSerializers, FastAPIEstimationSerializers, FlaskEstimationSerializers, NodeEstimationSerializers, ReactEstimationSerializers, VueEstimationSerializers, AngularEstimationSerializers, NextJSEstimationSerializers, NativeAndroidEstimationSerializers, NativeIOSEstimationSerializers, FlutterEstimationSerializers, ReactNativeEstimationSerializers


#  Django
@csrf_exempt
class DjangoList(generics.ListCreateAPIView):
    queryset = models.DjangoProjectEstimation.objects.all()
    serializer_class = DjangoEstimationSerializers


@csrf_exempt
class DjangoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DjangoProjectEstimation.objects.all()
    serializer_class = DjangoEstimationSerializers


#  PHP
@csrf_exempt
class PHPList(generics.ListCreateAPIView):
    queryset = models.PHPProjectEstimation.objects.all()
    serializer_class = PHPEstimationSerializers


@csrf_exempt
class PHPDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PHPProjectEstimation.objects.all()
    serializer_class = PHPEstimationSerializers


#  Wordpress
@csrf_exempt
class WordpressList(generics.ListCreateAPIView):
    queryset = models.WordpressProjectEstimation.objects.all()
    serializer_class = WordpressEstimationSerializers


@csrf_exempt
class WordpressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.WordpressProjectEstimation.objects.all()
    serializer_class = WordpressEstimationSerializers



#  DOT NET
@csrf_exempt
class DotNetList(generics.ListCreateAPIView):
    queryset = models.DOTNetProjectEstimation.objects.all()
    serializer_class = DotNetEstimationSerializers


@csrf_exempt
class DotNetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DOTNetProjectEstimation.objects.all()
    serializer_class = DotNetEstimationSerializers



#  Spring Boot
@csrf_exempt
class SpringBootList(generics.ListCreateAPIView):
    queryset = models.SpringBootProjectEstimation.objects.all()
    serializer_class = SpringBootEstimationSerializers


@csrf_exempt
class SpringBootDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SpringBootProjectEstimation.objects.all()
    serializer_class = SpringBootEstimationSerializers



#  FastAPI
@csrf_exempt
class FastAPIList(generics.ListCreateAPIView):
    queryset = models.FastAPIProjectEstimation.objects.all()
    serializer_class = FastAPIEstimationSerializers


@csrf_exempt
class FastAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FastAPIProjectEstimation.objects.all()
    serializer_class = FastAPIEstimationSerializers



#  Flask
@csrf_exempt
class FlaskList(generics.ListCreateAPIView):
    queryset = models.FlaskProjectEstimation.objects.all()
    serializer_class = FlaskEstimationSerializers


@csrf_exempt
class FlaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FlaskProjectEstimation.objects.all()
    serializer_class = FlaskEstimationSerializers



#  Node
@csrf_exempt
class NodeList(generics.ListCreateAPIView):
    queryset = models.NodeProjectEstimation.objects.all()
    serializer_class = NodeEstimationSerializers


@csrf_exempt
class NodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NodeProjectEstimation.objects.all()
    serializer_class = NodeEstimationSerializers



#  React
@csrf_exempt
class ReactList(generics.ListCreateAPIView):
    queryset = models.ReactProjectEstimation.objects.all()
    serializer_class = ReactEstimationSerializers


@csrf_exempt
class ReactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ReactProjectEstimation.objects.all()
    serializer_class = ReactEstimationSerializers




#  Vue
@csrf_exempt
class VueList(generics.ListCreateAPIView):
    queryset = models.VueProjectEstimation.objects.all()
    serializer_class = VueEstimationSerializers


@csrf_exempt
class VueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.VueProjectEstimation.objects.all()
    serializer_class = VueEstimationSerializers



#  Angular
@csrf_exempt
class AngularList(generics.ListCreateAPIView):
    queryset = models.AngularProjectEstimation.objects.all()
    serializer_class = AngularEstimationSerializers


@csrf_exempt
class AngularDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AngularProjectEstimation.objects.all()
    serializer_class = AngularEstimationSerializers




#  NextJS
@csrf_exempt
class NextJSList(generics.ListCreateAPIView):
    queryset = models.NextJSProjectEstimation.objects.all()
    serializer_class = NextJSEstimationSerializers


@csrf_exempt
class NextJSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NextJSProjectEstimation.objects.all()
    serializer_class = NextJSEstimationSerializers



#  Native Android
@csrf_exempt
class NativeAndroidList(generics.ListCreateAPIView):
    queryset = models.NativeAndroidProjectEstimation.objects.all()
    serializer_class = NativeAndroidEstimationSerializers


@csrf_exempt
class NativeAndroidDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NativeAndroidProjectEstimation.objects.all()
    serializer_class = NativeAndroidEstimationSerializers




#  Native iOS
@csrf_exempt
class NativeIOSList(generics.ListCreateAPIView):
    queryset = models.NativeIOSProjectEstimation.objects.all()
    serializer_class = NativeIOSEstimationSerializers


@csrf_exempt
class NativeIOSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NativeIOSProjectEstimation.objects.all()
    serializer_class = NativeIOSEstimationSerializers



#  Flutter
@csrf_exempt
class FlutterList(generics.ListCreateAPIView):
    queryset = models.FlutterProjectEstimation.objects.all()
    serializer_class = FlutterEstimationSerializers


@csrf_exempt
class FlutterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FlutterProjectEstimation.objects.all()
    serializer_class = FlutterEstimationSerializers




#  React Native
@csrf_exempt
class ReactNativeList(generics.ListCreateAPIView):
    queryset = models.ReactNativeProjectEstimation.objects.all()
    serializer_class = ReactNativeEstimationSerializers


@csrf_exempt
class ReactNativeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ReactNativeProjectEstimation.objects.all()
    serializer_class = ReactNativeEstimationSerializers
