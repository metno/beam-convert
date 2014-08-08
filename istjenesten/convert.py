import beampy

def read_avhrr_l1b(filepath, driver='beam'):
    """
    Read in AVHRR L1B files obtained from CLASS archive

    :param filepath:
        :py.string: input filepath
    :param driver:
        driver defines which framework to use for IO
    """
    if driver is 'beam':
        return read_avhrr_l1b_with_beam(filepath)
    else:
        pass

def read_avhrr_l1b_with_beam(filepath):
    """
    Read in AVHRR L1B files using BEAM
    :param filepath:
        :py.string: input filepath
    """
    product = beampy.ProductIO.readProduct(filepath)
    return product

def write_avhrr_l1b_as_netcdf(product, output_filepath, driver='beam'):
    """
    Write out AVHRR dat as netcdf
    
    :param product:
        object that contains satellite information
    :param output_filepath:
        :py.string: output filepath
    :param driver:
        driver defines which framework to use for IO
    """
    if driver is 'beam':
        print "Driver: ", driver
        beampy.ProductIO.writeProduct(product, output_filepath, 'NetCDF4-CF')
    else:
        pass
