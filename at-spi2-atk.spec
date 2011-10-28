Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Name:		at-spi2-atk
Version:	2.2.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://download.gnome.org/sources/at-spi2-atk/2.2/%{name}-%{version}.tar.xz
# Source0-md5:	19646097aca25a9c1b8ba7ab8d172916
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	at-spi2-core-devel >= 2.2.1
BuildRequires:	atk-devel >= 2.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	at-spi2-core >= 2.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a GTK+ module that bridges ATK to the new D-Bus
based at-spi.

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-*/modules/libatk-bridge.la

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
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop
%{_datadir}/glib-2.0/schemas/org.a11y.atspi.gschema.xml
