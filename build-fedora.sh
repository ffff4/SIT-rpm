#!/bin/sh

# Now I know this is going to seem *INSANE* to you. It is.
# Set HOME to $(pwd) so that this repo's .rpmmacros is read
# as though it was in the real $HOME
HOME=$(pwd)
NAME_DISTRIB="fedora"

cd $HOME/MAKE-SPEC
echo "%define DISTR_NAME" $NAME_DISTRIB > DISTR_NAME.txt
cat DISTR_NAME.txt ch1.txt requires-$NAME_DISTRIB.txt ch2.txt icons-$NAME_DISTRIB.txt files-$NAME_DISTRIB.txt postun-$NAME_DISTRIB.txt changelog.txt > simintech-$NAME_DISTRIB.spec
cp simintech-$NAME_DISTRIB.spec $HOME/SPECS
cd $HOME/SPECS
rpmbuild -bb simintech-$NAME_DISTRIB.spec

