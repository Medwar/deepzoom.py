# What is added in this fork:
- webp support
- Pillow 11 support
- option of sharpening after downscaling


# deepzoom.py: Python Deep Zoom Tools

## Installation

```bash
git clone https://github.com/Mindat-org/deepzoom.py.git
cd deepzoom.py
python setup.py install
```

## Development

Install for local development:

```
python3 -m pip install -e .
```

## Example

```bash
cd examples/helloworld/

# Single image (DZI)
./helloworld-dzi.py

# Collection (DZC)
./helloworld-dzc.py
```

## Acknowledgements

Initially developed by [Kapil Thangavelu](mailto:kapil.foss@gmail.com).
Powered by [OpenZoom][].

## License

Licensed under the [New BSD Licence][bsd].

[bsd]: http://www.opensource.org/licenses/bsd-license.php
[openzoom]: http://openzoom.org
[pil]: http://www.pythonware.com/products/pil
[pillow]: https://pillow.readthedocs.io/en/stable/installation.html#basic-installation
