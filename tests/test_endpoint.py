import pytest
from requests import Response
from box import Box
from restfly.endpoint import APIEndpoint


@pytest.fixture
def e(api):
    return APIEndpoint(api)


def validate_endpoint(e, api):
    assert e._api == api
    assert e._log == api._log


@pytest.mark.vcr()
def test_endpoint_delete(e):
    resp = e._delete('delete', json={'test': 'value'})
    assert isinstance(resp, Response)


@pytest.mark.vcr()
def test_endpoint_head(e):
    resp = e._head('')
    assert isinstance(resp, Response)


@pytest.mark.vcr()
def test_endpoint_get(e):
    resp = e._get('get', json={'test': 'value'})
    assert isinstance(resp, Response)


@pytest.mark.vcr()
def test_endpoint_patch(e):
    resp = e._patch('patch', json={'test': 'value'})
    assert isinstance(resp, Response)


@pytest.mark.vcr()
def test_endpoint_post(e):
    resp = e._post('post', json={'test': 'value'})
    assert isinstance(resp, Response)


@pytest.mark.vcr()
def test_endpoint_put(e):
    resp = e._put('put', json={'test': 'value'})
    assert isinstance(resp, Response)


@pytest.mark.vcr()
def test_endpoint_base_request(e):
    resp = e._req('PUT', 'put', json={'test': 'value'})
    assert isinstance(resp, Response)
    
    # Test endpoint params:
    e._box = True
    e._box_attrs = {'default_box': True}
    assert isinstance(e._req('PUT', 'put', json={'test': 'value'}), Box)
    
    e._box = None
    e._conv_json = True
    assert isinstance(e._req('PUT', 'put', json={'test': 'value'}), dict)
    


@pytest.mark.vcr()
def test_endpoint_path_get(api):
    class TestAPI(APIEndpoint):
        _path = 'get'

        def get(self):
            return self._get()

    endpoint = TestAPI(api)
    resp = endpoint.get()
    assert isinstance(resp, Response)
