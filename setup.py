from setuptools import setup, find_packages

setup(
    name="deepdlncud",
    version="0.0.1",
    keywords=["pip", "deepdlncud"],
    description="deepdlncud",
    long_description="deep learning drug-lncRNA relation",
    license="GPL-3.0",

    url="https://github.com/2003100127/deepdlncud",
    author="Jianfeng Sun",
    author_email="jianfeng.sunmt@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>=3.11,<3.12',
    install_requires=[
        'numpy==1.24.3',
        'tensorflow==2.14',
        'pandas',
        'biopython',
        'pyfiglet',
        'click',
        'rdkit',
    ],
    entry_points={
        'console_scripts': [
            'deepdlncud=deepdlncud.predict:run',
            'deepdlncud_download=deepdlncud.predict:download',
        ],
    }
)