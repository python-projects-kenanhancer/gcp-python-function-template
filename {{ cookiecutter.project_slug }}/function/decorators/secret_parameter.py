import os
import json
import functools
from google.cloud import secretmanager


def secret_parameter(secret_name, key=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self):
            if hasattr(self, "_cache") and func.__name__ in self._cache:
                return self._cache[func.__name__]

            client = secretmanager.SecretManagerServiceClient()
            project_id = os.environ.get("GCP_PROJECT")
            name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
            response = client.access_secret_version(name=name)
            payload = response.payload.data.decode("UTF-8")
            if key:
                secret_data = json.loads(payload)
                value = secret_data.get(key)
            else:
                value = payload

            if not hasattr(self, "_cache"):
                self._cache = {}
            self._cache[func.__name__] = value

            return value

        return wrapper

    return decorator
