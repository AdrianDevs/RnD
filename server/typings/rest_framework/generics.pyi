"""
This type stub file was generated by pyright.
"""

from rest_framework import mixins, views

"""
Generic views that provide commonly needed behaviour.
"""

def get_object_or_404(queryset, *filter_args, **filter_kwargs):
    """
    Same as Django's standard shortcut, but make sure to also raise 404
    if the filter_kwargs don't match the required types.
    """
    ...

class GenericAPIView(views.APIView):
    """
    Base class for all other generic views.
    """

    queryset = ...
    serializer_class = ...
    lookup_field = ...
    lookup_url_kwarg = ...
    filter_backends = ...
    pagination_class = ...
    def __class_getitem__(cls, *args, **kwargs):  # -> type[Self]:
        ...
    def get_queryset(self):
        """
        Get the list of items for this view.
        This must be an iterable, and may be a queryset.
        Defaults to using `self.queryset`.

        This method should always be used rather than accessing `self.queryset`
        directly, as `self.queryset` gets evaluated only once, and those results
        are cached for all subsequent requests.

        You may want to override this if you need to provide different
        querysets depending on the incoming request.

        (Eg. return a list of items that is specific to the user)
        """
        ...

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        ...

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        ...

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.

        You may want to override this if you need to provide different
        serializations depending on the incoming request.

        (Eg. admins get full serialization, others get basic serialization)
        """
        ...

    def get_serializer_context(self):  # -> dict[str, Any]:
        """
        Extra context provided to the serializer class.
        """
        ...

    def filter_queryset(self, queryset):  # -> Any:
        """
        Given a queryset, filter it with whichever filter backend is in use.

        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        ...

    @property
    def paginator(self):  # -> Any | None:
        """
        The paginator instance associated with the view, or `None`.
        """
        ...

    def paginate_queryset(self, queryset):  # -> Any | None:
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        ...

    def get_paginated_response(self, data):  # -> Any:
        """
        Return a paginated style `Response` object for the given output data.
        """
        ...

class CreateAPIView(mixins.CreateModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance.
    """
    def post(self, request, *args, **kwargs):  # -> Response:
        ...

class ListAPIView(mixins.ListModelMixin, GenericAPIView):
    """
    Concrete view for listing a queryset.
    """
    def get(self, request, *args, **kwargs):  # -> Response:
        ...

class RetrieveAPIView(mixins.RetrieveModelMixin, GenericAPIView):
    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):  # -> Response:
        ...

class DestroyAPIView(mixins.DestroyModelMixin, GenericAPIView):
    """
    Concrete view for deleting a model instance.
    """
    def delete(self, request, *args, **kwargs):  # -> Response:
        ...

class UpdateAPIView(mixins.UpdateModelMixin, GenericAPIView):
    """
    Concrete view for updating a model instance.
    """
    def put(self, request, *args, **kwargs):  # -> Response:
        ...
    def patch(self, request, *args, **kwargs):  # -> Response:
        ...

class ListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    def get(self, request, *args, **kwargs):  # -> Response:
        ...
    def post(self, request, *args, **kwargs):  # -> Response:
        ...

class RetrieveUpdateAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    """
    Concrete view for retrieving, updating a model instance.
    """
    def get(self, request, *args, **kwargs):  # -> Response:
        ...
    def put(self, request, *args, **kwargs):  # -> Response:
        ...
    def patch(self, request, *args, **kwargs):  # -> Response:
        ...

class RetrieveDestroyAPIView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    """
    Concrete view for retrieving or deleting a model instance.
    """
    def get(self, request, *args, **kwargs):  # -> Response:
        ...
    def delete(self, request, *args, **kwargs):  # -> Response:
        ...

class RetrieveUpdateDestroyAPIView(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView
):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """
    def get(self, request, *args, **kwargs):  # -> Response:
        ...
    def put(self, request, *args, **kwargs):  # -> Response:
        ...
    def patch(self, request, *args, **kwargs):  # -> Response:
        ...
    def delete(self, request, *args, **kwargs):  # -> Response:
        ...
