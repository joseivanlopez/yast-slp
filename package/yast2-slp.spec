#
# spec file for package yast2-slp
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-slp
Version:        4.0.0
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Group:	        System/YaST
License:        GPL-2.0-or-later
BuildRequires:	gcc-c++ openslp-devel doxygen perl-XML-Writer yast2-core-devel yast2 libtool
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  rubygem(rspec)
%if 0%{?suse_version} < 1220
BuildRequires:  libxcrypt-devel
%endif
Requires:       openslp yast2
Requires:       yast2-ruby-bindings >= 1.0.0

Summary:	YaST2 - SLP Agent and Library
Url: https://github.com/yast/yast-slp

%description
This package provides YaST modules to lookup/advertise services with SLP.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install


%files
%defattr(-,root,root)
%{yast_scrconfdir}/*.scr
%{yast_plugindir}/libpy2ag_slp.so.*
%{yast_plugindir}/libpy2ag_slp.so
%{yast_plugindir}/libpy2ag_slp.la
%{yast_moduledir}/SLP.rb
%{yast_moduledir}/SlpService.rb
%dir %{yast_libdir}/slp
%dir %{yast_libdir}/slp/dialogs
%{yast_libdir}/slp/dialogs/*
%doc %{yast_docdir}
%license COPYING
