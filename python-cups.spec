
%define module cups

Summary:       Python bindings for the CUPS API
Name:          python-%{module}
Version:       1.9.46
Release:       %mkrel 1
Source0:       http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
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
%setup -n pycups-%version

%build
make
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --skip-build --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT
