

from smdx.smdx import SMDXPoint as Point

MIN = 'Minimum'  # determine the minimum value over a period of time
MAX = 'Maximum'  # determine the maximum value over a period of time
AVG = 'Average'  # determine an average value over a period of time
SUM = 'Summation'  # perform a summation over a period of time

INSTANT = 'Instantaeous'
BIN = 'Binned'


class TimeSeriesCalc(object):
    """ Time Series calculator that processes Plant Extract Documents'
        sunSpecData blocks
    """

    def __init__(self, ped):
        self.ped = ped
        return

    def energy_exported_sum(self, start_time=None, end_time=None):
        sum = None
        if self.ped:
            self.ped.parse_data()
            self.period_calc(Point.TOTAL_ENERGY_EXPORTED, SUM, start_time, end_time)
        return 42

    def period_calc(self, point_id, calc=AVG, start_time=None, end_time=None):
        ssd = self.ped.sunspec_data
        points = ssd.get_points_in_period(point_id, start_time, end_time)
        return

########################
#   command line parsing
if __name__ == '__main__':
    print 'Hello from TimeSeriesCalc'
