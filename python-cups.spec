%define module cups
%define _disable_lto 1

Summary:       Python bindings for the CUPS API
Name:          python-%{module}
Version:	2.0.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pycups/pycups-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://cyberelk.net/tim/software/pycups/
BuildRequires:  make
BuildRequires:	cups-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:  python%{pyver}dist(setuptools)

%description
Python bindings for the CUPS API.

%files
%doc COPYING README NEWS TODO
%{py_platsitedir}/cups.cpython-3*.so
%{py_platsitedir}/pycups*.egg-info
%{_rpmconfigdir}/fileattrs/psdriver.attr
%{_rpmconfigdir}/postscriptdriver.prov
#--------------------------------------------------------------------

%prep
%setup -q -n pycups-%{version}
#sed -i 's/_rpmconfigdir/usr/lib/rpm/' Makefile

%build
export CC=%{__cc}
%make CFLAGS="%{optflags} -fno-strict-aliasing"

%py_build

%install
%make_install

%py_install
