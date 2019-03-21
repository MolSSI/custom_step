# -*- coding: utf-8 -*-
"""Non-graphical part of the Custom step in a MolSSI workflow"""

import molssi_workflow
from molssi_workflow import ureg, Q_, data  # nopep8
import logging
import os

logger = logging.getLogger(__name__)


class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


class Custom(molssi_workflow.Node):
    def __init__(self,
                 workflow=None,
                 extension=None):
        '''Setup the non-graphical part of the Custom step in a
        MolSSI workflow.

        Keyword arguments:
        '''
        logger.debug('Creating Custom {}'.format(self))

        self.script = ''

        super().__init__(
            workflow=workflow,
            title='Custom',
            extension=extension)

    def run(self):
        """Run a Custom step.
        """

        os.makedirs(self.directory, exist_ok=True)
        with cd(self.directory):
            exec(self.script, molssi_workflow.workflow_variables._data)

        return super().run()
