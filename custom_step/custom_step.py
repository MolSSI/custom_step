# -*- coding: utf-8 -*-
"""Helper class needed for the stevedore integration. Needs to provide
a description() method that returns a dict containing a description of
this node, and a factory() method for creating the graphical and non-graphical
nodes."""

import custom_step


class CustomStep(object):
    my_description = {
        'description':
        'An interface for Custom',
        'group': 'Simulations',
        'name': 'Custom'
    }

    def __init__(self, workflow=None, gui=None):
        """Initialize this helper class, which is used by
        the application via stevedore to get information about
        and create node objects for the workflow
        """
        pass

    def description(self):
        """Return a description of what this extension does
        """
        return CustomStep.my_description

    def create_node(self, workflow=None, **kwargs):
        """Return the new node object"""
        return custom_step.Custom(workflow=workflow, **kwargs)

    def create_tk_node(self, canvas=None, **kwargs):
        """Return the graphical Tk node object"""
        return custom_step.TkCustom(canvas=canvas, **kwargs)