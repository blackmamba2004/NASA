def paginate(data: list, page: int = 1, size: int = 30):
    total_items = len(data)
    start = (page - 1) * size
    end = start + size

    paginator = {
        "page": page,
        "total": total_items // size,
        "has_prev": page > 1,
        "has_next": end < total_items
    }

    return data[start:end], paginator