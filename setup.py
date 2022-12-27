from distutils.core import setup
import urllib.request

setup(name='SPPD M3rc Tools',
      version='1.0.0',
      description='Tools used by the M3rcenaries SPPD clan',
      author='padawan4330',
      install_requires=['python-dotenv', 'discord', 'pytz', 'gpsoauth', 'requests']
      )

urllib.request.urlretrieve("https://raw.githubusercontent.com/rbrasga/sppd-api"
                           "/a2be0d9d0bce003700887e4a0d50b5835f0b97b4/SPPD_API.py", "SPPD_API.py")

