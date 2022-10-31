"""
 Copyright (c) 2020 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import time
import sys
from pymata4 import pymata4

"""
Setup a pin for dht mode
One pin is set for a dht22 and another for dht11
Both polling and callback are being used in this example.
"""

#
POLL_TIME = 2  # number of seconds between polls

# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3


def the_callback(data):
    """
    A callback function to report data changes.
    This will print the pin number, its reported value and
    the date and time when the change occurred

    :param data: [report_type, pin, dht_type, error_value,
                  humidity, temperature, timestamp]
    """
    pass
#     if not data[3]:
#         tlist = time.localtime(data[6])
#         ftime = f'{tlist.tm_year}-{tlist.tm_mon:02}-{tlist.tm_mday:02} ' \
#                 f'{tlist.tm_hour:02}:{tlist.tm_min:0}:{tlist.tm_sec:02}'
# 
#         print(f'Pin: {data[1]} DHT Type: {data[2]} Humidity:{data[4]}, '
#               f'Temperature: {data[5]} Timestamp: {ftime}')


def dht(my_board, callback=None):
    my_board.set_pin_mode_dht(4, sensor_type=11, differential=.05, callback=callback)
    changed = False
    while True:
        try:
            time.sleep(POLL_TIME)

            # poll the first dht
            value = board.dht_read(4)

            # format the time string and then print the data
            tlist = time.localtime(value[2])
            ftime = f'{tlist.tm_year}-{tlist.tm_mon:02}-{tlist.tm_mday:02} ' \
                    f'{tlist.tm_hour:02}:{tlist.tm_min:0}:{tlist.tm_sec:02}'
            print(f'poll pin 4: humidity={value[0]} temp={value[1]}')
                  #f'time of last report: {ftime}')
           
        except KeyboardInterrupt:
            board.shutdown()
            sys.exit(0)


board = pymata4.Pymata4()

try:
    dht(board, the_callback)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
