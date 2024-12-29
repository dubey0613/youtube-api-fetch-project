import urllib.parse

def paginate(query, page, per_page):
    """Helper function to paginate a SQLAlchemy query."""
    return query.offset((page - 1) * per_page).limit(per_page)

def build_youtube_url(search_query, youtube_api_key, published_after):
    base_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': search_query,
        'key': youtube_api_key,
        'type': 'video',
        'order': 'date',
        'publishedAfter': published_after
    }
    query_string = urllib.parse.urlencode(params)
    
    url = f"{base_url}?{query_string}"
    return url