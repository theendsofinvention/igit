"""
Contains a representation of GitHub users.
"""
from typing import Optional
from typing import Union

from IGitt import ElementDoesntExistError
from IGitt.GitLab import GitLabMixin
from IGitt.GitLab import GitLabOAuthToken
from IGitt.GitLab import GitLabPrivateToken
from IGitt.Interfaces.User import User
from IGitt.Interfaces import get


class GitLabUser(GitLabMixin, User):
    """
    A GitLab user, e.g. sils :)
    """

    def __init__(self,
                 token: Union[GitLabPrivateToken, GitLabOAuthToken],
                 identifier: Optional[Union[str, int]]=None):
        """
        Creates a new user.

        :param token: The oauth token object
        :param identifier: Pass None if it's you! Otherwise the id, integer.
        """
        self._token = token
        self._url = '/user'
        self._id = identifier
        if identifier:
            if isinstance(identifier, str):
                params =  {'username': identifier}
                resp = get(self._token, self.absolute_url('/users'), params)
                if resp:
                    self._id = resp[0]['id']
                    self._url = '/users/' + str(resp[0]['id'])
                else:
                    raise ElementDoesntExistError('This username does not '
                                                  'exist.')
            else:
                self._url = '/users/' + str(identifier)


    @property
    def username(self) -> str:
        """
        Retrieves the login for the user.
        """
        return self.data['username']

    @property
    def identifier(self) -> int:
        """
        Gets a unique id for the user that never changes.
        """
        return self._id or self.data['id']

    def installed_repositories(self, installation_id: int):
        """
        List repositories that are accessible to the authenticated user for an
        installation.

        GitLab doesn't support building installations yet.
        """
        raise NotImplementedError

    def get_installations(self, jwt):
        """
        Gets the installations this user has access to.

        GitLab doesn't support building installations yet.
        """
        raise NotImplementedError
