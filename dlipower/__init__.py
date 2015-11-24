# Copyright (c) 2009-2015, Dwight Hubbard
# Copyrights licensed under the New BSD License
# See the accompanying LICENSE.txt file for terms.

from .dlipower import Outlet, PowerSwitch
import json
import os



__version__ = str('0.0.0')
__git_version__ = str("")
__git_origin__ = str("")
__git_branch__ = str("")
__git_hash__ = str("")
__source_url__ = str('')

# noinspection PyUnresolvedReferences
_metadata_file = os.path.join(
    os.path.dirname(__file__),
    'package_metadata.json'
)
if os.path.exists(_metadata_file):  # pragma: no cover
    with open(_metadata_file) as fh:
        _package_metadata = json.load(fh)
        __version__ = str(_package_metadata['version'])
        __git_version__ = str(_package_metadata['git_version'])
        __git_origin__ = str(_package_metadata['git_origin'])
        __git_branch__ = str(_package_metadata['git_branch'])
        __git_hash__ = str(_package_metadata['git_hash'])
        __git_base_url__ = 'https://github.com/yahoo/redislite'
        if __git_origin__.endswith('.git'):  # pragma: no cover
            __git_base_url__ = __git_origin__[:-4].strip('/')
        __source_url__ = __git_base_url__ + '/tree/' + __git_hash__
