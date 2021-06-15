"""Simple helper to paginate query
"""
import logging
import math

from flask import request

logger = logging.getLogger(__name__)


DEFAULT_PAGE_SIZE = 50
DEFAULT_PAGE_NUMBER = 1


def get_page_and_per_page_from_request():
    try:
        page = int(request.args.get("page"))
    except (TypeError, ValueError):
        page = DEFAULT_PAGE_NUMBER

    try:
        per_page = int(request.args.get("page_size"))
    except (TypeError, ValueError):
        per_page = DEFAULT_PAGE_SIZE

    return page, per_page


def paginate(query, schema):

    page, per_page = get_page_and_per_page_from_request()
    page_obj = query.paginate(page=page, per_page=per_page)

    return {
        "current_page": page,
        "total": page_obj.total,
        "pages": page_obj.pages or 1,
        "data": schema.dump(page_obj.items),
    }


class SequencePaginator:
    """
    Paginator for sequence object. Returns result, like upper one

    """

    def __init__(self, sequence, page, page_size):
        self.page = page or DEFAULT_PAGE_NUMBER
        self.page_size = page_size or DEFAULT_PAGE_SIZE
        self.sequence = sequence

    def paginate(self):
        total = len(self.sequence)
        pages = math.ceil(total / self.page_size)
        from_ = (self.page - 1) * self.page_size
        to = from_ + self.page_size  # pylint: disable=invalid-name
        data = self.sequence[from_:to]
        return {
            "current_page": self.page,
            "total": total,
            "pages": pages,
            "data": data,
        }
