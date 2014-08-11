# -*- coding: utf-8 -*-
"""
File: convert_avhrr.py
Author: Mikhail Itkin
Description:
    AVHRR to NetCDF4-CF converter
Usage:
    $ convert_avhrr.py [OPTIONS] <input files>
"""

import os
import argparse
from sys import stdout
from time import sleep
from istjenesten import convert

def make_output_filename(input_filename, suffix=None, output_dir="."):
    basename = os.path.basename(input_filename)
    if suffix is not None:
        suffix = "." + suffix
    output_basename = basename + suffix
    output_filepath = os.path.join(output_dir, output_basename)
    return output_filepath

def process_avhrr_files(input_files, output_dir=None):
    list_length = len(input_files)
    for i, input_filename in enumerate(input_files):
        print "Processing file %i of %i: %s" % (i+1, list_length, input_filename)
        try:
            nc_filepath = make_output_filename(input_filename, suffix="nc", output_dir=output_dir)
            avhrr_product = convert.read_avhrr_l1b(input_filename)
            convert.write_avhrr_l1b_as_netcdf(avhrr_product, nc_filepath)
        except:
            raise

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_avhrr_files",
            help="AVHRR L1B files to be converted to NetCDF4-CF", nargs='+')
    parser.add_argument("-o", "-Output directory")
    args = parser.parse_args()

    input_files = args.input_avhrr_files
    odir = args.o
    process_avhrr_files(input_files, output_dir=odir)

if __name__ == '__main__':
    main()
