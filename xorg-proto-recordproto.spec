Summary:	Record extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Record
Name:		xorg-proto-recordproto
Version:	1.14.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/recordproto-%{version}.tar.bz2
# Source0-md5:	24541a30b399213def35f48efd926c63
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-sgml-doctools >= 1.5
BuildRequires:	xorg-util-util-macros >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Record extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia Record.

%package devel
Summary:	Record extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Record
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	recordext

%description devel
Record extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia Record.

%prep
%setup -q -n recordproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README specs/*.{html,css}
%{_includedir}/X11/extensions/record*.h
%{_pkgconfigdir}/recordproto.pc
