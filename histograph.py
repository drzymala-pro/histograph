#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import math
import datetime


class Histograph():

    def __init__(self):
        self.db = {}
        self.first = None
        self.last  = None

    def add_marker(self, marker):
        self.db[marker] = self.db.get(marker, 0) + 1
        self.first = marker if self.first is None else min(self.first, marker)
        self.last  = marker if self.last  is None else max(self.last,  marker)

    def get_timespan(self):
        return self.first, self.last

    def get_histogram(self, resolution=10, first=None, last=None):
        if resolution < 1 or type(resolution) is not int:
            # In such case cannot create histogram
            raise Exception('Invalid resolution')
        first = first if first is not None else self.first
        last  = last  if last  is not None else self.last
        if first is None or last is None:
            # No markers, histogram will be empty.
            return [0 for x in range(resolution)]
        timespan = abs(last - first)
        timestep = timespan / resolution
        result = []
        if timespan == 0:
            # If the time range is a sinlge point, redistribute the value
            total = self.db[first] if first in self.db.keys() else 0
            for index in range(resolution):
                chunk = math.ceil(total / (resolution - index))
                total -= chunk
                result.append(chunk)
            return result
        else:
            # For every point in the graph
            for index in range(resolution):
                # Get all of the values from the corresponding time range
                begin = first + (index * timestep)
                # This is to overcome the "near zero" problem in floats.
                end = last - ((resolution - (index+1)) * timestep)
                if index == 0:
                    # This is the first data point - Include the left-most and right-most marker.
                    values = [self.db[marker] for marker in self.db.keys() if marker >= begin and marker <= end]
                else:
                    # Do not include the left-most marker. It was already included in the last data point.
                    values = [self.db[marker] for marker in self.db.keys() if marker > begin and marker <= end]
                result.append(sum(values))
            return result

    def make_marker(self, year, month, day, hour, minute, second):
        microsecond = 0
        timezone = datetime.timezone(datetime.timedelta())
        return int(datetime.datetime(year, month, day, hour, minute, second, microsecond, timezone).timestamp())




