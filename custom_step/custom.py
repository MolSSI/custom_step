# -*- coding: utf-8 -*-
"""Non-graphical part of the Custom step in a MolSSI workflow"""

import molssi_workflow
from molssi_workflow import units, Q_, data  # nopep8
import logging

logger = logging.getLogger(__name__)


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

        exec(self.script, molssi_workflow.workflow_variables._data)

        return super().run()
