"""
gbpxargs module:
Contains argument identifiers.
"""
from enum import Enum


class Flag(Enum):
    """ Execution flag identifiers. """
    VERBOSE = 'verbose'
    QUIET = 'quiet'
    COLOR = 'color'
    SAFEMODE = 'safemode'


class Option(Enum):
    """ Execution option identifiers. """
    CONFIG = 'config'
    DIR = 'dir'
    NO_RESTORE = 'no-restore'
    VERSION = 'version'
    HELP = 'help'
    SHOW_FLAGS = 'show-flags'
    SHOW_OPTIONS = 'show-options'
    SHOW_ACTIONS = 'show-actions'


class Action(Enum):
    """ Execution action identifiers. """
    TEST_PKG = 'test-pkg'
    COMMIT_RELEASE = 'commit-release'
    UPDATE_CHANGELOG = 'update-changelog'
    TEST_BUILD = 'test-build'
    COMMIT_BUILD = 'commit-build'
    UPLOAD = 'upload'
    CLONE = 'clone'
    RESTORE = 'restore'
    CONFIG = 'config'
