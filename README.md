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

    from pedparser import ModelIDValues, PointIDValues
    import plantextract.pedparser
    ...

    this_dir, this_filename = os.path.split(__file__)
    ped_file = os.path.join(this_dir, 'examples', 'ped-kitchen-sink.xml')
    parser = pedparser.PlantExtractParser()
    parser.parse(ped_file=ped_file)
    parser.ped.plant               # the Plant block
    parser.ped.plant.name          # the Plant's name attribute
    parser.ped.plant.location.city # the Plant's location city attribute

    # get ENERGY Points that are from an INVERTER_SINGLE_PHASE Model
    points = parser.match_model_points(
        model_id=ModelIDValues.INVERTER_SINGLE_PHASE,
        point_ids=[PointIDValues.ENERGY]
    )
    print('Retrieved point:', points[0].id, points[0].value())
    print('Point scale factor:', points[0].sf)
    print('Point value:', points[0].value())  # another way to get Point value

    # get ENERGY Points that are from an INVERTER_SINGLE_PHASE Model, but only
    # if the Device containing the Model has a logger ID of '11:22:33:44:55:66'
    points = parser.match_model_points(
        model_id=ModelIDValues.INVERTER_SINGLE_PHASE,
        logger_id='11:22:33:44:55:66',
        point_ids=[PointIDValues.ENERGY, PointIDValues.POWER]
    )
    print('Retrieved point:', points[0].id, points[0].value())
    # ...etc...

    # ...or one can directly interact with the sunSpecData block
    print parser.ped.sunSpecData.d   # the DeviceRecords list in the sunSpecData
    print parser.ped.sunSpecData.d[0].m # the Models list in the Zero'th Device
    print parser.ped.sunSpecData.d[0].m[0].p[0].id # the ID of the Zero'th Point
    # ...etc...


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

Requires [PyXB](http://pyxb.sourceforge.net) 1.2.3