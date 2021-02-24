from setuptools import setup

setup(
    name='Options-Analyzer',
    version="1.0",
    author="Varun Pius Rodrigues",
    description="Application to analyze options market and identify best contracts to invest in",
    url="https://github.com/VarunPius/OptionsTechAnalysis",
    install_requires=['requests',],
    packages=['lib'],
    entry_points={
        'console_scripts':['options=run:main']
    },
)
