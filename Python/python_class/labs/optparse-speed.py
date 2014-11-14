from optparse import OptionParser
distance_from_sf = {'Albany':2953,
                    'Detroit': 2411,
                    'New York': 2944,
                    'Atlanta':	2503,
                    'Baltimore': 2837,
                    'Orlando': 2836,
                    'Houston':	1941,
                    'Philadelphia': 2894,
                    'Phoenix': 725}

if __name__ == "__main__":
    p = OptionParser(description="Calculate the time in hours to travel "
                                 "from San Francisco to major US Cities.",
                     usage="[options] destination")
    p.add_option('-s', '--speed', action='store',
                 type='int', dest='speed',
                 help='Speed in MPH.')
    p.set_defaults(speed=60)
    options, args = p.parse_args()


    
