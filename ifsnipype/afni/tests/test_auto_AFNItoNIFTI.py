# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import AFNItoNIFTI


def test_AFNItoNIFTI_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        denote=dict(
            argstr="-denote",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            copyfile=False,
            extensions=None,
            mandatory=True,
            position=-1,
        ),
        newid=dict(
            argstr="-newid",
            xor=["oldid"],
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        oldid=dict(
            argstr="-oldid",
            xor=["newid"],
        ),
        out_file=dict(
            argstr="-prefix %s",
            extensions=None,
            hash_files=False,
            name_source="in_file",
            name_template="%s.nii",
        ),
        outputtype=dict(),
        pure=dict(
            argstr="-pure",
        ),
    )
    inputs = AFNItoNIFTI.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_AFNItoNIFTI_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = AFNItoNIFTI.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value