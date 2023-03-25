from .ad import AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, AdLoadImageView
from .category import CatListView, CatDetailView, CatCreateView, CatUpdateView, CatDeleteView
from .location import LocationViewSet
from .service import root
from .user import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView

__all__ = ['root']

__all__ += [
    'CatListView',
    'CatDetailView',
    'CatCreateView',
    'CatUpdateView',
    'CatDeleteView',
]

__all__ += [
    'AdListView',
    'AdDetailView',
    'AdCreateView',
    'AdUpdateView',
    'AdDeleteView',
    'AdLoadImageView',
]

__all__ += [
    'UserListView',
    'UserDetailView',
    'UserCreateView',
    'UserUpdateView',
    'UserDeleteView',
]

__all__ += ['LocationViewSet']
