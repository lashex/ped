



class TimeSeriesCalc(object):
    """Time Series calculator that processes Plant Extract Documents' sunSpecData blocks"""

    MIN = 'Minimum'
    MAX = 'Maximum'
    AVG = 'Average'
    SUM = 'Summation'
    
    def __init__(self, ped):
        self.ped = ped
        return
    
    def energy_sum(self, start_time=None, end_time=None):
        sum = None
        if self.ped:
            self.ped.parse_data()
            
            
        return 42
        
    def period_calc(self, start_time, end_time, point_id):
        return 
    
########################
#   command line parsing
if __name__ == '__main__':
    print 'Hello from TimeSeriesCalc'