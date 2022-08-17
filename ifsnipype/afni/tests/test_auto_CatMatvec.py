# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import CatMatvec


def test_CatMatvec_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fourxfour=dict(
            argstr="-4x4",
            xor=["matrix", "oneline"],
        ),
        in_file=dict(
            argstr="%s",
            mandatory=True,
            position=-2,
        ),
        matrix=dict(
            argstr="-MATRIX",
            xor=["oneline", "fourxfour"],
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        oneline=dict(
            argstr="-ONELINE",
            xor=["matrix", "fourxfour"],
        ),
        out_file=dict(
            argstr=" > %s",
            extensions=None,
            keep_extension=False,
            mandatory=True,
            name_source="in_file",
            name_template="%s_cat.aff12.1D",
            position=-1,
        ),
        outputtype=dict(),
    )
    inputs = CatMatvec.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CatMatvec_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = CatMatvec.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
