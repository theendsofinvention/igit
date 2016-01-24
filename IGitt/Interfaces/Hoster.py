"""
Contains the git Hoster abstraction.
"""


class Hoster:
    """
    Abstracts a service like GitHub and allows e.g. to query for available
    repositories and stuff like that.
    """
    @property
    def owned_repositories(self) -> {str}:
        """
        Retrieves the full names of the owned repositories as strings.

        :return: A set of strings.
        """
        raise NotImplementedError
