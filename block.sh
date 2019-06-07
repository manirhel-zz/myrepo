sudo mv /lib/modules/`uname -r`/kernel/drivers/usb/storage/usb-storage.ko.blacklist /lib/modules/`uname -r`/kernel/drivers/usb/storage/usb-storage.ko

sudo modprobe -r usb_storage

sudo modprobe -r uas

sudo mv /lib/modules/`uname -r`/kernel/drivers/usb/storage/usb-storage.ko /lib/modules/`uname -r`/kernel/drivers/usb/storage/usb-storage.ko.blacklist

#@reboot /home/clonezilla/Desktop/block.sh
