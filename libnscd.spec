Summary:	Interface to communicate with the nscd daemon
Summary(pl):	Interfejs do komunikowania z demonem nscd
Name:		libnscd
Version:	1.0
Release:	3
License:	LGPL v2.1
Group:		Libraries
# from ftp://ftp.suse.com/pub/suse/i386/9.2/suse/src/libnscd-1.0-2.src.rpm
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	e0346dc277dd5328d759cad9fa3a8327
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides an easy interface for normal programs to
communicate with the nscd daemon from the GNU C Library.

%description -l pl
Ta biblioteka dostarcza ³atwy w u¿yciu interfejs do komunikowania siê
z demonem nscd pochodz±cym z biblioteki GNU C w zwyk³ych programach.

%package devel
Summary:	Header files for libnscd library
Summary(pl):	Pliki nag³ówkowe biblioteki libnscd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnscd library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libnscd.

%package static
Summary:	Static libnscd library
Summary(pl):	Statyczna biblioteka libnscd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnscd library.

%description static -l pl
Statyczna biblioteka libnscd.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libnscd.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnscd.so
%{_libdir}/libnscd.la
%{_includedir}/libnscd.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libnscd.a
