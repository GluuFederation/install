__author__ = 'yuriy'

import subprocess

def call(actions):
    """Run commands sequentially.
    1. Run command
    2. Wait for command to complete
    3. Run next command
    ...
    """
    for action in actions:
        print "\n%s\n" % action
        subprocess.call(action, shell=True)
