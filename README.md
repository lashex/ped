Plant Extract Document processor
================================
A package for interacting with [SunSpec](http://sunspec.org) Plant Extract
Documents and the standard blocks contained therein.

Installation
------------
Using pip::

    pip install plantextract

Usage
-------
Typical usage looks like this::

    #!/usr/bin/env python

    from plantextract.ped import PlantExtract
    from plantextract.smdx import SMDX

    ped = PlantExtract('ped-file-to-process') # automatic parsing of envelope
    ped.parse_data()        # will parse an included sunSpecData block
    print ped.plant         # the Plant Info block
    print ped.sunspec_data  # the sunSpecData block

Requires [lxml](http://lxml.de) 3.0.1.