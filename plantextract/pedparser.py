# coding=utf-8
# Copyright 2013 Gridward LLC
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from operator import attrgetter
import logging
import plant_extract_pyxb


time_format = '%Y-%m-%dT%H:%M:%SZ'
#   logger = logging.getLogger('ped') f =
#   logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s') sh =
#   logging.StreamHandler() sh.setFormatter(f) logger.addHandler(sh)


class PlantExtractParser(object):
    """ A Plant Extract Document processor supporting straightforward
        interaction with information from each of the standard blocks.
    """

    def __init__(self):
        logging.debug("PlantExtract.__init__()")
        self.xml = None
        self.ped = None

    def parse(self, ped_file):
        """Parse the plant extract document"""
        self.ped = plant_extract_pyxb.CreateFromDocument(
            open(ped_file).read(), location_base=ped_file
        )

        # TODO: sunSpecMetadata
        # TODO: strings
        # TODO: extract extensions
        return

    def __str__(self):
        """Produces a string representation of the Plant Extract envelope"""
        return ''.join(['PlantExtract v:', str(self.ped.v), ' t:', str(self.ped.t),
                        ' seqId:', str(self.ped.seqId), ' lastSeqId:', str(self.ped.lastSeqId)])

    def last(self):
        """Determines if this Plant Extract is the last extract in a set
        """
        return self.ped.seqId == self.ped.lastSeqId

    # TODO: add equivalent sunSpecData convenience methods from ssparser
    # TODO: update logic in following methods to use PyXB functionality
    def get_points(self, model_id):
        """Get all the points for the given model_id"""
        all_points = list()
        for dr in self.ped.d:
            for model in dr.m:
                if model.id == model_id:
                    all_points = all_points.extend(model.p)
        return all_points

    def get_matched_model_points(self, model, point_id):
        """Get a list of sunSpecData points which match the given point_id
        @param point_id:
        @return : points
        """
        points = list()
        logging.info(''.join(["get_matched_model_points() looking for point_id:",
                              str(point_id)]))
        for p in model.p:
            logging.debug(''.join(["get_matched_model_points() p.id:", p.id,
                                   " given point_id:", str(point_id)]))
            if p.id == point_id:
                points.extend(p)

        return points

    def get_matching_points(self, model_id, point_id):
        """Get a list of points which match the given point_id
        @param model_id:
        @param point_id:
        @return : points
        """
        points = list()
        logging.debug(''.join([
            "SunSpecData.get_matching_points() looking for point_id:",
            str(point_id)
        ]))
        for dr in self.ped.d:
            if dr.m is not None:
                for m in dr.m:
                    if m.id == model_id:
                        plist = self.get_matched_model_points(m, point_id)
                        points = points.extend(plist)
        return points

    def get_points_in_period(self, start_time, end_time, model_id,
                             point_id='All'):
        """ Get a Point.time sorted list of points that are between the start_time
            and end_time and that match the point_id.

            If both start_time and end_time are None, then points for the
            sunSpecData block's entire time range is returned.

            Arguments:
            @param start_time: the datetime describing the beginning of the period
            @param end_time: the datetime describing the end of the period
            @param point_id: the id of the Points to retrieve within the period

            @return period_points: points within the period as time sorted
            Points in a list
        """
        logging.info("get_points_in_period: " + str(start_time) +
                     " > " + str(end_time) + " point_id: " + point_id)

        points = list()
        if point_id == 'All':
            points = self.get_points(model_id)
        else:
            points = self.get_matching_points(model_id, point_id)

        period_points = list()
        for p in points:
            if (end_time is None and start_time is None) or \
                    (start_time < p.time < end_time):
                period_points.extend(p)

        logging.info('Period points: ' + str(period_points))
        period_points = sorted(period_points, key=attrgetter('t'))
        return period_points


class ModelIDValues(object):
    # list of convenient model id values
    INVERTER_SINGLE_PHASE = 101
    INVERTER_SPLIT_PHASE = 102
    INVERTER_THREE_PHASE = 103
    METER_SINGLE_PHASE = 201


class PointIDValues(object):
    # list of convenient point ID values
    ENERGY = 'WH'
    TOTAL_ENERGY_EXPORTED = 'TotWhExp'
    TOTAL_ENERGY_IMPORTED = 'TotWhImp'
    POWER = 'W'
    GLOBAL_HORIZONTAL_IRRADIANCE = 'GHI'
    PLANE_OF_ARRAY_IRRADIANCE = 'POAI'
    DIFFUSE_IRRADIANCE = 'DFI'

    FLOAT32 = 'float32'
    INT16 = 'int16'
    UINT16 = 'unint16'
    INT32 = 'int32'
    ACC16 = 'acc16'
    ACC32 = 'acc32'
