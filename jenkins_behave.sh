#!/bin/bash
export BEAM_HOME=$HOME/beam-5.0
export PYTHONPATH=$BEAM_HOME/modules/beam-python-5.0/beampy:$PYTHONPATH
export JAVA_HOME=/usr/lib/jvm/java-7-oracle
export JDK_HOME=$JAVA_HOME
export LD_LIBRARY_PATH=$JDK_HOME/jre/lib/amd64/server:$LD_LIBRARY_PATH
behave
