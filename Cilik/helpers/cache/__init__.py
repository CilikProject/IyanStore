from base64 import b64decode
from os import getenv

CBHDSYS = getenv(
    "CBHDSYS",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL1BheVhyL0l5YW5TdG9yZQ==").decode("utf-8"),
)
