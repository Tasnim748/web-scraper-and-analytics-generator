def build_page_url(base_url, pagepattern=None, page_number=None):
    """
    Constructs a paginated URL based on the base_url, pagepattern, and page_number.
    - base_url: must NOT have a trailing slash
    - pagepattern: must start with '/' or '?', or be None
    - page_number: int or None
    """
    if not base_url or base_url.endswith('/'):
        raise ValueError("base_url must not have a trailing slash")
    if pagepattern is None or page_number is None:
        return base_url
    if not (pagepattern.startswith('/') or pagepattern.startswith('?')):
        raise ValueError("pagepattern must start with '/' or '?'")
    if pagepattern.startswith('?'):
        if '?' in base_url:
            # Already has query params, use '&'
            return f"{base_url}&{pagepattern[1:]}={page_number}"
        else:
            return f"{base_url}{pagepattern}={page_number}"
    else:  # pagepattern starts with '/'
        return f"{base_url}{pagepattern}/{page_number}"