from rest_framework import serializers
from rest_framework.reverse import reverse

from arenas.models import Arena, Territory, Terrain, TerritoryDetail


class TerritoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerritoryDetail
        fields = (
            'id',
            'territoryresource_set',
            'cost',
            'terrain',
        )


class TerritorySerializer(serializers.ModelSerializer):
    territory_detail_url = serializers.SerializerMethodField(read_only=True)
    territory_detail = TerritoryDetailSerializer(source='territorydetail', read_only=True)

    class Meta:
        model = Territory
        fields = (
            'id',
            'position_x',
            'position_y',
            'territory_detail',
            'territory_detail_url',
        )

    def get_territory_detail_url(self, obj):
        return reverse('arena-territory-detail', args=(obj.arena.id, obj.id,), request=self.context.get('request'))


class ArenaSerializer(serializers.ModelSerializer):
    territories = TerritorySerializer(source='territory_set', many=True, read_only=True)

    class Meta:
        model = Arena
        fields = (
            'id',
            'name',
            'territories',
            'size_x',
            'size_y',
        )


class TerrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terrain
        fields = (
            'name',
        )