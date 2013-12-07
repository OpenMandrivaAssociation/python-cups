%define module cups

Summary:	Python bindings for the CUPS API
Name:		python-%{module}
Version:	1.9.63
Release:	5
License:	BSD
Group:		Development/Python
Url:		http://cyberelk.net/tim/software/pycups/
Source0:	http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
BuildRequires:	cups-devel
BuildRequires:	pkgconfig(python2)

%description
Python bindings for the CUPS API.

%prep
%setup -qn pycups-%{version}

%build
CFLAGS=-DVERSION=\\\"%{version}\\\" python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%files
%{py_platsitedir}/*.egg-info
%{py_platsitedir}/cups.so
