from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class RestaurantLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class RestaurantPageNumberPagination(PageNumberPagination):
    page_size = 2
