# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device suzuran
%define vendor sony

%define vendor_pretty SONY
%define device_pretty E5823, E5803

%define installable_zip 1

%define straggler_files \
/fstab.qcom\
/init.cm.rc\
/init.qcom.rc\
/ueventd.qcom.rc\
/init.qcom.usb.rc\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

