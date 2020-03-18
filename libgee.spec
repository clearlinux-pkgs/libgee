#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgee
Version  : 0.20.3
Release  : 9
URL      : https://download.gnome.org/sources/libgee/0.20/libgee-0.20.3.tar.xz
Source0  : https://download.gnome.org/sources/libgee/0.20/libgee-0.20.3.tar.xz
Summary  : The GObject collection library
Group    : Development/Tools
License  : LGPL-2.1
Requires: libgee-data = %{version}-%{release}
Requires: libgee-lib = %{version}-%{release}
Requires: libgee-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)

%description
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%package data
Summary: data components for the libgee package.
Group: Data

%description data
data components for the libgee package.


%package dev
Summary: dev components for the libgee package.
Group: Development
Requires: libgee-lib = %{version}-%{release}
Requires: libgee-data = %{version}-%{release}
Provides: libgee-devel = %{version}-%{release}
Requires: libgee = %{version}-%{release}

%description dev
dev components for the libgee package.


%package lib
Summary: lib components for the libgee package.
Group: Libraries
Requires: libgee-data = %{version}-%{release}
Requires: libgee-license = %{version}-%{release}

%description lib
lib components for the libgee package.


%package license
Summary: license components for the libgee package.
Group: Default

%description license
license components for the libgee package.


%prep
%setup -q -n libgee-0.20.3
cd %{_builddir}/libgee-0.20.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584553487
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1584553487
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgee
cp %{_builddir}/libgee-0.20.3/COPYING %{buildroot}/usr/share/package-licenses/libgee/caeb68c46fa36651acf592771d09de7937926bb3
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gee-0.8.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/gee-0.8.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gee-0.8/gee.h
/usr/lib64/libgee-0.8.so
/usr/lib64/pkgconfig/gee-0.8.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgee-0.8.so.2
/usr/lib64/libgee-0.8.so.2.6.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgee/caeb68c46fa36651acf592771d09de7937926bb3
