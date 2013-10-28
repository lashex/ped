import unittest
import uuid
import os

from ped import PlantExtract, Plant, Location
from ped import NamePlate, Property, DesignElements
from ped import Array, Equipment
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

        print ped
        print ped.plant
        print ped.plant.location
        print ped.plant.name_plate
        print ped.plant.equipment
        self.assertEqual("2013-03-02", ped.plant.activation_date)


class PlantExtractParserTestCase(PedTest):
    def test_parse(self):
        parser = pedparser.PlantExtractParser()
        this_dir, this_filename = os.path.split(__file__)
        ped_file = os.path.join(this_dir, 'examples', 'ped-large.xml')
        parser.parse(ped_file=ped_file)
        self.assertEqual("Beach City", parser.ped.plant.location.city)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PedTest))
    suite.addTest(unittest.makeSuite(PedObjectTest))
    suite.addTest(unittest.makeSuite(PlantExtractParserTestCase))
    return suite

if __name__ == '__main__':
    unittest.main()
