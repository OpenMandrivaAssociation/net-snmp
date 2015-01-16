# not really needed anymore, but leaving for just incase legacy issues
#define _requires_exceptions devel(libperl
%define _disable_ld_no_undefined 1
%define Werror_cflags %{nil}

%define major	30
%define libname %mklibname netsnmp %{major}
%define libagent %mklibname netsnmpagent %{major}
%define libhelpers %mklibname netsnmphelpers %{major}
%define libmibs %mklibname netsnmpmibs %{major}
%define libtrapd %mklibname netsnmptrapd %{major}
%define libsnmp %mklibname snmp %{major}
%define devname %mklibname -d net-snmp

# (oe) never enable rpm support as it eats file descriptors like crazy 
# casuing the snmp daemon to die!.
%define build_rpm	0
%{?_without_rpm:	%global build_rpm 0}
%{?_with_rpm:		%global build_rpm 1}

Summary:	A collection of SNMP protocol tools and libraries
Name:		net-snmp
Version:	5.7.2
Release:	15
License:	BSDish
Group:		System/Servers
Url:		http://www.net-snmp.org/
Source0:	http://prdownloads.sourceforge.net/net-snmp/net-snmp-%{version}.tar.gz
Source1:	http://prdownloads.sourceforge.net/net-snmp/net-snmp-%{version}.tar.gz.asc
Source2:	snmpd.conf
Source3:	snmpd.logrotate
Source4:	snmpd.sysconfig
Source5:	snmpd.service
Source6:	snmptrapd.conf
Source7:	snmptrapd.logrotate
Source8:	snmptrapd.sysconfig
Source9:	snmptrapd.service
Source10:	net-snmp.tmpfiles
Source11:	ucd5820stat
Source12:	NOTIFICATION-TEST-MIB.txt
Source13:	TRAP-TEST-MIB.txt

# fedora patches
Patch1:		net-snmp-5.7.2-pie.patch
Patch2:		net-snmp-5.5-dir-fix.patch
Patch3:		net-snmp-5.6-multilib.patch
Patch5:		net-snmp-5.5-apsl-copying.patch
Patch7:		net-snmp-5.6-test-debug.patch
Patch8:		net-snmp-5.7.2-systemd.patch

# other patches
Patch100:	net-snmp-5.6.1-add-pythoninstall-destdir.patch
Patch101:	net-snmp-5.7.2-python3.patch

BuildRequires:	chrpath
BuildRequires:	lm_sensors-devel
BuildRequires:	mariadb-devel
BuildRequires:	perl-devel
BuildRequires:	tcp_wrappers-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
%if %{build_rpm}
BuildRequires:	pkgconfig(rpm)
%endif
Requires(pre,postun): rpm-helper
Requires:	net-snmp-mibs
Requires:	net-snmp-utils
Requires:	tcp_wrappers

%description
SNMP (Simple Network Management Protocol) is a protocol used for network
management. The NET-SNMP project includes various SNMP tools: an extensible
agent, an SNMP library, tools for requesting or setting information from SNMP
agents, tools for generating and handling SNMP traps, a version of the netstat
command which uses SNMP, and a Tk/Perl mib browser. This package contains the
snmpd and snmptrapd daemons, documentation, etc.

You will probably also want to install the net-snmp-utils package, which
contains NET-SNMP utilities.

%package -n	%{libname}
Summary:	Library for Network management (SNMP), from the NET-SNMP project
Group:		System/Libraries

%description -n	%{libname}
This package contains the %{name} library for use with NET-SNMP
project's network management tools.

%package -n	%{libagent}
Summary:	Library for Network management %{name}-agent
Group:		System/Libraries

%description -n	%{libagent}
This package contains the %{name}-agent library for use with NET-SNMP
project's network management tools.

%package -n	%{libhelpers}
Summary:	Library for Network management %{name}-helpers
Group:		System/Libraries

%description -n	%{libhelpers}
This package contains the %{name}-helpers library for use with NET-SNMP
project's network management tools.

%package -n	%{libmibs}
Summary:	Library for Network management %{name}-mibs
Group:		System/Libraries

%description -n	%{libmibs}
This package contains the %{name}-mibs library for use with NET-SNMP
project's network management tools.

%package -n	%{libtrapd}
Summary:	Library for Network management %{name}-trapd
Group:		System/Libraries

%description -n	%{libtrapd}
This package contains the %{name}-trapd library for use with NET-SNMP
project's network management tools.

%package -n	%{libsnmp}
Summary:	Library for Network management snmp
Group:		System/Libraries

%description -n	%{libsnmp}
This package contains the snmp library for use with NET-SNMP
project's network management tools.

%package -n	%{devname}
Summary:	The development environment for the NET-SNMP project
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libagent} = %{version}-%{release}
Requires:	%{libhelpers} = %{version}-%{release}
Requires:	%{libmibs} = %{version}-%{release}
Requires:	%{libtrapd} = %{version}-%{release}
Requires:	%{libsnmp} = %{version}-%{release}

%description -n	%{devname}
The %{devname} package contains the development libraries and header
files for use with the NET-SNMP project's network management tools.

Install the net-snmp-devel package if you would like to develop applications
for use with the NET-SNMP project's network management tools.

%package	utils
Summary:	Network management utilities using SNMP, from the NET-SNMP project
Group:		Networking/Other
Requires:	openssl
Requires:	net-snmp-mibs

%description	utils
The net-snmp package contains various utilities for use with the NET-SNMP
network management project.

Install this package if you need utilities for managing your network using the
SNMP protocol.

%package	tkmib
Summary:	MIB browser in TK
Group:		Networking/Other
Requires:	net-snmp-mibs
Requires:	perl(SNMP)

%description	tkmib
MIB browser in TK

%package	mibs
Summary:	MIBs for the NET-SNMP project
Group:		Networking/Other

%description	mibs
The net-snmp-mibs package contains various MIBs for use with the NET-SNMP
network management project.

%package	trapd
Summary:	The trap collecting daemon for %{name}
Group:		System/Servers
Requires(pre,postun): rpm-helper
Requires:	%{name} = %{version}
Requires:	openssl
Requires:	net-snmp-mibs
Requires:	net-snmp-utils
Requires:	tcp_wrappers

%description	trapd
The net-snmp-trapd package contains the trap collecting daemon for use with the
NET-SNMP network management project.

Install this package if you need to collect SNMP traps from your network using
the SNMP protocol.

%package -n	perl-NetSNMP
Summary:	Perl utilities using SNMP, from the NET-SNMP project
Group: 		Development/Perl
Requires:	%{name} = %{version}
Requires:	net-snmp-mibs
Requires:	net-snmp-utils

%description -n	perl-NetSNMP
NET SNMP (Simple Network Management Protocol) Perl5 Support The Simple Network
Management Protocol (SNMP) provides a framework for the exchange of management
information between agents (servers) and clients.  The NET SNMP perl5 support
files provide the perl functions for integration of SNMP into applications,
written in perl.

%package -n	python-netsnmp
Summary:	Python utilities using SNMP, from the NET-SNMP project
Group: 		Development/Python
Requires:	%{name} = %{version}
Requires:	net-snmp-mibs
Requires:	net-snmp-utils

%description -n	python-netsnmp
The 'netsnmp' module provides a full featured, tri-lingual SNMP (SNMPv3, 
SNMPv2c, SNMPv1) client API. The 'netsnmp' module internals rely on the
Net-SNMP toolkit library.

%prep
%setup -q
%apply_patches

# run tests in dir that is cleaned
install -d -m777 test_tmp_dir
HERE="%{_builddir}/%{name}-%{version}"
perl -pi -e "s|/tmp/snmp-test|$HERE/test_tmp_dir/snmp-test|g" testing/*

# Do this patch with a perl hack...
perl -pi -e "s|'\\\$install_libdir'|'%{_libdir}'|" ltmain.sh

bzip2 ChangeLog

%build
%serverbuild

MIBS="host agentx smux \
	ucd-snmp/diskio tcp-mib udp-mib mibII/mta_sendmail \
	ip-mib/ipv4InterfaceTable ip-mib/ipv6InterfaceTable \
	ip-mib/ipAddressPrefixTable/ipAddressPrefixTable \
	ip-mib/ipDefaultRouterTable/ipDefaultRouterTable \
	ip-mib/ipv6ScopeZoneIndexTable ip-mib/ipIfStatsTable \
	sctp-mib rmon-mib etherlike-mib \
	ucd-snmp/lmsensorsMib"

%configure2_5x \
%if %{build_rpm}
	--with-rpm \
%else
	--without-rpm \
%endif
	--disable-static \
	--enable-shared \
	--sysconfdir=%{_sysconfdir} \
	--enable-ipv6 \
	--enable-ucd-snmp-compatibility \
	--enable-embedded-perl \
	--with-python-modules \
	--enable-as-needed \
	--with-pic \
	--with-cflags="$CFLAGS -D_REENTRANT" \
	--with-ldflags="$LDFLAGS -lcrypto -lsensors" \
	--with-logfile="/var/log/snmpd.log" \
	--with-persistent-directory="/var/lib/net-snmp" \
	--with-mib-modules="$MIBS" \
	--with-libwrap \
	--with-openssl \
	--with-perl-modules="INSTALLDIRS=vendor" \
	--with-mnttab="/etc/mtab" \
	--with-mysql \
	--with-default-snmp-version="3" \
	--with-sys-location="Unknown" \
	--with-sys-contact="root@localhost" <<EOF

EOF

# XXX autojunk
sed -i -e "s,^#define HAVE_GETMNTENT,#define HAVE_GETMNTENT 1," \
	include/net-snmp/net-snmp-config.h

make

# more verbose tests
#perl -pi -e "s|\./RUNTESTS|\./RUNTESTS -V|g" testing/Makefile
# XXX - andreas - 15/aug/2006
# XXX - disabled because doesn't work on cluster
# and available bandwidth is TOO LOW for interactive debugging from
# 10.000km away
#make test

%install
#seems to be errors with parallel install (libs not getting installed)
make install DESTDIR=%{buildroot} \
    ucdincludedir=%{_includedir}/net-snmp/ucd-snmp

install -d %{buildroot}/var/lib/net-snmp
install -d %{buildroot}/var/agentx/master

install -d %{buildroot}%{_sysconfdir}/snmp
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}%{_unitdir}

install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/snmp/snmpd.conf
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/snmpd
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/snmpd

install -m 644 %{SOURCE5} %{buildroot}%{_unitdir}/snmpd.service
install -m 644 dist/snmpd.socket %{buildroot}%{_unitdir}/snmpd.socket

install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/snmp/snmptrapd.conf
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/logrotate.d/snmptrapd
install -m 644 %{SOURCE8} %{buildroot}%{_sysconfdir}/sysconfig/snmptrapd
install -m 644 %{SOURCE9} %{buildroot}%{_unitdir}/snmptrapd.service
install -m 644 dist/snmptrapd.socket %{buildroot}%{_unitdir}/snmptrapd.socket

install -D -m 644 %{SOURCE10} %{buildroot}%{_prefix}/lib/tmpfiles.d/net-snmp.conf

install -m 0755 %{SOURCE11} %{buildroot}%{_bindir}/ucd5820stat

rm -f %{buildroot}%{_bindir}/snmpinform
rm -f %{buildroot}%{_bindir}/snmpcheck
ln -s snmptrap %{buildroot}%{_bindir}/snmpinform

# install some extra stuff...
install -m 644 mibs/NET-SNMP-MONITOR-MIB.txt %{buildroot}%{_datadir}/snmp/mibs/
install -m 644 mibs/NET-SNMP-SYSTEM-MIB.txt %{buildroot}%{_datadir}/snmp/mibs/
install -m 644 mibs/TUNNEL-MIB.txt %{buildroot}%{_datadir}/snmp/mibs/
install -m 644 mibs/UCD-IPFILTER-MIB.txt %{buildroot}%{_datadir}/snmp/mibs/
install -m 644 mibs/UCD-SNMP-MIB-OLD.txt %{buildroot}%{_datadir}/snmp/mibs/
install -m 644 mibs/ianalist %{buildroot}%{_datadir}/snmp/mibs/
install -m 644 mibs/rfclist %{buildroot}%{_datadir}/snmp/mibs/
install -m 644 mibs/rfcmibs.diff %{buildroot}%{_datadir}/snmp/mibs/
install -m 755 mibs/mibfetch %{buildroot}%{_datadir}/snmp/mibs/
install -m 755 mibs/smistrip %{buildroot}%{_datadir}/snmp/mibs/
install -m 644 mibs/Makefile.mib %{buildroot}%{_datadir}/snmp/mibs/
install -m 644 %{SOURCE12} %{buildroot}%{_datadir}/snmp/mibs/NOTIFICATION-TEST-MIB.txt
install -m 644 %{SOURCE13} %{buildroot}%{_datadir}/snmp/mibs/TRAP-TEST-MIB.txt

# fix one bug
perl -pi -e "s|%{buildroot}||g" %{buildroot}%{_libdir}/*.la

# nuke rpath
find %{buildroot}%{perl_vendorarch} -name "*.so" | xargs chrpath -d || :

rm -fr %{buildroot}%{python_sitearch}/netsnmp/__pycache__
rm -fr %{buildroot}%{python_sitearch}/netsnmp/tests/__pycache__

%multiarch_binaries %{buildroot}%{_bindir}/net-snmp-config

%multiarch_includes %{buildroot}%{_includedir}/net-snmp/net-snmp-config.h

%multiarch_binaries %{buildroot}%{_bindir}/net-snmp-create-v3-user

%post
%_post_service snmpd

%preun
%_preun_service snmpd

%post trapd
%_post_service snmptrapd

%preun trapd
%_preun_service snmptrapd

%files
%doc AGENT.txt EXAMPLE.conf FAQ INSTALL NEWS TODO
%doc README README.agent* README.krb5 README.snmpv3 README.thread
%doc local/passtest local/README.mib2c local/ipf-mod.pl
%config(noreplace) %{_sysconfdir}/snmp/snmpd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/snmpd
%config(noreplace) %{_sysconfdir}/logrotate.d/snmpd
%{_prefix}/lib/tmpfiles.d/net-snmp.conf
%{_unitdir}/snmpd.service
%{_unitdir}/snmpd.socket
%{_bindir}/ucd5820stat
%{_sbindir}/snmpd
%{_mandir}/man5/snmpd.conf.5*
%{_mandir}/man5/snmp_config.5*
%{_mandir}/man5/snmp.conf.5*
%{_mandir}/man5/variables.5*
%{_mandir}/man5/snmpd.examples.5*
%{_mandir}/man5/snmpd.internal.5*
%{_mandir}/man8/snmpd.8*

%files trapd
%doc dist/schema-snmptrapd.sql README.sql
%config(noreplace) %{_sysconfdir}/snmp/snmptrapd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/snmptrapd
%config(noreplace) %{_sysconfdir}/logrotate.d/snmptrapd
%{_unitdir}/snmptrapd.service
%{_unitdir}/snmptrapd.socket
%{_sbindir}/snmptrapd
%{_mandir}/man5/snmptrapd.conf.5*
%{_mandir}/man8/snmptrapd.8*

%files utils
%{_bindir}/agentxtrap
%{_bindir}/encode_keychange
%{_bindir}/fixproc
%{_bindir}/ipf-mod.pl
%{_bindir}/mib2c
%{_bindir}/mib2c-update
%{_bindir}/net-snmp-cert
%{_bindir}/net-snmp-create-v3-user
%{multiarch_bindir}/net-snmp-create-v3-user
%{_bindir}/snmp-bridge-mib
%{_bindir}/snmpbulkget
%{_bindir}/snmpbulkwalk
%{_bindir}/snmpconf
%{_bindir}/snmpdelta
%{_bindir}/snmpdf
%{_bindir}/snmpget
%{_bindir}/snmpgetnext
%{_bindir}/snmpinform
%{_bindir}/snmpnetstat
%{_bindir}/snmpset
%{_bindir}/snmpstatus
%{_bindir}/snmptable
%{_bindir}/snmptest
%{_bindir}/snmptranslate
%{_bindir}/snmptrap
%{_bindir}/snmpusm
%{_bindir}/snmpvacm
%{_bindir}/snmpwalk
%{_bindir}/traptoemail
%{_datadir}/snmp/mib2c-data
%{_datadir}/snmp/snmpconf-data
%{_datadir}/snmp/snmp_perl.pl
%{_datadir}/snmp/snmp_perl_trapd.pl
%{_datadir}/snmp/*.conf
%{_mandir}/man1/agentxtrap.1*
%{_mandir}/man1/encode_keychange.1*
%{_mandir}/man1/fixproc.1*
%{_mandir}/man1/mib2c.1*
%{_mandir}/man1/mib2c-update.1*
%{_mandir}/man1/net-snmp-create-v3-user.1*
%{_mandir}/man1/snmp-bridge-mib.1*
%{_mandir}/man1/snmpbulkget.1*
%{_mandir}/man1/snmpbulkwalk.1*
%{_mandir}/man1/snmpcmd.1*
%{_mandir}/man1/snmpconf.1*
%{_mandir}/man1/snmpdelta.1*
%{_mandir}/man1/snmpdf.1*
%{_mandir}/man1/snmpget.1*
%{_mandir}/man1/snmpgetnext.1*
%{_mandir}/man1/snmpinform.1*
%{_mandir}/man1/snmpnetstat.1*
%{_mandir}/man1/snmpset.1*
%{_mandir}/man1/snmpstatus.1*
%{_mandir}/man1/snmptable.1*
%{_mandir}/man1/snmptest.1*
%{_mandir}/man1/snmptranslate.1*
%{_mandir}/man1/snmptrap.1*
%{_mandir}/man1/snmpusm.1*
%{_mandir}/man1/snmpvacm.1*
%{_mandir}/man1/snmpwalk.1*
%{_mandir}/man1/traptoemail.1*
%{_mandir}/man5/mib2c.conf.5*

%files mibs
%doc mibs/README.mibs
%{_datadir}/snmp/mibs

%files -n %{libname}
%{_libdir}/libnetsnmp.so.%{major}*

%files -n %{libagent}
%{_libdir}/libnetsnmpagent.so.%{major}*

%files -n %{libhelpers}
%{_libdir}/libnetsnmphelpers.so.%{major}*

%files -n %{libmibs}
%{_libdir}/libnetsnmpmibs.so.%{major}*

%files -n %{libtrapd}
%{_libdir}/libnetsnmptrapd.so.%{major}*

%files -n %{libsnmp}
%{_libdir}/libsnmp.so.%{major}*

%files -n %{devname}
%doc ChangeLog.bz2
%{multiarch_bindir}/net-snmp-config
%{multiarch_includedir}/net-snmp/net-snmp-config.h
%{_bindir}/net-snmp-config
%{_libdir}/*.so
%dir %{_includedir}/net-snmp
%{_includedir}/net-snmp/*.h
%dir %{_includedir}/net-snmp/agent
%{_includedir}/net-snmp/agent/*.h
%dir %{_includedir}/net-snmp/machine
%{_includedir}/net-snmp/machine/*.h
%dir %{_includedir}/net-snmp/library
%{_includedir}/net-snmp/library/*.h
%{_includedir}/net-snmp/library/README
%dir %{_includedir}/net-snmp/system
%{_includedir}/net-snmp/system/*.h
%dir %{_includedir}/net-snmp/ucd-snmp
%{_includedir}/net-snmp/ucd-snmp/*.h
%dir %{_includedir}/net-snmp/agent/util_funcs
%{_includedir}/net-snmp/agent/util_funcs/*.h
%dir /var/lib/net-snmp
%dir /var/agentx/master
%{_mandir}/man3/*
%exclude %{_mandir}/man3/NetSNMP*
%exclude %{_mandir}/man3/SNMP.3*
%{_mandir}/man1/net-snmp-config.1*

%files -n perl-NetSNMP
%{perl_vendorarch}/auto/NetSNMP
%{perl_vendorarch}/auto/SNMP
%{perl_vendorarch}/SNMP.pm
%{perl_vendorarch}/NetSNMP
%{perl_vendorarch}/Bundle/Makefile.subs.pl
%{_mandir}/man3/NetSNMP*
%{_mandir}/man3/SNMP.3*

%files -n python-netsnmp
%dir %{python_sitearch}/netsnmp
%{python_sitearch}/netsnmp/__init__.py
%{python_sitearch}/netsnmp/client.py
%{python_sitearch}/netsnmp/client_intf*.so
%dir %{python_sitearch}/netsnmp/tests
%{python_sitearch}/netsnmp/tests/__init__.py
%{python_sitearch}/netsnmp/tests/test.py
%dir %{python_sitearch}/netsnmp_python*-py%{py_ver}.egg-info
%{python_sitearch}/netsnmp_python*-py%{py_ver}.egg-info/*

%files tkmib
%{_bindir}/tkmib
%{_mandir}/man1/tkmib.1*
