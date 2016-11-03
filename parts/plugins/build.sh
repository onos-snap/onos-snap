#!/bin/bash

set -e

INSTALLDIR=$1

export ONOS_ROOT=$PWD

tools/build/onos-buck build onos
tar -C $INSTALLDIR --strip-components 1 -zxf buck-out/gen/tools/package/onos-package/onos.tar.gz

