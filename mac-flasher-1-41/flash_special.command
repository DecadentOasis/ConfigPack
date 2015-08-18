#!/bin/bash

clear
echo "Okay, let's flash a pusher!"

pushd . > /dev/null
SCRIPT_PATH="${BASH_SOURCE[0]}";
while([ -h "${SCRIPT_PATH}" ]); do
    cd "`dirname "${SCRIPT_PATH}"`"
    SCRIPT_PATH="$(readlink "`basename "${SCRIPT_PATH}"`")";
done
cd "`dirname "${SCRIPT_PATH}"`" > /dev/null
SCRIPT_PATH="`pwd`";
popd  > /dev/null
echo "Running updater in [${SCRIPT_PATH}]"
cd "${SCRIPT_PATH}"

if [ -e /Volumes/MBED ]; then
	echo Detected Early Access PixelPusher.
	cp PixelPusher-EARLY-1-41.bin /Volumes/MBED/
	sync
	diskutil eject MBED
	echo Please reset your PixelPusher.
	exit 0
fi

echo Setting pusher to reflash mode.

echo Please enter your user password so I can get access to the PixelPusher.
# sudo echo Purple > /dev/cu.usbmodem12341
#sleep 1
#sudo dfu-programmer atmega32u4 erase
#sudo dfu-programmer atmega32u4 flash PixelPusher-super-1-3.hex
#sudo dfu-programmer atmega32u4 start
#sleep 1
#sudo echo Orange > /dev/cu.usbmodem12341

echo Here we go:  watch for progress dots!
sudo ./lpc21isp-pp -bin -control ./PixelPusher-1.43-MP-special.bin /dev/cu.usbmodem12341 115200 96000

echo Now power cycle your PixelPusher.

