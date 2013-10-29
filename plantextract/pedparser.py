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

import logging
import plant_extract

#TODO add sunSpecData convenience methods from ssparser

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
        self.ped = plant_extract.CreateFromDocument(open(ped_file).read(),
                                                    location_base=ped_file)

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

