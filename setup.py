from setuptools import setup

setup(name='GLαDOS',
      version='1.0',
      description='General Lookup of α-Decay for Optimised Search (GLαDOS)',
      url='https://github.com/Yottaphy/GL-DOS',
      author='Jorge Romero',
      author_email='joromero@jyu.fi',
      license='GPL-3.0',
      packages=['glados'],
      install_requires=[
          'argparse',
      ],
      zip_safe=False,
      entry_points={
        'console_scripts': [
            'glados = glados:main'
        ]},
    )