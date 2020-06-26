import os
import sys
import ctypes
import importlib.resources

with importlib.resources.path('k8062', 'libs') as p:
    libs_folder_path = p

libs_arch_path = None

if sys.maxsize > 2**32:
    # 64 bit
    libs_arch_path = os.path.join(libs_folder_path, '64')
else:
    # 32 bit
    libs_arch_path = os.path.join(libs_folder_path, '32')

os.environ['PATH'] = libs_arch_path + os.pathsep + os.environ['PATH']

lib_path = os.path.abspath(os.path.join(libs_arch_path, 'K8062D.dll'))

lib = ctypes.CDLL(lib_path)


def start_device() -> None:
    """
    Starts the k8062 driver.
    """
    lib.StartDevice()

def stop_device() -> None:
    """
    Stops the k8062 driver.
    """
    lib.StopDevice()

def set_data(channel: int, value: int) -> None:
    """
    Sets the specified channel to the specified value.

    Parameters:
    channel (int): The channel to control
    value (int [0-255]): The value to set    
    """
    lib.SetData(channel, value)

def set_channel_count(count: int) -> None:
    """
    Sets the maximum channel used.

    Parameters:
    count (int): The highest channel number desired
    """
    lib.SetChannelCount(count)

class K8062():
    def __init__(self, channel_count=100):
        self.channel_count = channel_count

    def __enter__(self):
        start_device()
        set_channel_count(self.channel_count)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        stop_device()

    def set_data(self, channel: int, value: int) -> None:
        """
        Sets the specified channel to the specified value.

        Parameters:
        channel (int): The channel to control
        value (int [0-255]): The value to set    
        """
        set_data(channel, value)

    def set_channel_count(self, count: int) -> None:
        """
        Sets the maximum channel used.

        Parameters:
        count (int): The highest channel number desired
        """
        set_channel_count(count)
