Name:		python-flatbuffers
Version:	25.12.19
Release:	2
# PyPI publishes a wheel only. The Python sources are the python/ tree
# in the FlatBuffers tag.
Source0:	https://github.com/google/flatbuffers/archive/refs/tags/v%{version}.tar.gz#/flatbuffers-%{version}.tar.gz
Summary:	The FlatBuffers serialization format for Python
URL:		https://pypi.org/project/flatbuffers/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
The FlatBuffers serialization format for Python

%prep
%autosetup -n flatbuffers-%{version} -p1
# setup.cfg points license_files at ../LICENSE, outside the python tree.
sed -i 's|../LICENSE|LICENSE|' python/setup.cfg
cp -a LICENSE python/LICENSE

%build
cd python
%py_build

%install
cd python
%py_install

%files
%{py_sitedir}/flatbuffers
%{py_sitedir}/flatbuffers-*.*-info
