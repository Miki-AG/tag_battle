"""ht_battle_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from ht_battle_app.models import Battle
from rest_framework import routers, serializers, viewsets

class BatlleSerializer(serializers.HyperlinkedModelSerializer):
    """ http://127.0.0.1:8000/api/battles/1/ """
    who_is_winning = serializers.SerializerMethodField()
    def get_who_is_winning(self, battle):
        if battle.tag_1_typos < battle.tag_2_typos:
            return battle.tag_1
        elif battle.tag_1_typos > battle.tag_2_typos:
            return battle.tag_2
        else:
            return 'Draw'

    ### Serializers define the API representation ###
    class Meta:
        ### Meta class ###
        model = Battle
        fields = [
            'who_is_winning',
            'tag_1', 'tag_2',
            'tag_1_typos', 'tag_2_typos',
            'start', 'end']


# ViewSets define the view behavior.
class BatlleViewSet(viewsets.ModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BatlleSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'battles', BatlleViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
