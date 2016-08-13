%define name pcrunner
%define version 0.2.3
%define unmangled_version 0.2.3
%define release 1

Summary: Pcrunner (Passive Check Runner)
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: ISCL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Maarten Diemel <maarten@maartendiemel.nl>
Url: https://github.com/maartenq/pcrunner
Requires: python-argparse,PyYAML
BuildRequires: python-setuptools

%description
Pcrunner (Passive Checks Runner is a daemon and service that periodically runs
Nagios_ / Icinga_ checks paralell. The results are posted via HTTPS to a
`NSCAweb`_ server.


* Free software: ISC license
* Documentation: https://pcrunner.readthedocs.io.

Features
--------

* Runs as a daemon on Linux.
* Runs as a service on win32.
* Command line interface for single test runs and/or cron use.
* Parallel execution of check commands.
* Posts check results external commands.
* Termniation of check commands if maximum time exceeds.
* Configuration in YAML.
* Command definition in YAML or text format.


Installation
------------

http://pcrunner.readthedocs.io/en/latest/installation.html


.. _NSCAweb: https://github.com/smetj/nscaweb
.. _Nagios: http://www.nagios.org/
.. _Icinga: http://www.icinga.org/


.. :changelog:

0.2.3 (2016-08-13)
------------------

* Travis/tox fix


0.2.2 (2016-08-13)
------------------

*  ISC License


0.2.1 (2016-08-13)
------------------

* Documentation RPM build updated.


0.2.0 (2016-08-12)
------------------

* First release on PyPI.


%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
mkdir -p %{buildroot}/var/spool/pcrunner
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}/etc/rc.d/init.d
install -m 0644 %{_builddir}/%{name}-%{unmangled_version}/%{name}/etc/commands.txt %{buildroot}%{_sysconfdir}/%{name}/commands.txt
install -m 0644 %{_builddir}/%{name}-%{unmangled_version}/%{name}/etc/commands.yml %{buildroot}%{_sysconfdir}/%{name}/commands.yml
install -m 0640 %{_builddir}/%{name}-%{unmangled_version}/%{name}/etc/pcrunner.yml %{buildroot}%{_sysconfdir}/%{name}/pcrunner.yml
install -m 0755 %{_builddir}/%{name}-%{unmangled_version}/%{name}/etc/pcrunner.init.sh %{buildroot}/etc/rc.d/init.d/pcrunner

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%attr(0755,root,root) /var/spool/pcrunner
%attr(0755,root,root) %{_sysconfdir}/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/commands.txt
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/commands.yml
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/%{name}/pcrunner.yml
%attr(0755,root,root) %config %{_sysconfdir}/rc.d/init.d/pcrunner