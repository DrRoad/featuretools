from setuptools import find_packages, setup
from setuptools.command.build_ext import build_ext as _build_ext


# Bootstrap numpy install
class build_ext(_build_ext):

    def finalize_options(self):
        _build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())


setup(
    name='featuretools',
    version='0.3.0',
    packages=find_packages(),
    package_data={'featuretools': ['config.yaml']},
    description='a framework for automated feature engineering',
    url='http://featuretools.com',
    license='BSD 3-clause',
    author='Feature Labs, Inc.',
    author_email='support@featurelabs.com',
    classifiers=[
         'Development Status :: 3 - Alpha',
         'Intended Audience :: Developers',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.5',
         'Programming Language :: Python :: 3.6'
    ],
    install_requires=open('requirements.txt').readlines(),
    setup_requires=open('setup-requirements.txt').readlines(),
    python_requires='>=2.7, <4',
    cmdclass={'build_ext': build_ext},
    test_suite='featuretools/tests',
    tests_require=open('test-requirements.txt').readlines(),
    keywords='feature engineering data science machine learning',
    include_package_data=True
)
