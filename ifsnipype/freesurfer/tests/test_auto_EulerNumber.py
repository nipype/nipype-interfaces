# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import EulerNumber


def test_EulerNumber_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-1,
        ),
        subjects_dir=dict(),
    )
    inputs = EulerNumber.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_EulerNumber_outputs():
    output_map = dict(
        defects=dict(),
        euler=dict(),
    )
    outputs = EulerNumber.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
