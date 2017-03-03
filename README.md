# steamspy-ruby [![Build Status](https://travis-ci.org/rbarysas/steamspy-ruby.svg?branch=master)](https://travis-ci.org/rbarysas/steamspy-ruby)

A Python interface to the [SteamSpy](https://steamspy.com/) API.

### Usage

```python
import ss from steamspy

# Get application details
d = ss.appdetails(730)
d.status # => 200
d.data   # => {...}

# Get games in genre
d = ss.genre("Early Access")

# Get top 100 games by players in the last two weeks
d = ss.top100in2weeks

# Get top 100 games by players since March 2009
d = ss.top100forever

# Get top 100 games by owners
d = ss.top100owned

# Get all games with owners data sorted by owners
d = ss.all
```

More information about API could be found in the [official website](https://steamspy.com/api.php).

### License

The SteamSpy python module is released under the MIT license.
