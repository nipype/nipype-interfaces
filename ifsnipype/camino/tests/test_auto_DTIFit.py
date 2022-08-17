# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..dti import DTIFit


def test_DTIFit_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        bgmask=dict(
            argstr="-bgmask %s",
            extensions=None,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=1,
        ),
        non_linear=dict(
            argstr="-nonlinear",
            position=3,
        ),
        out_file=dict(
            argstr="> %s",
            extensions=None,
            genfile=True,
            position=-1,
        ),
        scheme_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=2,
        ),
    )
    inputs = DTIFit.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DTIFit_outputs():
    output_map = dict(
        tensor_fitted=dict(
            extensions=None,
        ),
    )
    outputs = DTIFit.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value