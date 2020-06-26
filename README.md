# k8062

k8062 is a package for interacting with the Velleman K8062 DMX controller.

## Installation

This package is bundled with native drivers. It is only supported on Windows (32/64 bit x86).

```bash
pip install k8062
```

## Usage

```python
import k8062

k8062.start_device() # Start the k8062's driver

k8062.set_channel_count(100) # Set the maximum channel number

k8062.set_data(7, 255) # Set channel 7 to 255

k8062.stop_device() # Stop the driver

```

With the context manager:
```python
import k8062

with k8062.K8062(100) as dmx:
    dmx.set_data(7, 255)

```

## Command Line Usage
```bash
python -m k8062 7 255
```


The context manager takes care of starting and stopping the driver.

## License
MIT