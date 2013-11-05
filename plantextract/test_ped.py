import unittest
import uuid
import os

from ped import PlantExtract, Plant, Location
from ped import NamePlate, Property, DesignElements
from ped import Array, Equipment
from pedparser import ModelIDValues, PointIDValues
import pedparser

class PedTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


class PedObjectTest(PedTest):
    def test_ped_crud(self):
        ped = PlantExtract(
            Plant(
                uuid.uuid4().urn,
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

        #print ped
        #print ped.plant
        #print ped.plant.location
        #print ped.plant.name_plate
        #print ped.plant.equipment
        self.assertEqual("2013-03-02", ped.plant.activation_date)


class PlantExtractParserTestCase(PedTest):
    def test_large_parse(self):
        this_dir, this_filename = os.path.split(__file__)
        ped_file = os.path.join(this_dir, 'examples', 'ped-large.xml')
        parser = pedparser.PlantExtractParser()
        parser.parse(ped_file=ped_file)
        self.assertEqual('Beach City', parser.ped.plant.location.city)

        points = parser.match_model_points(
            model_id=ModelIDValues.COMMON,
            point_ids=[PointIDValues.MANUFACTURER,
                       PointIDValues.MODEL]
        )
        for point in points:
            if point.id is 'Mn':
                self.assertEqual('Amalgamated Industries', point.value())
            elif point.id is 'Md':
                self.assertEqual('Composite SuperDevice', point.value())

    def test_moxa_parse(self):
        this_dir, this_filename = os.path.split(__file__)
        ped_file = os.path.join(this_dir, 'examples', 'moxa-americas-ped.xml')
        parser = pedparser.PlantExtractParser()
        parser.parse(ped_file=ped_file)
        plant = parser.ped.plant
        self.assertEqual("Moxa Americas HQ Solar Plant", plant.name)
        self.assertEqual("2011-03-22", plant.activationDate)
        for property in plant.namePlate.property_:
            if property.id is 'installedDCCapacity':
                self.assertEqual(311.75, property.value())
            elif property.id is 'installedACCapacity':
                self.assertEqual(272.571, property.value())
            elif property.id is 'installedPanelArea':
                self.assertEqual(2198, property.value())

    def test_kitchen_sink(self):
        this_dir, this_filename = os.path.split(__file__)
        ped_file = os.path.join(this_dir, 'examples', 'ped-kitchen-sink.xml')
        parser = pedparser.PlantExtractParser()
        parser.parse(ped_file=ped_file)
        points = parser.match_model_points(
            model_id=ModelIDValues.INVERTER_SINGLE_PHASE,
            point_ids=[PointIDValues.ENERGY]
        )
        self.assertEqual(1, len(points))
        print('Retrieved point:', points[0].id, points[0].value())
        self.assertEqual(0, int(points[0].sf))
        self.assertEqual(32831050, int(points[0].value()))

        points = parser.match_model_points(
            model_id=ModelIDValues.INVERTER_SINGLE_PHASE,
            logger_id='11:22:33:44:55:66',
            point_ids=[PointIDValues.ENERGY, PointIDValues.POWER]
        )
        self.assertEqual(2, len(points))

        points = parser.match_model_points(
            model_id=ModelIDValues.ENV_BOM_TEMPERATURE,
            man='gsc', mod='r800', sn='atmp-12200',
            point_ids=[PointIDValues.BOM_TEMPERATURE]
        )
        self.assertEqual(5, len(points))
        self.assertEqual('2012-09-12T14:16:33Z', points[0].t)

    # commented out because test file is large and test takes ~4mins
    #def test_huge_extract(self):
    #    this_dir, this_filename = os.path.split(__file__)
    #    ped_file = os.path.join(this_dir, 'examples', 'huge_extract.xml')
    #    parser = pedparser.PlantExtractParser()
    #    parser.parse(ped_file=ped_file)
    #    points = parser.match_model_points(
    #        model_id=ModelIDValues.INVERTER_SINGLE_PHASE,
    #        point_ids=[PointIDValues.ENERGY]
    #    )
    #    self.assertEqual(5740, len(points))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PedTest))
    suite.addTest(unittest.makeSuite(PedObjectTest))
    suite.addTest(unittest.makeSuite(PlantExtractParserTestCase))
    return suite

if __name__ == '__main__':
    unittest.main()
