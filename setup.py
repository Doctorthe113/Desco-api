from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'descoApi',         # How you named your package folder (MyLib)
    packages = ['descoApi'],   # Chose the same as "name"
    version = '1.0',      # Start with a small number and increase it with every change you make
    license='GNU V3',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Let\'s you use the DESCO api.',   # Give a short description about your library
    long_description= long_description,
    author = 'DoctorThe113',                   # Type in your name
    author_email = 'code.doc113@gmail.com',      # Type in your E-Mail
    url = 'https://github.com/Doctorthe113/Desco-api',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/Doctorthe113/Desco-api/releases/tag/v1.0',    # I explain this later on
    keywords = ['desco', 'descoapi', 'DESCO API'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
            'requests',
        ],
    classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.11',
    ],
)