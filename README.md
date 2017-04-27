# histograph

## Description
Add time markers and see the distribution of frequency versus time. Resolution and bounds are dynamic.

The whole project is just a single, tiny class ```Histograph``` which allows you to create histograms of your data.
Your data consists of timestamps. The resulting histogram will show you how many markers there were at given time.

## Example
``` Python
from histograph import Histograph

# Create the class
h = Histograph()

# Lets put ten markers to the history
for i in range(10):
  marker = h.make_marker(second=i+1)
  h.add_marker(marker)

# Lets add a high spike at second 7
for x in range(5):
  m = h.make_marker(second=7)
  h.add_marker(m)

# Let's generate the histogram for our data
print(h.get_histogram(resolution=10))
```
The result will be:
``` bash
# Notice the spike at seventh second
[1, 1, 1, 1, 1, 1, 6, 1, 1, 1] 
```

## API of Histograph class

### make_marker
``` python 
marker = make_marker(year=1970, month=1, day=1, hour=0, minute=0, second=0)
```
Converts a date and/or time into a marker. The returned marker is a unix timestamp. This function has the granularity of one second. If you need a greater precision in your histogram, then implement your own ```make_marker``` function.

### add_marker
``` python
marker = 3.1415
hist = Histogram()
hist.add_marker(marker)
```
Adds a marker to the histogram. The histograph accepts arbitraty numbers as the value of the marker. When using the ```make_marker``` function, the histograph class has a granularity of one second. If a different precision is needed, use a custom function to make the markers.

### get_histogram
``` python
values = h.get_histogram(resolution=10, first=None, last=None)
```
Returns the histogram data as a list. The number of items in the list is defined by the ```resolution``` parameter. The bounding markers are defined by the ```first``` and ```last``` parameters. 

The histogram data tells you how many marker indices there were in the given time between the ```first``` and ```last``` marker indices. If ```first``` is not given, the histogram will start from the "oldest" one. If ```last``` is not given, it will stop at the last marker.

### get_timespan
``` python
first, last = h.get_timespan()
```
Returns the oldest and youngest markers. This allows you to mark in time the beginning and end of the histogram.

