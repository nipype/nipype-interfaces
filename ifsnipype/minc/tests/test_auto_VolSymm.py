# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..minc import VolSymm


def test_VolSymm_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        clobber=dict(
            argstr="-clobber",
            usedefault=True,
        ),
        config_file=dict(
            argstr="-config_file %s",
            extensions=None,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fit_linear=dict(
            argstr="-linear",
        ),
        fit_nonlinear=dict(
            argstr="-nonlinear",
        ),
        input_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-3,
        ),
        input_grid_files=dict(),
        nofit=dict(
            argstr="-nofit",
        ),
        output_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            hash_files=False,
            name_source=["input_file"],
            name_template="%s_vol_symm.mnc",
            position=-1,
        ),
        trans_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            hash_files=False,
            keep_extension=False,
            name_source=["input_file"],
            name_template="%s_vol_symm.xfm",
            position=-2,
        ),
        verbose=dict(
            argstr="-verbose",
        ),
        x=dict(
            argstr="-x",
        ),
        y=dict(
            argstr="-y",
        ),
        z=dict(
            argstr="-z",
        ),
    )
    inputs = VolSymm.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_VolSymm_outputs():
    output_map = dict(
        output_file=dict(
            extensions=None,
        ),
        output_grid=dict(
            extensions=None,
        ),
        trans_file=dict(
            extensions=None,
        ),
    )
    outputs = VolSymm.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value