"""
This type stub file was generated by pyright.
"""

from rest_framework.fields import Field

def method_overridden(method_name, klass, instance): # -> bool:
    """
    Determine if a method has been overridden.
    """
    ...

class ObjectValueError(ValueError):
    """
    Raised when `queryset.get()` failed due to an underlying `ValueError`.
    Wrapping prevents calling code conflating this with unrelated errors.
    """
    ...


class ObjectTypeError(TypeError):
    """
    Raised when `queryset.get()` failed due to an underlying `TypeError`.
    Wrapping prevents calling code conflating this with unrelated errors.
    """
    ...


class Hyperlink(str):
    """
    A string like object that additionally has an associated name.
    We use this for hyperlinked URLs that may render as a named link
    in some contexts, or render as a plain URL in others.
    """
    def __new__(cls, url, obj): # -> Self:
        ...
    
    def __getnewargs__(self): # -> tuple[str, str]:
        ...
    
    @property
    def name(self): # -> str:
        ...
    
    is_hyperlink = ...


class PKOnlyObject:
    """
    This is a mock object, used for when we only need the pk of the object
    instance, but still want to return an object with a .pk attribute,
    in order to keep the same interface as a regular model instance.
    """
    def __init__(self, pk) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


MANY_RELATION_KWARGS = ...
class RelatedField(Field):
    queryset = ...
    html_cutoff = ...
    html_cutoff_text = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def __new__(cls, *args, **kwargs): # -> ManyRelatedField | Self:
        ...
    
    @classmethod
    def many_init(cls, *args, **kwargs): # -> ManyRelatedField:
        """
        This method handles creating a parent `ManyRelatedField` instance
        when the `many=True` keyword argument is passed.

        Typically you won't need to override this method.

        Note that we're over-cautious in passing most arguments to both parent
        and child classes in order to try to cover the general case. If you're
        overriding this method you'll probably want something much simpler, eg:

        @classmethod
        def many_init(cls, *args, **kwargs):
            kwargs['child'] = cls()
            return CustomManyRelatedField(*args, **kwargs)
        """
        ...
    
    def run_validation(self, data=...): # -> empty | None:
        ...
    
    def get_queryset(self): # -> Manager[Any] | QuerySet[Any] | None:
        ...
    
    def use_pk_only_optimization(self): # -> Literal[False]:
        ...
    
    def get_attribute(self, instance): # -> PKOnlyObject | Any | empty | None:
        ...
    
    def get_choices(self, cutoff=...): # -> dict[Any, Any] | dict[Any, str]:
        ...
    
    @property
    def choices(self): # -> dict[Any, Any] | dict[Any, str]:
        ...
    
    @property
    def grouped_choices(self): # -> dict[Any, Any] | dict[Any, str]:
        ...
    
    def iter_options(self): # -> Generator[StartOptionGroup | Option | EndOptionGroup, Any, None]:
        ...
    
    def display_value(self, instance): # -> str:
        ...
    


class StringRelatedField(RelatedField):
    """
    A read only field that represents its targets using their
    plain string representation.
    """
    def __init__(self, **kwargs) -> None:
        ...
    
    def to_representation(self, value): # -> str:
        ...
    


class PrimaryKeyRelatedField(RelatedField):
    default_error_messages = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def use_pk_only_optimization(self): # -> Literal[True]:
        ...
    
    def to_internal_value(self, data):
        ...
    
    def to_representation(self, value):
        ...
    


class HyperlinkedRelatedField(RelatedField):
    lookup_field = ...
    view_name = ...
    default_error_messages = ...
    def __init__(self, view_name=..., **kwargs) -> None:
        ...
    
    def use_pk_only_optimization(self): # -> bool:
        ...
    
    def get_object(self, view_name, view_args, view_kwargs):
        """
        Return the object corresponding to a matched URL.

        Takes the matched URL conf arguments, and should return an
        object instance, or raise an `ObjectDoesNotExist` exception.
        """
        ...
    
    def get_url(self, obj, view_name, request, format): # -> Any | str | None:
        """
        Given an object, return the URL that hyperlinks to the object.

        May raise a `NoReverseMatch` if the `view_name` and `lookup_field`
        attributes are not configured to correctly match the URL conf.
        """
        ...
    
    def to_internal_value(self, data):
        ...
    
    def to_representation(self, value): # -> Hyperlink | None:
        ...
    


class HyperlinkedIdentityField(HyperlinkedRelatedField):
    """
    A read-only field that represents the identity URL for an object, itself.

    This is in contrast to `HyperlinkedRelatedField` which represents the
    URL of relationships to other objects.
    """
    def __init__(self, view_name=..., **kwargs) -> None:
        ...
    
    def use_pk_only_optimization(self): # -> Literal[False]:
        ...
    


class SlugRelatedField(RelatedField):
    """
    A read-write field that represents the target of the relationship
    by a unique 'slug' attribute.
    """
    default_error_messages = ...
    def __init__(self, slug_field=..., **kwargs) -> None:
        ...
    
    def to_internal_value(self, data):
        ...
    
    def to_representation(self, obj): # -> Any:
        ...
    


class ManyRelatedField(Field):
    """
    Relationships with `many=True` transparently get coerced into instead being
    a ManyRelatedField with a child relationship.

    The `ManyRelatedField` class is responsible for handling iterating through
    the values and passing each one to the child relationship.

    This class is treated as private API.
    You shouldn't generally need to be using this class directly yourself,
    and should instead simply set 'many=True' on the relationship.
    """
    initial = ...
    default_empty_html = ...
    default_error_messages = ...
    html_cutoff = ...
    html_cutoff_text = ...
    def __init__(self, child_relation=..., *args, **kwargs) -> None:
        ...
    
    def get_value(self, dictionary): # -> type[empty]:
        ...
    
    def to_internal_value(self, data): # -> list[Any]:
        ...
    
    def get_attribute(self, instance): # -> list[Any] | empty | Any | None:
        ...
    
    def to_representation(self, iterable): # -> list[Any]:
        ...
    
    def get_choices(self, cutoff=...):
        ...
    
    @property
    def choices(self):
        ...
    
    @property
    def grouped_choices(self):
        ...
    
    def iter_options(self): # -> Generator[StartOptionGroup | Option | EndOptionGroup, Any, None]:
        ...
    


