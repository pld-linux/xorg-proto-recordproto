Summary:	Record extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Record
Name:		xorg-proto-recordproto
Version:	1.14
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/recordproto-%{version}.tar.bz2
# Source0-md5:	70f5998c673aa510e2acd6d8fb3799de
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/record*.h
%{_pkgconfigdir}/recordproto.pc
