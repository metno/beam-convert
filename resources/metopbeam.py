"""Loader for metop avhrr, netcdf beam format.
"""

from ConfigParser import ConfigParser
from mpop import CONFIG_PATH
import os
import numpy

from netCDF4 import Dataset


def load(satscene):
    """Load avhrr data.
    """

    # Read config file content
    conf = ConfigParser()
    conf.read(os.path.join(CONFIG_PATH, satscene.fullname + ".cfg"))
    values = {"orbit": satscene.orbit,
              "satname": satscene.satname,
              "number": satscene.number,
              "instrument": satscene.instrument_name,
              "satellite": satscene.fullname
              }

    print values

    # import ipdb; ipdb.set_trace()
    filename = os.path.join(
        conf.get("avhrr-level1b", "dir"),
        satscene.time_slot.strftime(conf.get("avhrr-level1b",
                                             "filename",
                                             raw=True)) % values)

    print filename
    # Load data from netCDF file
    ds = Dataset(filename, 'r')

    for chn_name in satscene.channels_to_load:
        # Read variable corresponding to channel name
        data = ds.variables[chn_name][:]
        madata = numpy.ma.array(data, mask = data != data)
        satscene[chn_name] = madata

    lons = ds.variables['longitude'][:]
    lats = ds.variables['latitude'][:]

    # Set scene area as pyresample geometry object
    try:
        from pyresample import geometry
        satscene.area = geometry.SwathDefinition(lons=lons, lats=lats)
    except ImportError:
        # pyresample not available. Set lon and lats directly
        satscene.area = None
        satscene.lat = lons
        satscene.lon = lats
