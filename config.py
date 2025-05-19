# Buitins that should never be executed (Security)
# Add any potentially dangerous functions here.
# The full list of builtins can be found at: https://www.openpolicyagent.org/docs/latest/policy-reference/#built-in-functions
import os


RESTRICTED_BUILTINS = [
    # 'http.send',
    # 'opa.runtime'
]

SQLITE3_DB_FILE_NAME = os.environ.get('SQLITE3_DB_FILE_NAME', 'db/policies.db')