# noinspection PyUnresolvedReferences
from ..fixtures import client


def test_endpoints_are_valid(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert rv.status_code == 200

