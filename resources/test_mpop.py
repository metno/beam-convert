from mpop.satellites import PolarFactory
from datetime import datetime
import ice_conc
from mpop import scene

gd_dict = {}
hours = range(0, 23)
minutes = range(0, 59)

for i in hours:
    for j in minutes:
        time_slot = datetime(2013, 8, 1, i, j)
        try:
            data = PolarFactory.create_scene('metop', 'M1', 'avhrr', time_slot)
            data.load(['reflec_1'])
            local_data = data.project('istjenesten_main_4k', ['reflec_1'], mode='nearest')
            img = local_data.image.channel_image('reflec_1')
            # import ipdb; ipdb.set_trace()
            img.save('./image_M2_%i%i.png' % (i, j))
            gd_dict['file_%i%i' % (i, j)] = data
        except:
            print i,j, "no m2 file"

# import ipdb; ipdb.set_trace()
global_all = scene.assemble_segments(gd_dict.values())
# 
# from mpop.projector import get_area_def
# from pyresample import plot
# from matplotlib import pyplot
# 
local_data = global_all.project("istjenesten_main_4k", ["reflec_1"], mode="nearest")
img = local_data.image.channel_image('reflec_1')
img.save('./arctic_composite.png')
img.show()
# nh = get_area_def("istjenesten_main_1k")
# pyplot.imshow(local_data['temp_4'].data)
# pyplot.show()
# plot.show_quicklook(nh, local_data['reflec_1'].data, label='cloudFlag')
