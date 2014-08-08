import os
from istjenesten.convert import Converter

@given(u'avhrr l1b file {avhrr_l1b_filepath}')
def step_impl(context, avhrr_l1b_filepath):
    context.avhrr_l1b_filepath = avhrr_l1b_filepath

@then(u'read the input avhrr file')
def step_impl(context):
    input_filename = context.avhrr_l1b_filepath
    context.avhrr_product = Converter.read_avhrr_l1b(input_filename)

@then(u'export it as a {output_netcdf4_filepath}')
def step_impl(context, output_netcdf4_filepath):
    context.avhrr_product.save_product(output_netcdf4_filepath, 'NetCDF4-CF')
    assert os.path.exists(output_netcdf4_filepath)
