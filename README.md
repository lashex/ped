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

    from plantextract.pedparser import PlantExtractParser
    from plantextract.smdx import SMDX

    pedp = PlantExtractParser()
    pedp.parse('ped-cls-to-process') # automatic parsing of envelope
    pedp.parse_data()    # will parse an included sunSpecData block
    print pedp.plant     # the Plant block
    print pedp.plant.name    # the Plant's name attribute
    # ...etc...

    print pedp.sunspec_data  # the sunSpecData block
    print pedp.sunspec_data.device_records[0].models[0].smdx # SMDX info of model
    print pedp.sunspec_data.device_records[0].models[0].points[0] # block structure

Typical `create` usage looks like this:

    #!/usr/bin/env python

    from plantextract.ped import PlantExtract, Plant, Location
    from plantextract.ped import NamePlate, Array, Equipment

    ped = PlantExtract(
        Plant(
            uuid4(),
            activation_date="2013-03-02",
            location=Location(latitude=1.1, longitude=2.2,
                                     city="Redwood City",
                                     state_province="CA"),
            name_plate=NamePlate(props=[
                Property('installedDCCapacity', 'float', '6.5'),
                Property('installedACCapacity', 'float', '6.4')
            ]),
            design_elements=DesignElements(props=[
                Property('plantType', 'string', 'commercial')
            ]),
            array=Array(props=[
                Property('description','string','Carport')
            ], array_id=1),
            equipment=Equipment(props=[
                Property('Mn', 'string', 'MeterManuf'),
                Property('Md', 'string', 'MeterModel'),
                Property('uncertainty', 'float', '0.5')
            ], equipment_type='meter')
        )
    )

Requires [lxml](http://lxml.de) 3.2.1.