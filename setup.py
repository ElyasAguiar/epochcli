from setuptools import setup, find_packages

setup(
    name="epochcli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "pytz",
    ],
    entry_points="""
        [console_scripts]
        epochcli=epochcli.cli:app
    """,
    description="Command line tool for timestamp operations",
    author="Elyas Aguiar",
    author_email="elyas.santana98@academico.ifs.edu.br",
)
