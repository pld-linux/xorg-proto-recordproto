Summary:	Record protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu X i pomocnicze
Name:		xorg-proto-recordproto
Version:	1.13.2
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/recordproto-%{version}.tar.bz2
# Source0-md5:	0ed4706564a34fc2aff724aa16d3ff00
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Record protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu X i pomocnicze.

%package devel
Summary:	Record protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu X i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	recordext

%description devel
Record protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu X i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/recordproto.pc
