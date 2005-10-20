Summary:	Record protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u X i pomocnicze
Name:		xorg-proto-recordproto
Version:	1.13.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/recordproto-%{version}.tar.bz2
# Source0-md5:	e858fe69ff4ce7bcdaa850d8a3631b17
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Record protocol and ancillary headers.

%description -l pl
Nag��wki protoko�u X i pomocnicze.

%package devel
Summary:	Record protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u X i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	recordext

%description devel
Record protocol and ancillary headers.

%description devel -l pl
Nag��wki protoko�u X i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/recordproto.pc
