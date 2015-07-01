#!/bin/bash

for x in linux*; do if [ $x != linux.sps ]; then rm $x ; fi ; done

export LD_LIBRARY_PATH=/usr/local/lib
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
export GST_PLUGIN_PATH=/usr/lib/gstreamer-0.10

python MakeSpeechProject.py linux linux.sps

python main.py
