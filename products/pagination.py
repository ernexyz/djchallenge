from rest_framework.pagination import LimitOffsetPagination


class PaginationWithMaxLimit(LimitOffsetPagination):
    max_limit = 10
