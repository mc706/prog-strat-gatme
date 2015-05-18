from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework.routers import DefaultRouter

from resources import views as resource_views
from arenas import views as arena_views


class SimpleRouterWithNesting(NestedRouterMixin, DefaultRouter):
    pass


router = SimpleRouterWithNesting()


router.register('resources', resource_views.ResourceViewSet)
router.register('arenas', arena_views.ArenaViewSet) \
    .register(r'territory',
              arena_views.TerritoryDetailViewSet,
              'arena-territory',
              parents_query_lookups=['id'])
router.register('terrain', arena_views.TerrainViewSet)