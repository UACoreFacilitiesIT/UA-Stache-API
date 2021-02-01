"""Retrieves information stored in stache entry secrets."""

import requests
import json


def auth(key, url, cred_type=None, get_all=False):
    """Takes api keys and returns the desired from the stache entry's secret.

    Arguments:
        key: The stache X-STACHE-READ-KEY.
        url: The stache endpoint.
        cred_type: Key mapping to desired cred within stache secret, where
            nested dictionary keys are separated by '/'.

    Returns:
        Requested credentials if found, None if they could not be found.

    Requirements:
        The secret must be a json-able dictionary, with any number of nested
            dictionaries within it.
    """
    response = requests.get(url, headers=key)
    response.raise_for_status()
    response = response.json()

    secret = json.loads(response["secret"])

    if get_all:
        result = response
        result["secret"] = secret
    else:
        result = secret

    if cred_type:
        for key in cred_type.split('/'):
            result = result.get(key)

    return result


def get_entry(file_contents):
    """Loads file from filename and returns the stache information as a tuple.

    Arguments:
        file_contents: File contents which stores X-STACHE-READ-KEY and
            endpoint as a JSON. The contents must be in the format:
        {
            "X-STACHE-READ-KEY": "stache_read_key",
            "endpoint": "stache_endpoint"
        }

    Returns:
        returns (key, url) of the api entry as a tuple.
    """
    creds = json.loads(file_contents)

    # Get key, check for old version of json's first.
    key = creds.get("X-STACHE-READ-KEY")
    if not key:
        key = creds["X-STACHE-KEY"]

    # Grab endpoint.    
    endpoint = creds["endpoint"]

    # Format for request.
    key = {"X-STACHE-KEY": key}
    url = f"https://stache.arizona.edu{endpoint}"
    return key, url


def post(key, url, contents):
    """Updates contents of an entry in Stache.

    Arguments:
        key: The stache X-STACHE-KEY.
        url: The stache endpoint.
        contents: The body of the post to update stache entry with.

    Returns:
        Response to post message.
    Requirements:
        Url must be full endpoint, including https://stache...
        Contents must be a dictionary, containing at least a 'secret' key.
    """
    contents["secret"] = json.dumps(contents["secret"])
    response = requests.post(url, json=contents, headers=key)
    response.raise_for_status()
    contents["secret"] = json.loads(contents["secret"])
    return response
