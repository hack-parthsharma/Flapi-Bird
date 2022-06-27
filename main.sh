#!/bin/bash

# resetting the screen
clear

echo "                          .   .       "
echo "                          | \/|       "
echo "  (\   _                  ) )|/|      "
echo "      (/            _----. /.'.'      "
echo ".-._________..      .' @ _\  .'              Welcome to..."
echo "'.._______.   '.   /    (_| .')       the one and only,"
echo "  '._____.  /   '-/      | _.'                the legendary,"
echo "   '.______ (         ) ) \           "
echo "     '..____ '._       )  )           "
echo "        .' __.--\  , ,  // ((         The Flapi"
echo "        '.'     |  \/   (_.'(         Birb Game!"
echo "                '   \ .'              "
echo "                 \   (                "
echo "                  \   '.              "
echo "  Author: Tanishq  \ \ '.)            Build Time: 7H"
echo "     Chaudhary      '-'-'             (mostly for the config file XD)"

echo -e "\n\nMain Menu: "
echo -e "\t001. Play Yourself"
echo -e "\t002. See NEAT in action"
echo -e "\tany. Exit"

while [ true ]
do
    echo -ne "\n\nEnter Your Choice: "
    read input

    if [[ $input == '1' ]]
    then
        python Game/play.py
    elif [[ $input == '2' ]]
    then
        python Game/NEATplay.py
    else
        break
    fi
done

