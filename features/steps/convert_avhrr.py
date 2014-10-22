import os
from beamsatconvert import convert

@given(u'avhrr l1b file {avhrr_l1b_filepath}')
def step_impl(context, avhrr_l1b_filepath):
    context.avhrr_l1b_filepath = avhrr_l1b_filepath

@then(u'read the input avhrr file')
def step_impl(context):
    input_filename = context.avhrr_l1b_filepath
    context.avhrr_product = convert.read_avhrr_l1b(input_filename)

@then(u'export it as a {output_netcdf4_filepath}')
def step_impl(context, output_netcdf4_filepath):
    convert.write_avhrr_l1b_as_netcdf(context.avhrr_product, output_netcdf4_filepath)
    assert os.path.exists(output_netcdf4_filepath)
    os.remove(output_netcdf4_filepath)
