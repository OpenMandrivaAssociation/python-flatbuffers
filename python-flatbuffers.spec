Name:		python-flatbuffers
Version:	25.12.19
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/f/flatbuffers/flatbuffers-%{version}.tar.gz
Summary:	The FlatBuffers serialization format for Python
URL:		https://pypi.org/project/flatbuffers/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
The FlatBuffers serialization format for Python

%files
%{py_sitedir}/flatbuffers
%{py_sitedir}/flatbuffers-*.*-info
