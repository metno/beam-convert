Feature: Convert NOAA CLASS AVHRR L1B files to NetCDF format
    As a user of istjenesten
    When I process AVHRR data using beampy
    I receive NetCDF4 files

    Scenario Outline: GAC files
        Given avhrr l1b file <avhrr_l1b_filepath>
        Then read the input avhrr file
        Then export it as a <output_netcdf4_filepath> 
        Examples:
            | avhrr_l1b_filepath | output_netcdf4_filepath |
            | test_data/L1B/AVHRR/NSS.GHRR.M2.D13212.S2237.E0020.B3519495.SV | test_data/L1B/AVHRR/NSS.GHRR.M2.D13212.S2237.E0020.B3519495.SV.nc |
