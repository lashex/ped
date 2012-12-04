

from smdx import SMDXPoint


def _minimum(points):
    return min(item.value for item in points)


def _maximum(points):
    return max(item.value for item in points)


def _sum(points):
    return sum(item.value for item in points)


def _avg(points):
    return sum(item.value for item in points) / float(len(points))


def _diff(points):
    minimum = _minimum(points)
    maximum = _maximum(points)
    return maximum - minimum

ts_MIN = _minimum  # determine the minimum value over a period of time
ts_MAX = _maximum  # determine the maximum value over a period of time
ts_SUM = _sum  # perform a summation over a period of time
ts_AVG = _avg  # determine an average value over a period of time
ts_DIFF = _diff  # determine the difference MIN and MAX over period of time

INSTANT = 'Instantaneous'
BIN = 'Binned'


class TimeSeriesCalc(object):
    """ Time Series calculator that processes Plant Extract Documents'
        sunSpecData blocks
    """
    def __init__(self, ped):
        self.ped = ped
        return

    def energy(self, calc=ts_AVG, start_time=None, end_time=None):
        return self.period_calc(SMDXPoint.ENERGY, calc, start_time, end_time)

    def energy_exported(self, calc=ts_AVG, start_time=None, end_time=None):
        return self.period_calc(SMDXPoint.TOTAL_ENERGY_EXPORTED, calc,
                                start_time, end_time)

    def period_calc(self, point_id, calc=ts_AVG, start_time=None, end_time=None):
        if self.ped:
            ssd = self.ped.sunspec_data
            self.ped.parse_data()
            points = ssd.get_points_in_period(start_time, end_time, point_id)
            print ' period points count:', len(points)
            print ' sum of points:'
            print '  ts_SUM:', str(ts_SUM(points))
            print '     sum:', str(sum(p.value for p in points))
            print '  ts_MIN:', ts_MIN(points)
            print '  ts_MAX:', ts_MAX(points)
            print ' ts_DIFF:', str(ts_DIFF(points))
        return calc(points)

#     def ts_sum(self, points):
#         total = 0
#         idx = 0
#         print ' ts_sum.length:' + str(len(points))
#         for p in points:
#             idx = idx + 1
#             print "index:"+str(idx) + " p.value:" + str(p.value)
#             total += p.value
#         return total


########################
#   command line parsing
if __name__ == '__main__':
    print 'Hello from TimeSeriesCalc'
