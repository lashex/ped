from distutils.core import setup

setup(name='pyped',
      version='0.5',
      description='Python Plant Extract Document processor',
      author='Brett Francis',
      package_dir = {'': ''},
      py_modules=['plant_extract','smdx.smdx'],
      data_files=[('smdx-xml', ['smdx/files/smdx_00001.xml', 'smdx/files/smdx_00002.xml',
                                'smdx/files/smdx_00010.xml', 'smdx/files/smdx_00011.xml',
                                'smdx/files/smdx_00012.xml', 'smdx/files/smdx_00013.xml',
                                'smdx/files/smdx_00014.xml', 'smdx/files/smdx_00015.xml',
                                'smdx/files/smdx_00016.xml', 'smdx/files/smdx_00017.xml',
                                'smdx/files/smdx_00018.xml', 'smdx/files/smdx_00019.xml',
                                ...]),
                  ('smdx-xsd', ['smdx/files/smdx.xsd'])],
      )