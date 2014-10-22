AVHRR conversion
----------------

To convert AVHRR L1B data obtained from CLASS archive I am using BEAM software, which has a Python 2.7 API.
To use BEAM one first has to export few shell variables, which are declared in the lib/beam.env

Software prerequisites
----------------------

 * Java JDK. Using Java Oracle JDK 7. (package from webupd8 works just fine)
 * JPY bidirectional Python bridge. See the [docs](http://jpy.readthedocs.org/en/latest/install.html)
 * BEAM. Using BEAM-5.0. beam-python module is installed via VISAT interface or can be just copied from existing beam installation
 * Beam Python Api (beampy). Provided with the BEAM package.

Jenkins settings
----------------
 * use EnvInject module to beampy environment variables
 * software packages should be installed system wide
