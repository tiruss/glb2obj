# GLB to OBJ Converter

This script extracts `.glb` files and converts them to `.obj` format using `trimesh`.

## Installation

Before running the script, install the required dependencies:

```bash
pip install trimesh numpy
```

## Usage

Run the script with the following command:

```bash
python glb_extractor.py --glb_file path/to/your_model.glb
```

### Example

```bash
python glb_extractor.py --glb_file sample_model.glb
```

## Output

The converted `.obj` file will be saved in the `output` directory, structured as follows:

```
output/
    your_model_name/
        model.obj
```

The output folder is automatically created based on the `.glb` filename.

## Notes
- This script only extracts the `.obj` model. If you need material (`.mtl`) and texture files, additional processing will be required.
- Ensure the input `.glb` file is valid before running the script.