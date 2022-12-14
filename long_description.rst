=========================================
Neuroimaging in Python: Nipype Interfaces
=========================================
Current neuroimaging software offer users an incredible opportunity to
analyze data using a variety of different algorithms. However, this has
resulted in a heterogeneous collection of specialized applications
without transparent interoperability or a uniform operating interface.
*Nipype*, an open-source, community-developed initiative under the
umbrella of `NiPy <http://nipy.org>`_, is a Python project that provides a
uniform interface to existing neuroimaging software and facilitates interaction
between these packages within a single workflow. Nipype provides an environment
that encourages interactive exploration of algorithms from different
packages (e.g., AFNI, ANTS, BRAINS, BrainSuite, Camino, FreeSurfer, FSL, MNE,
MRtrix, MNE, Nipy, Slicer, SPM), eases the design of workflows within and
between packages, and reduces the learning curve necessary to use different \
packages. Nipype is creating a collaborative platform for neuroimaging \
software development in a high-level language and addressing limitations of \
existing pipeline systems.
*Nipype* allows you to:
* easily interact with tools from different software packages
* combine processing steps from different software packages
* develop new workflows faster by reusing common steps from old ones
* process data faster by running it in parallel on many cores/machines
* make your research easily reproducible
* share your processing workflows with the community