from setuptools import setup, find_packages

setup(
    name="deepdlncud",
    # version="0.0.1",
    version="0.0.0.0.1",
    keywords=("pip", "deepdlncud"),
    description="deepdlncud",
    long_description="deep learning drug-lncRNA relation",
    license="MIT",

    url="https://github.com/2003100127",
    author="Jianfeng Sun",
    author_email="jianfeng.sunmt@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>3.6',
    install_requires=[
        'pandas==1.3.5',
        'numpy==1.19.5',
        'biopython==1.79',
        'pyfiglet==0.8.post1',
        'click==8.1.3',
        # 'rdkit-pypi==2022.3.2',
        # 'tensorflow-gpu==2.6.0',
    ],
    entry_points={
        'console_scripts': [
            'deepdlncud=deepdlncud.Main:main',
            'deepdlncud_download=deepdlncud.Main:download',
        ],
    }
)