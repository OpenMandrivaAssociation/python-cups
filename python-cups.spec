%define module cups
%define _disable_lto 1

Summary:       Python bindings for the CUPS API
Name:          python-%{module}
Version:       1.9.73
Release:       4
Source0:       http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
License:       BSD 
Group:         Development/Python
Url:           http://cyberelk.net/tim/software/pycups/
BuildRequires: pkgconfig(python)
BuildRequires: cups-devel
BuildRequires: pkgconfig(python3)

%description
Python bindings for the CUPS API.

%package -n python2-%{module}
Group:         Development/Python
Summary:       Python 2 bindings for the CUPS API

%description -n python2-%{module}
Python 3 bindings for the CUPS API.

%files
%doc COPYING README NEWS TODO
%{py_platsitedir}/cups.cpython-3*.so
%{py_platsitedir}/pycups*.egg-info
%{_rpmhome}/fileattrs/psdriver.attr
%{_rpmhome}/postscriptdriver.prov

%files -n python2-%{module}
%doc COPYING README NEWS TODO
%{python2_sitearch}/cups.so
%{python2_sitearch}/pycups*.egg-info

#--------------------------------------------------------------------

%prep
%setup -q -n pycups-%{version}
sed -i 's/_rpmconfigdir/_rpmhome/' Makefile

cp -a . %{py2dir}

%build
export CC=%{__cc}
%make CFLAGS="%{optflags} -fno-strict-aliasing"

pushd %{py2dir}
CFLAGS="%{optflags}" %{__python2} setup.py build
popd

%install
%makeinstall_std

pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
chmod 755 %{buildroot}%{py_platsitedir}/cups*.so
popd
