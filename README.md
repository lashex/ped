Plant Extract Document processor
================================
A package for interacting with and creating [SunSpec](http://sunspec.org)
Plant Extract Documents and the standard blocks contained therein.

Installation
------------
Using pip::

    pip install plantextract

Usage
-------
Typical `parse` usage looks like this::

    #!/usr/bin/env python

    from plantextract.ped import PlantExtract
    from plantextract.smdx import SMDX

    ped = PlantExtract()
    ped.parse('ped-cls-to-process') # automatic parsing of envelope
    ped.parse_data()    # will parse an included sunSpecData block
    print ped.plant     # the Plant block
    print ped.plant.name    # the Plant's name attribute
    # ...etc...

    print ped.sunspec_data  # the sunSpecData block
    print ped.sunspec_data.device_records[0].models[0].smdx # SMDX info of model
    print ped.sunspec_data.device_records[0].models[0].points[0] # block structure

Typical `create` usage looks like this:

    #!/usr/bin/env python

    from plantextract.ped import PlantExtract, Plant, Location, NamePlate
    ped = PlantExtract.create(
            Plant.create(
              uuid4(),
              activation_date="2013-03-02",
              location=Location.create(latitude=1.1, longitude=2.2,
                                       city="Redwood City",
                                       state_province="CA"),
              name_plate=NamePlate.create(props=[
                Property('installedDCCapacity', 'float', '6.5'),
                Property('installedACCapacity', 'float', '6.4')
              ])
            ),
            # ...etc...
          )

Requires [lxml](http://lxml.de) 3.0.2.