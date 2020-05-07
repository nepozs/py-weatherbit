from distutils.core import setup
setup(
  name = 'py-weatherbit',
  packages = ['py-weatherbit'],
  version = '0.1',
  license='MIT',
  description = 'Python Wrapper for Weatherbit API', 
  author = 'Bjarne Riis',
  author_email = 'bjarne@briis.com',
  url = 'https://github.com/briis/py-weatherbit',
#   download_url = 'https://github.com/briis/py-weatherbit/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Weatherbit', 'Forecast', 'Python'],
  install_requires=[
          'asyncio',
          'logging',
          'typing',
          'aiohttp',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)