#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Summary(pl.UTF-8):	Moduł GTK+ łączący ATK z at-spi jako usługą D-Bus
Name:		at-spi2-atk
Version:	2.38.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/at-spi2-atk/2.38/%{name}-%{version}.tar.xz
# Source0-md5:	aed95be54ef213d210331dda88298b92
URL:		https://wiki.linuxfoundation.org/accessibility/d-bus
BuildRequires:	at-spi2-core-devel >= 2.34.0
BuildRequires:	atk-devel >= 1:2.36.0
BuildRequires:	dbus-devel >= 1.5
BuildRequires:	glib2-devel >= 1:2.32.0
# for tests only
#BuildRequires:	libxml2-devel >= 1:2.9.1
BuildRequires:	meson >= 0.40.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	atk >= 1:2.36.0
Requires:	at-spi2-core >= 2.34.0
Requires:	dbus >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a GTK+ module that bridges ATK to the new D-Bus
based at-spi.

%description -l pl.UTF-8
Ten pakiet dostarcza moduł GTK+ łączący ATK z nowym at-spi, opartym o
usługę D-Bus.

%package libs
Summary:	Shared atk-bridge library
Summary(pl.UTF-8):	Biblioteka współdzielona atk-bridge
Group:		Libraries
Requires:	at-spi2-core-libs >= 2.34.0
Requires:	atk >= 1:2.36.0
Requires:	dbus-libs >= 1.5
Requires:	glib2 >= 1:2.32.0
Conflicts:	at-spi2-atk < 2.6.0-2

%description libs
Shared atk-bridge library, providing ATK/D-Bus bridge.

%description libs -l pl.UTF-8
Biblioteka współdzielona atk-bridge, zapewniająca pomost między ATK a
D-Bus.

%package devel
Summary:	Header files for atk-bridge library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki atk-bridge
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	at-spi2-core-devel >= 2.34.0
Requires:	glib2-devel >= 1:2.32.0

%description devel
Header files for atk-bridge library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki atk-bridge.

%package static
Summary:	Static atk-bridge library
Summary(pl.UTF-8):	Biblioteka statyczna atk-bridge
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static atk-bridge library.

%description static -l pl.UTF-8
Biblioteka statyczna atk-bridge.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libatk-bridge.so
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop

%files libs
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libatk-bridge-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatk-bridge-2.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatk-bridge-2.0.so
%{_includedir}/at-spi2-atk
%{_pkgconfigdir}/atk-bridge-2.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libatk-bridge-2.0.a
%endif
