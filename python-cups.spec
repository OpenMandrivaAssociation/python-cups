%define module cups

Summary:       Python bindings for the CUPS API
Name:          python-%{module}
Version:       1.9.62
Release:       1
Source0:       http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
Source1:       http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2.sig
License:       BSD 
Group:         Development/Python
Url:           http://cyberelk.net/tim/software/pycups/
BuildRequires: cups-devel

%description
Python bindings for the CUPS API.

%files
%{py_platsitedir}/*.egg-info
%{py_platsitedir}/cups.so

#--------------------------------------------------------------------

%prep
%setup -qn pycups-%{version}

%build
CFLAGS=-DVERSION=\\\"%{version}\\\" python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%changelog
* Thu Jun 16 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.9.57-1mdv2011.0
+ Revision: 685475
- new version
- add sig

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.55-2
+ Revision: 667926
- mass rebuild

* Mon Mar 21 2011 Funda Wang <fwang@mandriva.org> 1.9.55-1
+ Revision: 647211
- new version 1.9.55

* Sat Oct 30 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1.9.49-2mdv2011.0
+ Revision: 590604
- fix build
- patch0: fix "format not a string literal"
- rebuild for new python 2.7

* Mon Mar 15 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.9.49-1mdv2010.1
+ Revision: 519132
- New version

* Tue Jan 19 2010 Frederik Himpe <fhimpe@mandriva.org> 1.9.48-1mdv2010.1
+ Revision: 493843
- update to new version 1.9.48

* Thu Jun 18 2009 Frederik Himpe <fhimpe@mandriva.org> 1.9.46-1mdv2010.0
+ Revision: 387137
- update to new version 1.9.46

* Thu Jan 08 2009 Frederik Himpe <fhimpe@mandriva.org> 1.9.45-1mdv2009.1
+ Revision: 327227
- Update to new version 1.9.45

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 1.9.42-2mdv2009.1
+ Revision: 319436
- rebuild for new python

* Thu Sep 04 2008 Tiago Salem <salem@mandriva.com.br> 1.9.42-1mdv2009.0
+ Revision: 280914
- version 1.9.42

* Tue Jul 15 2008 Funda Wang <fwang@mandriva.org> 1.9.41-1mdv2009.0
+ Revision: 235722
- update to new version 1.9.41

* Sat Jun 21 2008 Funda Wang <fwang@mandriva.org> 1.9.40-1mdv2009.0
+ Revision: 227651
- update to new version 1.9.40

* Fri Jun 13 2008 Tiago Salem <salem@mandriva.com.br> 1.9.39-1mdv2009.0
+ Revision: 218828
- version 1.9.39

* Sat May 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.9.38-2mdv2009.0
+ Revision: 205407
- Fix Spec file
- import python-cups


