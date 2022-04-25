import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='rp_scrape',
                 packages=['rp_scrape'],
                 install_requires=install_requires)

