import requests


class configuration:
    # update these values to your actual service URL and documentation path
    URL_SERVICE = "https://www.python.org/"
    DOC_PATH = "/docs"

def get_docs():
    """
    This function sends a GET request to the specified URL and retrieves the documentation.
    """
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)
print(response.text)