

from smdx import SMDXPoint as Point

ts_MIN = min  # determine the minimum value over a period of time
ts_MAX = max  # determine the maximum value over a period of time
ts_SUM = sum  # perform a summation over a period of time
def avg(list):
    return sum(list) / float(len(list))

ts_AVG = avg  # determine an average value over a period of time

INSTANT = 'Instantaeous'
BIN = 'Binned'


class TimeSeriesCalc(object):
    """ Time Series calculator that processes Plant Extract Documents'
        sunSpecData blocks
    """

    def __init__(self, ped):
        self.ped = ped
        return

    def energy(self, calc=ts_SUM, start_time=None, end_time=None):
        return self.period_calc(Point.ENERGY, calc, start_time, end_time)

    def energy_exported(self, calc=ts_SUM, start_time=None, end_time=None):
        return self.period_calc(Point.TOTAL_ENERGY_EXPORTED, calc, start_time, end_time)

    def period_calc(self, point_id, calc=ts_SUM, start_time=None, end_time=None):
        if self.ped:
            ssd = self.ped.sunspec_data
            self.ped.parse_data()
            points = ssd.get_points_in_period(start_time, end_time, point_id)
            print ' period calc:', points
        return


########################
#   command line parsing
if __name__ == '__main__':
    print 'Hello from TimeSeriesCalc'
