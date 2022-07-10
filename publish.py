#!/usr/bin/env python3

"""
    Helper to publish this Project to PyPi
"""

from pathlib import Path

from poetry_publish.publish import poetry_publish
from poetry_publish.utils.subprocess_utils import verbose_check_call

import beautiful_barcode


PACKAGE_ROOT = Path(beautiful_barcode.__file__).parent.parent


def publish():
    """
        Publish to PyPi
        Call this via:
            $ poetry run publish
    """
    verbose_check_call('make', 'pytest')  # don't publish if tests fail
    verbose_check_call('make', 'fix-code-style')  # don't publish if code style wrong

    poetry_publish(package_root=PACKAGE_ROOT, version=beautiful_barcode.__version__)


if __name__ == '__main__':
    publish()
