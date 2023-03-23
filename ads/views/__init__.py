from .ad import AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, AdLoadImageView
from .category import CatListView, CatDetailView, CatCreateView, CatUpdateView, CatDeleteView
from .service import root

__all__ = ['root']

__all__.extend([
    'CatListView',
    'CatDetailView',
    'CatCreateView',
    'CatUpdateView',
    'CatDeleteView',
])

__all__.extend([
    'AdListView',
    'AdDetailView',
    'AdCreateView',
    'AdUpdateView',
    'AdDeleteView',
    'AdLoadImageView',
])
