.. contents::

Introduction
============

This package is part of the templer code generator system.  It provides local
command templates for the ``archetype`` and ``plone_basic`` templates from
templer.plone_ and is dependent on that package.  Installing 
``templer.plone[localcommands]`` will automatically include this package.

Local Commands
==============

Templer local commands are an extension of the PasteScript_ local command 
concept which allow the user to insert additional features into a skeleton 
package already created by a templer template.

Executing Local Commands
------------------------

The first step in accessing local commands is to build a package skeleton 
using one of the templer templates which support local commands::

    bin/templer plone_basic example.package

When the run is completed, you should see output that informs you that 
localcommands are available for this new package::

    Your new package supports local commands. To access them, change
    directories into the 'src' directory inside your new package. From there,
    you will be able to run the command `paster add --list` to see the local
    commands available for this package.

Follow these instructions to see the local commands you have available to you
from the context of your ``plone_basic`` package skeleton.  You may also run
``paster add --list-all`` to see the full list of local commands available in
your current installation.  Commands not available within the current package
will be prefaced with an 'N' character in the listing.

Provided Local Templates
------------------------

This package provides local command templates for the ``archetype`` and 
``plone_basic`` templates:

archetype
+++++++++

contenttype
  A skeleton Archetypes content type

schema_field
  An iterative generator for Archetypes schema fields

plone_basic
+++++++++++

browserview
  A zope BrowserView class, interface and template

browserlayer
  A zope BrowserLayer interface and GenericSetup registration

Issues
======

Issues with this package should be reported in the package repository on 
GitHub_.

.. _templer.plone: http://pypi.python.org/pypi/templer.plone
.. _PasteScript: http://pythonpaste.org/script/
.. _GitHub: http://github.com/collective/templer.plone.localcommands/issues
