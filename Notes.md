Mo 11. Aug 13:34:08 CEST 2014
-----------------------------
    DONE: Implemented beampy AVHRR reader and behaviour tests.
          Source beam.env file before running the test suite.
    DONE: implemented an AVHRR converter program
    DONE: request AVHRR data (LAC/GAC/FRAC?)

    TODO: do a quick analysis of different resolutions, 1km vs 4km, how much of information is being lost?
    TODO: define area of interest, create Pyresample areas.cfg file
    TODO: download AMSR2 data
    TODO: resample both to a common grid
    TODO: perform analysis

Do 14. Aug 11:04:06 CEST 2014
-----------------------------
Update:
 * three projects
   -- compare the spatial resolution effects (lac vs gac vs 10k?)
   -- compare the temporal resolution effect (swath vs daily)
   -- get GAC data records


Model evaluation statistics
===========================
    Gathered a set of statistical measures to analyze the experiments
    Use "model evaluation guidelines" search key to find more information
    Natalia Ivanovas paper on 11 Sea Ice Concentration algorithms intercomparison
    is also a good source of information

ICE-ARC report
==============
    Started a TEX report with an outline

CODING
======
    Istjenesten should probably exist as a git sub module in the ICE-ARC folder
    TODO: make istjenesten a stand alone project
    TODO: define areas of interest in the areas.cfg file
