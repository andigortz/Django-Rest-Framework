from rest_framework.routers import DefaultRouter
from shelf.views import AuthorViewSet, BookViewSet, EditionViewSet
from rest_framework_extensions.routers import NestedRouterMixin

router = DefaultRouter()

router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()

authors_router = router.register('authors', AuthorViewSet)
authors_router.register(
    'books',
    BookViewSet,
    base_name='author-books',
    parents_query_lookups=['author']).register('editions', EditionViewSet, base_name='author-books-edition', parents_query_lookups=['book__author', 'book'])
