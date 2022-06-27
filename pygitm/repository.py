# -*- coding: utf-8 -*-

from pygitm.auth import HTTPSAuth, SSHAuth
from pygitm.options import CloneOptions


class LocalRepository:
    ...


class RemoteRepository:
    def SSH_clone(self, opts: CloneOptions, auth: SSHAuth) -> LocalRepository:
        ...  # --config core.sshCommand="ssh -i ~/location/to/private_ssh_key"

    def HTTPS_clone(self, opts: CloneOptions, auth: HTTPSAuth) -> LocalRepository:
        ...
