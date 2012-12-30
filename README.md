Plant Extract Document processor
================================
A package for interacting with SunSpec Plant Extract Documents and the
standard blocks contained therein.

Installation
------------
Using pip::

    pip install plantextract

Usage
-------
Typical usage often looks like this::

    #!/usr/bin/env python

    from plantextract.ped import PlantExtract
    from plantextract.smdx import SMDX

    ped = PlantExtract('ped-file-to-process')
    ped.parse_data()    # will parse any existing sunSpecData block

Requires lxml-3.0_ or later

.. _lxml-3.0: http://lxml.de