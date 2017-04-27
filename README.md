# histograph
## Description
Add time markers and see the distribution of frequency versus time. Resolution and bounds are dynamic.

The whole project is just a single, tiny class ```Histograph``` which allows you to create histograms of your data.
Your data consists of timestamps. The resulting histogram will show you how many markers there were at given time.

## Example

``` Python3
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
``` [1, 1, 1, 1, 1, 1, 6, 1, 1, 1] ```

