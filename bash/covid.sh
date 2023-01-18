#!/bin/bash
#This script downloads covid data and displays it

#Set positive value to variable 
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')

NEGATIVE=$(echo $DATA | jq '.[0].negative')


PENDING=$(echo $DATA | jq '.[0].pending')

inIcuCumulative=$(echo $DATA | jq '.[0].inIcuCumulative')
#Set date variable 
TODAY=$(date)
echo "ON $TODAY, there were $POSITIVE positive COVID cases, there were $NEGATIVE negative COVID cases, there were $PENDING pending COVID cases,there were $inIcuCumulative inIcuCumulative COVID cases"

