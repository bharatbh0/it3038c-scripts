#!/bin/bash 

echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME 
echo Working Dir: $PWD
echo Session Length: $SECONDS
echo Home Dir: $HOME
 
a=$(ip a | grep 'nonprefixroute dynamic ens192' | awk '{print $2}')
echo My IP is $a

