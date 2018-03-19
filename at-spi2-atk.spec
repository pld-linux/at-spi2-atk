#
# Conditional build:
%bcond_with	static_libs	# static library
#
Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Summary(pl.UTF-8):	Moduł GTK+ łączący ATK z at-spi jako usługą D-Bus
Name:		at-spi2-atk
Version:	2.26.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/at-spi2-atk/2.26/%{name}-%{version}.tar.xz
# Source0-md5:	355c7916a69513490cb83ad34016b169
URL:		https://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	at-spi2-core-devel >= 2.26.0
BuildRequires:	atk-devel >= 1:2.26.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.5
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	atk >= 1:2.26.0
Requires:	at-spi2-core >= 2.26.0
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
Requires:	at-spi2-core-libs >= 2.26.0
Requires:	atk >= 1:2.26.0
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
Requires:	at-spi2-core-devel >= 2.26.0
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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-*/modules/libatk-bridge.la \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%{?with_static_libs:%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-*/module/libatk-bridge.a}

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
%doc AUTHORS NEWS README
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
