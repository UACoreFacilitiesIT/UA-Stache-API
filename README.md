# UA-Stache-API
Allows the caller to easily get "secret" information from stache entries at [https://stache.arizona.edu].

## Motivation
To make a python API that could generically get information from stache.

## Code Example
```python
from ua_stache_api import ua_stache_api


key, url = ua_stache_api.get_entry(file_name)
ua_stache_api.auth(key, url)
```
Where file_name is the name of file with content such as:
```JSON
{
    "X-STACHE-READ-KEY": "stache_read_key",
    "endpoint": "stache_endpoint"
}
```

stache secret must be a JSON-able dictionary that can be nested.

## Installation
pip install --user ua-stache-api

## Tests
cd ./ua_stache_api/tests
python -m nose ./test_ua_stache_api.py

## Credits
[sterns1](https://github.com/sterns1)
[raflopjr](https://github.com/raflopjr)
[RyanJohannesBland](https://github.com/RyanJohannesBland)

## License
MIT
