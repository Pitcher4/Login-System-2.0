import hashlib
import secrets
import json
import time


class User:
    def __init__(username: str, password: str, full_name: str) -> None: