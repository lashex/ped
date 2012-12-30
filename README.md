Plant Extract Document processor
================================
A package for interacting with SunSpec Plant Extract Documents and the
standard blocks contained therein. Hopefully this processor will make it
easier for you to receive and interact with Plant Extract documents.

Installation::
------------
    pip install plantextract
or... ::
    easy_install plantextract

Typical usage often looks like this::

    #!/usr/bin/env python

    from plantextract.ped import PlantExtract
    from plantextract.smdx import SMDX

    ped = PlantExtract('ped-file-to-process')
    ped.parse_data()    # will parse any existing sunSpecData block

Requires lxml 3.0 or later
