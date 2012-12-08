# not really needed anymore, but leaving for just incase legacy issues
%define _requires_exceptions devel(libperl
%define _disable_ld_no_undefined 1
%define Werror_cflags %{nil}

%define major 30
%define libname %mklibname netsnmp %{major}
%define libagent %mklibname netsnmpagent %{major}
%define libhelpers %mklibname netsnmphelpers %{major}
%define libmibs %mklibname netsnmpmibs %{major}
%define libtrapd %mklibname netsnmptrapd %{major}
%define libsnmp %mklibname snmp %{major}
%define develname %mklibname -d net-snmp

# (oe) never enable rpm support as it eats file descriptors like crazy 
# casuing the snmp daemon to die!.
%define build_rpm	0
%{?_without_rpm:	%global build_rpm 0}
%{?_with_rpm:		%global build_rpm 1}

Summary:	A collection of SNMP protocol tools and libraries
Name: 		net-snmp
Version: 	5.7.1
Release: 	1
License:	BSDish
Group:		System/Servers
URL:		http://www.net-snmp.org/
Source0:	http://prdownloads.sourceforge.net/net-snmp/net-snmp-%{version}.tar.gz
Source1:	http://prdownloads.sourceforge.net/net-snmp/net-snmp-%{version}.tar.gz.asc
#Source0:	net-snmp-%{version}.pre1.tar.gz
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
Patch1:		net-snmp-5.4.1-pie.patch
Patch2:		net-snmp-5.5-dir-fix.patch
Patch3:		net-snmp-5.5-multilib.patch
Patch4:		net-snmp-5.5-sensors3.patch
Patch5:		net-snmp-5.6.1-add-pythoninstall-destdir.patch
Patch6:		net-snmp-5.6.1-mysql.patch
Patch7:		net-snmp-5.7.1-linkage_fix.diff
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	net-snmp-mibs
Requires:	net-snmp-utils
Requires:	tcp_wrappers
BuildRequires:	chrpath
BuildRequires:	lm_sensors-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
%if %{build_rpm}
BuildRequires:	rpm-devel
%endif
BuildRequires:	tcp_wrappers-devel
BuildRequires:	mysql-devel
BuildRequires:	python-setuptools

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
Obsoletes:	%{mklibname snmp 0}
Obsoletes:	%{mklibname net-snmp 5}
Obsoletes:	%{mklibname net-snmp 9}
Obsoletes:	%{mklibname net-snmp 50}
Obsoletes:	%{mklibname net-snmp 51}
Obsoletes:	%{mklibname net-snmp 20}
# lib renamed to proper standalone lib
Obsoletes:	%{mklibname net-snmp 30}

%description -n	%{libname}
This package contains the %{name} library for use with NET-SNMP
project's network management tools.

%package -n	%{libagent}
Summary:	Library for Network management %{name}-agent
Group:		System/Libraries
Conflicts:	%{mklibname net-snmp 30}

%description -n	%{libagent}
This package contains the %{name}-agent library for use with NET-SNMP
project's network management tools.

%package -n	%{libhelpers}
Summary:	Library for Network management %{name}-helpers
Group:		System/Libraries
Conflicts:	%{mklibname net-snmp 30}

%description -n	%{libhelpers}
This package contains the %{name}-helpers library for use with NET-SNMP
project's network management tools.

%package -n	%{libmibs}
Summary:	Library for Network management %{name}-mibs
Group:		System/Libraries
Conflicts:	%{mklibname net-snmp 30}

%description -n	%{libmibs}
This package contains the %{name}-mibs library for use with NET-SNMP
project's network management tools.

%package -n	%{libtrapd}
Summary:	Library for Network management %{name}-trapd
Group:		System/Libraries
Conflicts:	%{mklibname net-snmp 30}

%description -n	%{libtrapd}
This package contains the %{name}-trapd library for use with NET-SNMP
project's network management tools.

%package -n	%{libsnmp}
Summary:	Library for Network management snmp
Group:		System/Libraries
Conflicts:	%{mklibname net-snmp 30}

%description -n	%{libsnmp}
This package contains the snmp library for use with NET-SNMP
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
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libagent} = %{version}-%{release}
Requires:	%{libhelpers} = %{version}-%{release}
Requires:	%{libmibs} = %{version}-%{release}
Requires:	%{libtrapd} = %{version}-%{release}
Requires:	%{libsnmp} = %{version}-%{release}
Requires:	perl-devel >= 2:5.12.3-11

%description -n	%{develname}
The %{develname} package contains the development libraries and header
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
Requires(pre): rpm-helper
Requires(postun): rpm-helper
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
Conflicts:	%{name}-devel < 5.6.1-5

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

%setup -q -n %{name}-%{version}

%patch1 -p1 -b .pie~
%patch2 -p1 -b .dir-fix~
%patch3 -p1 -b .multilib~
%patch5 -p1 -b .py_destdir~
#patch6 -p1 -b .mysql
%patch7 -p0 -b .linkage

%if %mdkversion >= 201000
#%%patch4 -p1 -b .sensors3
%endif

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
rm -rf %{buildroot}
%makeinstall_std \
    ucdincludedir=%{_includedir}/net-snmp/ucd-snmp
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

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
%doc dist/schema-snmptrapd.sql README.sql
%attr(0755,root,root) %{_initrddir}/snmptrapd
%attr(0644,root,root) %config(noreplace,missingok) %{_sysconfdir}/snmp/snmptrapd.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/snmptrapd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/snmptrapd
%{_sbindir}/snmptrapd
%attr(0644,root,root) %{_mandir}/man5/snmptrapd.conf.5*
%attr(0644,root,root) %{_mandir}/man8/snmptrapd.8*

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
%attr(0644,root,root) %{_mandir}/man1/agentxtrap.1*
%attr(0644,root,root) %{_mandir}/man1/encode_keychange.1*
%attr(0644,root,root) %{_mandir}/man1/fixproc.1*
%attr(0644,root,root) %{_mandir}/man1/mib2c.1*
%attr(0644,root,root) %{_mandir}/man1/mib2c-update.1*
%attr(0644,root,root) %{_mandir}/man1/net-snmp-create-v3-user.1*
%attr(0644,root,root) %{_mandir}/man1/snmp-bridge-mib.1*
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

%files -n %{develname}
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
#%dir %{_includedir}/net-snmp/agent/util_funcs
#%{_includedir}/net-snmp/agent/util_funcs/*.h
%dir /var/lib/net-snmp
%dir /var/agentx/master
%{_mandir}/man3/*
%exclude %{_mandir}/man3/NetSNMP*
%exclude %{_mandir}/man3/SNMP.3*
%attr(0644,root,root) %{_mandir}/man1/net-snmp-config.1*

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
%{python_sitearch}/netsnmp/client_intf.so
%dir %{python_sitearch}/netsnmp/tests
%{python_sitearch}/netsnmp/tests/__init__.py
%{python_sitearch}/netsnmp/tests/test.py
%dir %{python_sitearch}/netsnmp_python*-py%{py_ver}.egg-info
%{python_sitearch}/netsnmp_python*-py%{py_ver}.egg-info/*

%files tkmib
%{_bindir}/tkmib
%{_mandir}/man1/tkmib.1*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 5.7.1-5
+ Revision: 765938
- rebuilt for perl-5.14.2

* Wed Dec 14 2011 Matthew Dawkins <mattydaw@mandriva.org> 5.7.1-4
+ Revision: 741150
- rebuild
- split all libs up individually
- this greatly reduces laterally linked deps
- disabled static (per oden)
- removed .la files (per oden)
- removed pre 2010 build conditions

  + Oden Eriksson <oeriksson@mandriva.com>
    - cleanup
    - cleanup

* Thu Dec 01 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.7.1-3
+ Revision: 735905
- add a versioned buildrequires on perl-devel to get -fno-PIE fix
- reenable %%serverbuild

* Thu Dec 01 2011 Matthew Dawkins <mattydaw@mandriva.org> 5.7.1-2
+ Revision: 735886
- commented out serverbuild macro as newly adde -fPIE breaks build
- removed dup require (main>utils>openssl)
- rebuild
- cleaned up spec
- removed defattr, mkrel, BuildRoot, clean section
- removed dup reqs for devel pkgs
- dropped req by the lib pkg for openssl
- made comment about _requires_exceptions & perl-devel

  + Oden Eriksson <oeriksson@mandriva.com>
    - ucd is long gone :-)

* Sun Oct 02 2011 Oden Eriksson <oeriksson@mandriva.com> 5.7.1-1
+ Revision: 702427
- added P6 from fedora, mysql fix
- added P7 to fix a mysterious linkage problem
- 5.7.1

* Mon Jul 18 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.7-2
+ Revision: 690521
- Revert lib64 change because perl-base always install libperl.so under /usr/lib

* Sun Jul 17 2011 Oden Eriksson <oeriksson@mandriva.com> 5.7-1
+ Revision: 690190
- 5.7

  + Matthew Dawkins <mattydaw@mandriva.org>
    - removed ifarch conditions for lm-sensors-devel
    - the configure test fails w/o it

* Mon Jun 20 2011 Oden Eriksson <oeriksson@mandriva.com> 5.6.1-8
+ Revision: 686319
- avoid pulling 32 bit libraries on 64 bit arch

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 5.6.1-7
+ Revision: 661708
- multiarch fixes

* Tue Mar 29 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.6.1-6
+ Revision: 648764
- add missing buildrequires for python support
- build python module
- drop no longer needed lib64 quirks
- replace %%ifarch check for lib64 with a %%{_lib} == lib64 check
- add conflicts on older devel package release to ensure file conflict resolution
- drop redundant explicit NEVR dependencies on library package

* Fri Mar 18 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.6.1-5
+ Revision: 646488
- drop ancient scriptlets
- drop useless %%defattr
- fix files included several times

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 5.6.1-4
+ Revision: 645751
- relink against libmysqlclient.so.18

* Mon Mar 14 2011 Thomas Spuhler <tspuhler@mandriva.org> 5.6.1-3
+ Revision: 644609
- increased rel for rebuild

* Wed Jan 05 2011 Oden Eriksson <oeriksson@mandriva.com> 5.6.1-2mdv2011.0
+ Revision: 628693
- rebuilt due to package loss

* Tue Jan 04 2011 Oden Eriksson <oeriksson@mandriva.com> 5.6.1-1mdv2011.0
+ Revision: 628608
- 5.6.1

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 5.6-5mdv2011.0
+ Revision: 627001
- rebuilt against mysql-5.5.8 libs, again

* Mon Dec 27 2010 Oden Eriksson <oeriksson@mandriva.com> 5.6-4mdv2011.0
+ Revision: 625422
- rebuilt against mysql-5.5.8 libs

  + Funda Wang <fwang@mandriva.org>
    - fix lib major

* Mon Oct 11 2010 Funda Wang <fwang@mandriva.org> 5.6-2mdv2011.0
+ Revision: 584956
- rebuild

* Sun Oct 10 2010 Oden Eriksson <oeriksson@mandriva.com> 5.6-1mdv2011.0
+ Revision: 584583
- 5.6
- rediff some patches
- drop upstream added patches

* Mon Sep 13 2010 Thomas Spuhler <tspuhler@mandriva.org> 5.5-10mdv2011.0
+ Revision: 577840
- rebuilt with perl 5.12.2

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 5.5-9mdv2011.0
+ Revision: 564221
- rebuild for new perl 5.12.1

* Thu Jul 22 2010 Olivier Thauvin <nanardon@mandriva.org> 5.5-8mdv2011.0
+ Revision: 556866
- rebuild for new perl

* Tue Apr 06 2010 Funda Wang <fwang@mandriva.org> 5.5-7mdv2010.1
+ Revision: 531960
- rebuild for new openssl

* Thu Apr 01 2010 Oden Eriksson <oeriksson@mandriva.com> 5.5-6mdv2010.1
+ Revision: 530640
- sync some patches with net-snmp-5.5-12.fc13.src.rpm

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 5.5-5mdv2010.1
+ Revision: 511595
- rebuilt against openssl-0.9.8m

* Wed Feb 17 2010 Oden Eriksson <oeriksson@mandriva.com> 5.5-4mdv2010.1
+ Revision: 507033
- rebuild
- rebuild
- fix #55952 (snmp.local.conf settings break Nagios)

* Sat Nov 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.5-2mdv2010.1
+ Revision: 470872
- drop useless manual stripping
- don't install stuff twice, and don'treak permissions on executables
- sync patches and build options with fedora
- sync MIBs list with fedora package
- stop providing compatibility virtual packages for every past versions of
  lib packages
- one single package per line is more readable

* Thu Oct 15 2009 Oden Eriksson <oeriksson@mandriva.com> 5.5-1mdv2010.0
+ Revision: 457609
- 5.5
- drop a whole bunch of patches applied upstream
- rediffed some patches
- new major (20)
- fix deps, snmptrapd supports mysql now so use it

* Tue Sep 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.4.2.1-7mdv2010.0
+ Revision: 450889
- fix build with lm_sensors 3
- more MIBs

* Thu Aug 27 2009 Raphaël Gertz <rapsys@mandriva.org> 5.4.2.1-6mdv2010.0
+ Revision: 421659
- Fix build with gcc4
- Missing patch
- Fix perl agent snmp_error format
- Rebuild

* Wed Feb 25 2009 Oden Eriksson <oeriksson@mandriva.com> 5.4.2.1-5mdv2009.1
+ Revision: 344976
- P56: security fix for CVE-2008-6123
- fix build with latest libtool 2.2.x

* Fri Jan 16 2009 Oden Eriksson <oeriksson@mandriva.com> 5.4.2.1-4mdv2009.1
+ Revision: 330301
- disable -Werror=format-security due to problems in the perl/* code
- disable P16 and fix deps (buchan)
- fix build (partly) with -Wformat-security (P55, from upstream svn)

* Fri Dec 12 2008 Oden Eriksson <oeriksson@mandriva.com> 5.4.2.1-2mdv2009.1
+ Revision: 313620
- rediff some patches to meet the nofuzz criteria

* Fri Oct 31 2008 Oden Eriksson <oeriksson@mandriva.com> 5.4.2.1-1mdv2009.1
+ Revision: 299063
- 5.4.2.1 (fixes CVE-2008-4309)

* Wed Sep 10 2008 Oden Eriksson <oeriksson@mandriva.com> 5.4.2-2mdv2009.0
+ Revision: 283519
- fix deps

* Wed Sep 10 2008 Oden Eriksson <oeriksson@mandriva.com> 5.4.2-1mdv2009.0
+ Revision: 283466
- 5.4.2
- set default snmp version to 3
- use --enable-embedded-perl and --enable-as-needed (build fix)
- drop one obsolete patch (P25)
- rediffed P52

* Fri Jul 11 2008 Oden Eriksson <oeriksson@mandriva.com> 5.4.1.2-1mdv2009.0
+ Revision: 233725
- 5.4.1.2

* Thu Jul 03 2008 Michael Scherer <misc@mandriva.org> 5.4.1.1-3mdv2009.0
+ Revision: 231240
- add patch 54, fix https://qa.mandriva.com/show_bug.cgi?id=41592 and CVE-2008-2292

* Tue Jun 10 2008 Oden Eriksson <oeriksson@mandriva.com> 5.4.1.1-2mdv2009.0
+ Revision: 217535
- bump release
- 5.4.1.1 (Major security fixes)
- use "_disable_ld_no_undefined 1" due to problems with the perl module

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat May 03 2008 Oden Eriksson <oeriksson@mandriva.com> 5.4.1-6mdv2009.0
+ Revision: 200724
- added P2 to make it build
- rebuild

* Wed Jan 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.4.1-5mdv2008.1
+ Revision: 157169
- add tkmib subpackage

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 5.4.1-4mdv2008.1
+ Revision: 151415
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 17 2007 Oden Eriksson <oeriksson@mandriva.com> 5.4.1-3mdv2008.1
+ Revision: 121689
- don't cast possible lvalue (P1 from pld)

* Sat Dec 08 2007 David Walluck <walluck@mandriva.org> 5.4.1-2mdv2008.1
+ Revision: 116544
- add sensors3 and xen-crash patch from Fedora

* Wed Aug 08 2007 Oden Eriksson <oeriksson@mandriva.com> 5.4.1-1mdv2008.0
+ Revision: 60181
- fix rpmlint upload blockers
- 5.4.1
- dropped upstream/obsolete patches; P20,P23,P29,P30,P31,P32,P51
- rediffed patches; P24,P50,P52,P53
- added new P25 from fedora
- obey 2008 specs

* Thu Jun 28 2007 Andreas Hasenack <andreas@mandriva.com> 5.3.1-7mdv2008.0
+ Revision: 45526
- rely on new serverbuild macro to set -fstack-protector* flags

* Fri Jun 08 2007 Oden Eriksson <oeriksson@mandriva.com> 5.3.1-6mdv2008.0
+ Revision: 37287
- really use the cflags
- update libtool since that was removed in the latest %%configure2_5x macro
- fix build, again
- it suddenly wants -fPIC on x86_64, so be it
- fix build
- use distro conditional -fstack-protector

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 5.3.1-5mdv2008.0
+ Revision: 33597
- make it provide two forgotten directories

* Tue May 29 2007 Andreas Hasenack <andreas@mandriva.com> 5.3.1-4mdv2008.0
+ Revision: 32533
- fix build


* Mon Jan 29 2007 Olivier Blin <oblin@mandriva.com> 5.3.1-3mdv2007.0
+ Revision: 115115
- bzip2 huge ChangeLog and move it in devel package
- remove README files for other operating systems

* Wed Aug 16 2006 Andreas Hasenack <andreas@mandriva.com> 5.3.1-2mdv2007.0
+ Revision: 56245
- disable make test, doesn't work on cluster but works here and latency
  is too high for proper debugging
- get rid of bzcat
- added support for parallel initscripts (closes #24223)
- bunzip files now that we are stored in svn
- Import net-snmp

* Fri Aug 11 2006 Oden Eriksson <oeriksson@mandriva.com> 5.3.1-1mdv2007.0
- 5.3.1 (Major bugfixes)
- new P25
- rediffed P50 (one hunk didn't apply but seemed ok)

* Sun Jul 30 2006 Oden Eriksson <oeriksson@mandriva.com> 5.3.0.1-8mdv2007.0
- fix #20742

* Sat May 13 2006 Oden Eriksson <oeriksson@mandriva.com> 5.3.0.1-7mdk
- enable DISMAN-EVENT-MIB (Zeck)

* Fri Apr 07 2006 Oden Eriksson <oeriksson@mandriva.com> 5.3.0.1-6mdk
- deactivate the lm_sensors mibs per default (S13) (#19388)

* Wed Mar 15 2006 Oden Eriksson <oeriksson@mandriva.com> 5.3.0.1-5mdk
- disable rpm support because it eats file descriptors like crazy and 
  makes the snmp daemon easy to kill
- drop the apache hooks as it is poorly written and unmaintained

* Wed Mar 08 2006 Oden Eriksson <oeriksson@mandriva.com> 5.3.0.1-4mdk
- fix deps

* Sun Feb 05 2006 Oden Eriksson <oeriksson@mandriva.com> 5.3.0.1-3mdk
- fix crash on s390x and ppc64 (from fedora 5.3-4)

* Wed Feb 01 2006 Oden Eriksson <oeriksson@mandriva.com> 5.3.0.1-2mdk
- added P29,P30,P31 from fedora (5.3-3)

* Sun Jan 15 2006 Oden Eriksson <oeriksson@mandriva.com> 5.3.0.1-1mdk
- 5.3.0.1 (security fix)

* Fri Jan 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.3-2mdk
- drop selinux support

* Wed Jan 04 2006 Oden Eriksson <oeriksson@mandriva.com> 5.3-1mdk
- 5.3
- drop obsolete/upstream patches (P29-P32)

* Sat Dec 31 2005 Stefan van der Eijk <stefan@eijk.nu> 5.2.2-3mdk
- re-enable rpm support

* Wed Dec 21 2005 Oden Eriksson <oeriksson@mandriva.com> 5.2.2-2mdk
- bump major to 9 (!)
- fix deps

* Tue Dec 20 2005 Oden Eriksson <oeriksson@mandriva.com> 5.2.2-1mdk
- 5.2.2
- drop obsolete/upstream patches, reorder patches
- sync with fedora (5.2.2-4.1)
- rediffed P50
- added a work around for #20256 (S13)

* Sun Nov 13 2005 Oden Eriksson <oeriksson@mandriva.com> 5.2.1.2-6mdk
- rebuilt against openssl-0.9.8a

* Wed Oct 26 2005 Oden Eriksson <oeriksson@mandriva.com> 5.2.1.2-5mdk
- rebuilt against new shared tcp_wrappers lib (libwrap)
- fix deps
- fix #16460

* Sat Sep 10 2005 Olivier Blin <oblin@mandriva.com> 5.2.1.2-4mdk
- fix typo in summary

* Wed Aug 24 2005 Oden Eriksson <oeriksson@mandriva.com> 5.2.1.2-3mdk
- mod_ap2_snmp_1.03 (Minor bugfixes)
- fix deps

* Fri Aug 19 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 5.2.1.2-2mdk
- add back some of previous 64-bit fixes
- libtool fixes for the testsuite to work with just-built libraries

* Sat Aug 13 2005 Olivier Blin <oblin@mandriva.com> 5.2.1.2-1mdk
- 5.2.1.2

* Thu Jul 21 2005 Olivier Blin <oblin@mandriva.com> 5.2.1-6mdk
- conflict with libsnmp-devel (#16460)

* Fri Jun 10 2005 Oden Eriksson <oeriksson@mandriva.com> 5.2.1-5mdk
- added P52 to fix a mem leak (Loic Vaillant)
- added two mibs on request by Loic Vaillant
- use the %%mkrel macro
- reactivate the make test test suite

* Sat Jun 04 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.2.1-4mdk
- sync with fedora (5.2.1-13)
- rediffed our 64bit fixes patch (now P50)
- use new rpm-4.4.x pre,post magic
- nuke rpath, spec file hack + P51
- rpmlint fixes

* Fri Mar 11 2005 Luca Berra <bluca@vodka.it> 5.2.1-3mdk 
- devel pacjage requires lm_sensors-devel when building with lm_sensors support

* Mon Feb 14 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.2.1-2mdk
- mod_ap2_snmp_1.02
- drop P28, it's implemented upstream

* Tue Feb 01 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.2.1-1mdk
- 5.2.1
- added P27 (fedora)

* Mon Jan 31 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.2-3mdk
- fix deps and conditional %%multiarch

* Sat Jan 15 2005 Luca Berra <bluca@vodka.it> 5.2-2mdk 
- rebuild to catch libwrap requiring libnsl

* Fri Dec 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.2-1mdk
- 5.2
- sync with fedora
- drop P4,P6,P22,P27,P31, redundant/merged upstream
- rpmlint fixes

* Tue Nov 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.1.2-7mdk
- rebuilt for unthreaded perl

* Tue Oct 05 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 5.1.2-6mdk
- 64-bit fixes + little endian fix for AgentX (SF #996462)

* Fri Aug 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.1.2-5mdk
- fix a problem with showing numerical OID's (S9), reported by "tbsky"

* Fri Aug 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.1.2-4mdk
- perl-Net-SNMP does not obsolete the older perl-Net-SNMP that 
  provides perl(Net::SNMP), these are unrelated(!) rename _this_ 
  perl package to perl-NetSNMP.

* Fri Aug 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.1.2-3mdk
- added the perl-Net-SNMP sub package

* Tue Aug 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.1.2-2mdk
- added P28 to make S10 compile

* Sun Aug 22 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.1.2-1mdk
- 5.1.2
- added S10, but it won't compile just yet...
- drop P1 & P5, it's included

* Mon Jun 07 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.1.1-1mdk
- 5.1.1
- stole P20 - P27 from fedora
- fixed the initscripts
- use the %%configure2_5x macro
- remove deprecated stuff from S6
- run tests in dir that is cleaned
- misc spec file fixes

* Wed Mar 17 2004 Florin <florin@mandrakesoft.com> 5.1-7mdk
- add the bsd-compat patch to fix the error:
"process `snmptrapd' is using obsolete setsockopt SO_BSDCOMPAT"

