rm -r build
rm -r dist
rm -r onethirtyseven.egg-info

pip uninstall --yes onethirtyseven

python3 setup.py sdist bdist_wheel
pip install dist/onethirtyseven-0.0.1.tar.gz