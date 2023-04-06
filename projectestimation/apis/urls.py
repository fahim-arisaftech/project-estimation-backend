from django.urls import path

from .views import AngularDetail, AngularList, DjangoList, DjangoDetail, DotNetDetail, DotNetList, FastAPIDetail, FastAPIList, FlaskDetail, FlaskList, FlutterDetail, FlutterList, NativeAndroidDetail, NativeAndroidList, NativeIOSDetail, NativeIOSList, NextJSDetail, NextJSList, NodeDetail, NodeList, PHPDetail, PHPList, ReactDetail, ReactList, ReactNativeDetail, ReactNativeList, SpringBootDetail, SpringBootList, VueDetail, VueList, WordpressDetail, WordpressList

urlpatterns = [
    path('django', DjangoList.as_view()),
    path('<int:pk>/', DjangoDetail.as_view()),
    path('php', PHPList.as_view()),
    path('<int:pk>/', PHPDetail.as_view()),
    path('wordpress', WordpressList.as_view()),
    path('<int:pk>/', WordpressDetail.as_view()),
    path('dotnet', DotNetList.as_view()),
    path('<int:pk>/', DotNetDetail.as_view()),
    path('springboot', SpringBootList.as_view()),
    path('<int:pk>/', SpringBootDetail.as_view()),
    path('fastapi', FastAPIList.as_view()),
    path('<int:pk>/', FastAPIDetail.as_view()),
    path('flask', FlaskList.as_view()),
    path('<int:pk>/', FlaskDetail.as_view()),
    path('node', NodeList.as_view()),
    path('<int:pk>/', NodeDetail.as_view()),
    path('react', ReactList.as_view()),
    path('<int:pk>/', ReactDetail.as_view()),
    path('vue', VueList.as_view()),
    path('<int:pk>/', VueDetail.as_view()),
    path('angular', AngularList.as_view()),
    path('<int:pk>/', AngularDetail.as_view()),
    path('nextjs', NextJSList.as_view()),
    path('<int:pk>/', NextJSDetail.as_view()),
    path('nativeandroid', NativeAndroidList.as_view()),
    path('<int:pk>/', NativeAndroidDetail.as_view()),
    path('nativeios', NativeIOSList.as_view()),
    path('<int:pk>/', NativeIOSDetail.as_view()),
    path('flutter', FlutterList.as_view()),
    path('<int:pk>/', FlutterDetail.as_view()),
    path('reactnative', ReactNativeList.as_view()),
    path('<int:pk>/', ReactNativeDetail.as_view()),
]