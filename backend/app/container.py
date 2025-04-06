from dishka import make_async_container

from backend.app.providers import provider_list

container = make_async_container(
    *provider_list()
)