import numpy
import NITLibrary_x64_320_py39 as NIT
from tkinter import messagebox


def main():
    exposure_time, dest_folder, file_name = 100, "c:\\users\\admin\\desktop", "test_file_name"

    try:
        node = NIT.Gige.openByIpAddress("143.185.118.64")
        if node: print("node created via Gige connection")
    except Exception:
        node = NIT.NITManager.getInstance()
        if node: print("node created via USB connection")


    device = None
    device_flag = True

    try:
        node.listDevices()
    except Exception:
        print("node cannot connect to  device")
        # messagebox.showerror("Driver Exception", "No Device detected")
        device_flag = False



    num_of_devices = node.deviceCount()
    if num_of_devices == 0:
        print("no devices connected : device count = "+str(num_of_devices))

    if device_flag:
        device = node.openOneDevice()
    else:
        assert "No valid device reference"

    if device:
        device.setParamValueOf("ExposureTime", exposure_time).updateConfig()
        device.setParamValueOf("OutputType", "RAW").updateConfig()

    snap_ = NIT.NITToolBox.NITSnapshot(dest_folder, file_name, "tiff")

    if snap_:
        snap_.snap(1)
        snap_.disconnect()


if __name__ == "__main__":
    main()
