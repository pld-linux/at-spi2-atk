Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Summary(pl.UTF-8):	Moduł GTK+ łączący ATK z at-spi jako usługą D-Bus
Name:		at-spi2-atk
Version:	2.5.90
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/at-spi2-atk/2.5/%{name}-%{version}.tar.xz
# Source0-md5:	9513a6a3a6bed3685bc20a80d1a6ab81
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	at-spi2-core-devel >= 2.4.0
BuildRequires:	atk-devel >= 2.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	at-spi2-core >= 2.4.0
Requires:	atk >= 2.4.0
Requires:	dbus >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a GTK+ module that bridges ATK to the new D-Bus
based at-spi.

%description -l pl.UTF-8
Ten pakiet dostarcza moduł GTK+ łączący ATK z nowym at-spi, opartym o
usługę D-Bus.

%package devel
Summary:	Header files for at-spi2-atk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki at-spi2-atk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for at-spi2-atk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki at-spi2-atk.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-*/modules/libatk-bridge.la \
    $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libatk-bridge.so
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libatk-bridge.so
%attr(755,root,root) %{_libdir}/libatk-bridge-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatk-bridge-2.0.so.0
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop
%{_datadir}/glib-2.0/schemas/org.a11y.atspi.gschema.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatk-bridge-2.0.so
%{_includedir}/at-spi2-atk
%{_pkgconfigdir}/atk-bridge-2.0.pc
