Summary:	TDBC driver to access MySQL databases
Summary(pl.UTF-8):	Sterownik TDBC służący do dostępu do baz danych MySQL
Name:		tcl-tdbc-mysql
Version:	1.1.10
Release:	1
License:	Tcl (BSD-like)
Group:		Libraries
Source0:	https://downloads.sourceforge.net/tcl/tdbcmysql%{version}.tar.gz
# Source0-md5:	3530d0fca570eb38235cdc22a3c8540b
URL:		https://wiki.tcl-lang.org/page/MySQL
BuildRequires:	tcl-devel >= 8.6
BuildRequires:	tcl-tdbc-devel >= %{version}
Requires:	tcl >= 8.6
Requires:	tcl-tdbc >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcl TDBC MySQL module is the driver for Tcl Database Connectivity
(TDBC) to access MySQL databases.

%description -l pl.UTF-8
Moduł Tcl TDBC MySQL to sterownik szkieletu Tcl Database Connectivity
(TDBC) służący do dostępu do baz danych MySQL.

%prep
%setup -q -n tdbcmysql%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# internal headers
%{__rm} $RPM_BUILD_ROOT%{_includedir}/{fakemysql,mysqlStubs}.h

# allow dependency generation
chmod 755 $RPM_BUILD_ROOT%{_libdir}/tdbcmysql%{version}/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README license.terms
%dir %{_libdir}/tdbcmysql%{version}
%attr(755,root,root) %{_libdir}/tdbcmysql%{version}/libtdbcmysql%{version}.so
%{_libdir}/tdbcmysql%{version}/*.tcl
%{_mandir}/mann/tdbc_mysql.n*
