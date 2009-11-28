%define _requires_exceptions devel(libperl

%if %mdkversion >= 200810
%define _disable_ld_no_undefined 1
%endif

%if %mdkversion >= 200910
%define Werror_cflags %{nil}
%endif

%define major 20
%define libname %mklibname net-snmp %{major}
%define develname %mklibname -d net-snmp
%define staticdevelname %mklibname -d -s net-snmp

# (oe) never enable rpm support as it eats file descriptors like crazy 
# casuing the snmp daemon to die!.
%define build_rpm	0
%{?_without_rpm:	%global build_rpm 0}
%{?_with_rpm:		%global build_rpm 1}

Summary:	A collection of SNMP protocol tools and libraries
Name: 		net-snmp
Version: 	5.5
Release: 	%mkrel 1
License:	BSDish
Group:		System/Servers
URL:		http://www.net-snmp.org/
Source0:	http://prdownloads.sourceforge.net/net-snmp/net-snmp-%{version}.tar.gz
Source1:	http://prdownloads.sourceforge.net/net-snmp/net-snmp-%{version}.tar.gz.asc
Source2:	net-snmpd.init
Source3:	snmpd.conf
Source4:	snmpd.logrotate
Source5:	net-snmptrapd.init
Source6:	snmptrapd.conf
Source7:	snmptrapd.logrotate
Source8:	ucd5820stat
Source9:	snmp.local.conf
Source11:	NOTIFICATION-TEST-MIB.txt
Source12:	TRAP-TEST-MIB.txt
Source13:	net-snmpd.sysconfig
Source14:	net-snmptrapd.sysconfig
# OE: stolen from fedora
Patch1:		net-snmp-5.4.1-pie.patch
Patch2:		net-snmp-5.5-dir-fix.patch
Patch3:		net-snmp-5.5-multilib.patch
Patch4:		net-snmp-5.5-sensors3.patch 
# mdv patches
Patch52:   net-snmp-5.5-gcc4-format-fix.patch
Patch53:   net-snmp-5.5-fix-perl-install.patch
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre): %{libname} = %{version}
Requires(postun): %{libname} = %{version}
Requires:	openssl
Requires:	net-snmp-mibs
Requires:	net-snmp-utils
Requires:	tcp_wrappers
BuildRequires:	chrpath
%ifarch %{ix86} x86_64
BuildRequires:	lm_sensors-devel
%endif
%if %mdkversion >= 1020
BuildRequires:	multiarch-utils >= 1.0.3
%endif
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
%if %{build_rpm}
BuildRequires:	rpm-devel
%endif
BuildRequires:	tcp_wrappers-devel
BuildRequires:	mysql-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Summary:	Libraries for Network management (SNMP), from the NET-SNMP project
Group:		System/Libraries
Obsoletes:	%{mklibname snmp 0}
Obsoletes:	%{mklibname net-snmp 5}
Obsoletes:	%{mklibname net-snmp 9}
Obsoletes:	%{mklibname net-snmp 50}
Obsoletes:	%{mklibname net-snmp 51}
Obsoletes:	ucd-snmp
Requires:	openssl

%description -n	%{libname}
The %{libname} package contains the libraries for use with the NET-SNMP
project's network management tools.

%package -n	%{develname}
Summary:	The development environment for the NET-SNMP project
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libnet-snmp-devel
Obsoletes:	%{mklibname snmp 0}-devel
Obsoletes:	%{mklibname net-snmp 10}-devel 
Obsoletes:	%{mklibname net-snmp 9}-devel
Obsoletes:	%{mklibname net-snmp 5}-devel
Obsoletes:	%{mklibname net-snmp 50}-devel
Obsoletes:	%{mklibname net-snmp 51}-devel
Requires:	%{libname} = %{version}
Requires:	tcp_wrappers-devel
%ifarch %{ix86} x86_64
Requires:	lm_sensors-devel
%endif
Obsoletes:	ucd-snmp-devel
Requires:	perl-devel

%description -n	%{develname}
The %{develname} package contains the development libraries and header
files for use with the NET-SNMP project's network management tools.

Install the net-snmp-devel package if you would like to develop applications
for use with the NET-SNMP project's network management tools.

%package -n	%{staticdevelname}
Summary:	The static development libraries for the NET-SNMP project
Group:		Development/C
Provides:	%{name}-static-devel
Obsoletes:	%{mklibname snmp 0}-static-devel
Obsoletes:	%{mklibname net-snmp 5}-static-devel
Obsoletes:	%{mklibname net-snmp 9}-static-devel
Obsoletes:	%{mklibname net-snmp 10}-static-devel
Obsoletes:	%{mklibname net-snmp 50}-static-devel
Obsoletes:	%{mklibname net-snmp 51}-static-devel
Requires:	%{develname} = %{version}
Requires:	%{libname} = %{version}

%description -n	%{staticdevelname}
The %{staticdevelname} package contains the static development
libraries and header files for use with the NET-SNMP project's network
management tools.

Install the net-snmp-static-devel package if you would like to develop
applications for use with the NET-SNMP project's network management tools.

%package	utils
Summary:	Network management utilities using SNMP, from the NET-SNMP project
Group:		Networking/Other
Requires:	%{libname} = %{version}
Requires:	openssl
Requires:	net-snmp-mibs
Obsoletes:	ucd-snmp-util ucd-snmp-utils

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
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}
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
Requires:	%{libname} = %{version}
Requires:	net-snmp-mibs
Requires:	net-snmp-utils

%description -n	perl-NetSNMP
NET SNMP (Simple Network Management Protocol) Perl5 Support The Simple Network
Management Protocol (SNMP) provides a framework for the exchange of management
information between agents (servers) and clients.  The NET SNMP perl5 support
files provide the perl functions for integration of SNMP into applications,
written in perl.

%prep
%setup -q

# fedora patches
%patch1 -p1 -b .pie
%patch2 -p1 -b .dir-fix
%patch3 -p1 -b .multilib

%if %mdkversion >= 201000
%patch4 -p1 -b .sensors3
%endif

# mdv patches
%patch52 -p0 -b .gcc4-format-fix

# run tests in dir that is cleaned
install -d -m777 test_tmp_dir
HERE="$RPM_BUILD_DIR/%{name}-%{version}"
perl -pi -e "s|/tmp/snmp-test|$HERE/test_tmp_dir/snmp-test|g" testing/*

# Do this patch with a perl hack...
perl -pi -e "s|'\\\$install_libdir'|'%{_libdir}'|" ltmain.sh

bzip2 ChangeLog

%build
%serverbuild

%ifarch ia64 x86_64 s390x ppc64
export LDFLAGS="-L%{_libdir}"
%endif
export LIBDIR="%{_libdir}" 

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
    --enable-static \
    --enable-shared \
    --sysconfdir=%{_sysconfdir} \
    --enable-ipv6 \
    --enable-ucd-snmp-compatibility \
    --enable-embedded-perl \
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
rm -rf %{buildroot}
%makeinstall_std \
    ucdincludedir=%{_includedir}/net-snmp/ucd-snmp

install -d %{buildroot}%{_initrddir}
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}%{_sysconfdir}/snmp
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -d %{buildroot}/var/lib/net-snmp
install -d %{buildroot}/var/agentx/master

install -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/snmpd
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/snmp/snmpd.conf
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/snmpd
install -m 0755 %{SOURCE5} %{buildroot}%{_initrddir}/snmptrapd
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/snmp/snmptrapd.conf
install -m 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/logrotate.d/snmptrapd
install -m 0755 %{SOURCE8} %{buildroot}%{_bindir}/ucd5820stat
install -m 0644 %{SOURCE9} %{buildroot}%{_sysconfdir}/snmp/snmp.local.conf

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
install -m 644 %{SOURCE11} %{buildroot}%{_datadir}/snmp/mibs/NOTIFICATION-TEST-MIB.txt
install -m 644 %{SOURCE12} %{buildroot}%{_datadir}/snmp/mibs/TRAP-TEST-MIB.txt
install -m 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/sysconfig/snmpd
install -m 644 %{SOURCE14} %{buildroot}%{_sysconfdir}/sysconfig/snmptrapd

# fix one bug
perl -pi -e "s|%{buildroot}||g" %{buildroot}%{_libdir}/*.la

# nuke rpath
find %{buildroot}%{perl_vendorarch} -name "*.so" | xargs chrpath -d || :

%if %mdkversion >= 1020
%multiarch_binaries %{buildroot}%{_bindir}/net-snmp-config
%multiarch_includes %{buildroot}%{_includedir}/net-snmp/net-snmp-config.h
%multiarch_binaries %{buildroot}%{_bindir}/net-snmp-create-v3-user
%endif

%post
%_post_service snmpd

%preun
%_preun_service snmpd

%post trapd
%_post_service snmptrapd

%preun trapd
%_preun_service snmptrapd

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AGENT.txt EXAMPLE.conf FAQ INSTALL NEWS TODO
%doc README README.agent* README.krb5 README.snmpv3 README.thread
%doc local/passtest local/README.mib2c local/ipf-mod.pl
%attr(0755,root,root) %{_initrddir}/snmpd
%attr(0644,root,root) %config(noreplace,missingok) %{_sysconfdir}/snmp/snmpd.conf
%attr(0644,root,root) %config(noreplace,missingok) %{_sysconfdir}/snmp/snmp.local.conf
%attr(0644,root,root) %config(noreplace,missingok) %{_sysconfdir}/sysconfig/snmpd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/snmpd
%{_bindir}/ucd5820stat
%{_sbindir}/snmpd
%attr(0644,root,root) %{_mandir}/man5/snmpd.conf.5*
%attr(0644,root,root) %{_mandir}/man5/snmp_config.5*
%attr(0644,root,root) %{_mandir}/man5/snmp.conf.5*
%attr(0644,root,root) %{_mandir}/man5/variables.5*
%attr(0644,root,root) %{_mandir}/man5/snmpd.examples.5*
%attr(0644,root,root) %{_mandir}/man5/snmpd.internal.5*
%attr(0644,root,root) %{_mandir}/man8/snmpd.8*

%files trapd
%defattr(-,root,root,-)
%doc dist/schema-snmptrapd.sql README.sql
%attr(0755,root,root) %{_initrddir}/snmptrapd
%attr(0644,root,root) %config(noreplace,missingok) %{_sysconfdir}/snmp/snmptrapd.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/snmptrapd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/snmptrapd
%{_sbindir}/snmptrapd
%attr(0644,root,root) %{_mandir}/man5/snmptrapd.conf.5*
%attr(0644,root,root) %{_mandir}/man8/snmptrapd.8*

%files utils
%defattr(-,root,root,-)
%{_bindir}/encode_keychange
%{_bindir}/fixproc
%{_bindir}/ipf-mod.pl
%{_bindir}/mib2c
%{_bindir}/mib2c-update
%{_bindir}/net-snmp-create-v3-user
%if %mdkversion >= 1020
%multiarch %{multiarch_bindir}/net-snmp-create-v3-user
%endif
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
%attr(0644,root,root) %{_mandir}/man1/encode_keychange.1*
%attr(0644,root,root) %{_mandir}/man1/fixproc.1*
%attr(0644,root,root) %{_mandir}/man1/mib2c-update.1*
%attr(0644,root,root) %{_mandir}/man1/mib2c.1*
%attr(0644,root,root) %{_mandir}/man1/net-snmp-create-v3-user.1*
%attr(0644,root,root) %{_mandir}/man1/snmpbulkget.1*
%attr(0644,root,root) %{_mandir}/man1/snmpbulkwalk.1*
%attr(0644,root,root) %{_mandir}/man1/snmpcmd.1*
%attr(0644,root,root) %{_mandir}/man1/snmpconf.1*
%attr(0644,root,root) %{_mandir}/man1/snmpdelta.1*
%attr(0644,root,root) %{_mandir}/man1/snmpdf.1*
%attr(0644,root,root) %{_mandir}/man1/snmpget.1*
%attr(0644,root,root) %{_mandir}/man1/snmpgetnext.1*
%attr(0644,root,root) %{_mandir}/man1/snmpinform.1*
%attr(0644,root,root) %{_mandir}/man1/snmpnetstat.1*
%attr(0644,root,root) %{_mandir}/man1/snmpset.1*
%attr(0644,root,root) %{_mandir}/man1/snmpstatus.1*
%attr(0644,root,root) %{_mandir}/man1/snmptable.1*
%attr(0644,root,root) %{_mandir}/man1/snmptest.1*
%attr(0644,root,root) %{_mandir}/man1/snmptranslate.1*
%attr(0644,root,root) %{_mandir}/man1/snmptrap.1*
%attr(0644,root,root) %{_mandir}/man1/snmpusm.1*
%attr(0644,root,root) %{_mandir}/man1/snmpvacm.1*
%attr(0644,root,root) %{_mandir}/man1/snmpwalk.1*
%attr(0644,root,root) %{_mandir}/man1/traptoemail.1*
%attr(0644,root,root) %{_mandir}/man5/mib2c.conf.5*

%files mibs
%defattr(-,root,root,-)
%doc mibs/README.mibs
%{_datadir}/snmp/mibs

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(0644,root,root,755)
%defattr(-,root,root,-)
%doc ChangeLog.bz2
%if %mdkversion >= 1020
%multiarch %{multiarch_bindir}/net-snmp-config
%multiarch %{multiarch_includedir}/net-snmp/net-snmp-config.h
%endif
%{_bindir}/net-snmp-config
%{_libdir}/*.so
%{_libdir}/*.la
#%{_includedir}/ucd-snmp
%{_includedir}/net-snmp
%{_includedir}/net-snmp/net-snmp-config.h
%{_mandir}/man3/*
%dir /var/lib/net-snmp
%dir /var/agentx/master
%attr(0644,root,root) %{_mandir}/man1/net-snmp-config.1*

%files -n %{staticdevelname}
%defattr(0644,root,root,755)
%defattr(-,root,root,-)
%{_libdir}/*.a

%files -n perl-NetSNMP
%defattr(0644,root,root,755)
%{perl_vendorarch}/auto/NetSNMP
%{perl_vendorarch}/auto/SNMP
%{perl_vendorarch}/SNMP.pm
%{perl_vendorarch}/NetSNMP
%{perl_vendorarch}/Bundle/Makefile.subs.pl
%{_mandir}/man3/NetSNMP*
%{_mandir}/man3/SNMP.3*

%files tkmib
%defattr(-,root,root)
%{_bindir}/tkmib
%{_mandir}/man1/tkmib.1*

