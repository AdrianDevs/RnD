"""
This type stub file was generated by pyright.
"""

def apply_suffix_patterns(urlpatterns, suffix_pattern, suffix_required, suffix_route=...):  # -> list[Any]:
    ...
def format_suffix_patterns(urlpatterns, suffix_required=..., allowed=...):  # -> list[Any]:
    """
    Supplement existing urlpatterns with corresponding patterns that also
    include a '.format' suffix.  Retains urlpattern ordering.

    urlpatterns:
        A list of URL patterns.

    suffix_required:
        If `True`, only suffixed URLs will be generated, and non-suffixed
        URLs will not be used.  Defaults to `False`.

    allowed:
        An optional tuple/list of allowed suffixes.  eg ['json', 'api']
        Defaults to `None`, which allows any suffix.
    """
    ...
