
%define module cups

Summary:       Python bindings for the CUPS API
Name:          python-%{module}
Version:       1.9.49
Release:       %mkrel 2
Source0:       http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
Patch0:	       pycups-1.9.49-fix-printf-format.patch
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
%patch0 -p1 -b .printf

%build
CFLAGS=-DVERSION=\\\"%{version}\\\" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --skip-build --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT
