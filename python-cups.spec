
%define module cups

Summary:       Python bindings for the CUPS API
Name:          python-%{module}
Version:       1.9.57
Release:       %mkrel 1
Source0:       http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
Source1:       http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2.sig
License:       BSD 
Group:         Development/Python
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:           http://cyberelk.net/tim/software/pycups/
%py_requires -d
BuildRequires: cups-devel

%description
Python bindings for the CUPS API.

%files
%defattr(-,root,root)
%{py_platsitedir}/*.egg-info
%{py_platsitedir}/cups.so

#--------------------------------------------------------------------

%prep
%setup -qn pycups-%version

%build
CFLAGS=-DVERSION=\\\"%{version}\\\" python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --skip-build --root=%{buildroot}

%clean
rm -rf %{buildroot}
