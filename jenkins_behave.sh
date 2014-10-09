#!/bin/bash
BEAM_HOME=$HOME/beam-5.0 PYTHONPATH=$BEAM_HOME/modules/beam-python-5.0/beampy:$PYTHONPATH JAVA_HOME=/usr/lib/jvm/java-7-oracle JDK_HOME=$JAVA_HOME LD_LIBRARY_PATH=$JDK_HOME/jre/lib/amd64/server:$LD_LIBRARY_PATH behave
behave
