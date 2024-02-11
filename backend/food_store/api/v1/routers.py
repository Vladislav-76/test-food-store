from rest_framework.routers import Route, SimpleRouter


class CustomCartRouter(SimpleRouter):
    """Роутер для ручки cart."""

    routes = [
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'create',
                'delete': 'destroy',
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
    ]
