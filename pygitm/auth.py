# -*- coding: utf-8 -*-

import getpass


class SSHAuth:
    def __init__(self, ssh_key: str) -> None:
        self._ssh_key = ssh_key

    @classmethod
    def from_identity_file(cls, filepath: str) -> None:
        with open(filepath) as f:
            ssh_key = f.read()
        return cls(ssh_key)


class HTTPSAuth:
    def __init__(self, username: str, password: str) -> None:
        self._username = username
        self._password = password

    @classmethod
    def from_prompt(cls):
        username = getpass.getuser()
        password = getpass.getpass()
        return cls(username, password)
