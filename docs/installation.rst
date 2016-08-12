============
Installation
============


Windows
=======

* Install *Python 2.7.6*

    * Download `Python 2.7.6 Windows X86-64 Installer`_
    * Double click to run the installer.


* Install *Python for Windows extensions*

    * Download `pywin32-218.win-amd64-py2.7.exe`_
    * Double click to run the installer.


* Install *Setuptools*

    * Download `ez_setup.py`_
    * Go to folder
    * Shift-right-click
    * Click *Open command window here*
    * Run::

        C:\Python27\python.exe ez_setup.py


* Install *Passive Check Runner*

    * Download `master.zip`_::
      curl -o master.zip https://codeload.github.com/maartenq/pcrunner/zip/master
    * Go to folder
    * Shift-right-click
    * Click *Open command window here*
    * Run::

        C:\Python27\Scripts\easy_install.exe master.zip


* Install *Passive Check Runner* as Windows Service

    * Go to folder ``C:\Python27\Lib\site-packages\pcrunner-0.2.0-py2.7.egg\pcrunner``
    * Shift-right-click
    * Click *Open command window here*
    * Run::

        C:\Python27\python.exe windows_service.py install


* Configure *Passive Check Runner* as Windows Service

    * Edit ``C:\Python27\Lib\site-packages\pcrunner-0.2.0-py2.7.egg\pcrunner\etc\pcrunner.yml``
        * *nsca_web_url*
        * *nsca_web_username*
        * *nsca_web_password*


* Start *Passive Check Runner* as Windows Service

    * *Start* -> *Administrative Tools* -> *Services*
    * Select *Passive Check Runner*
    * Click start


Linux with virtualenv
=====================

Installation on Fedora/RH/Centos/SL

.. note::

    * Commands with a '#' prompt must be run as root.
    * Commands with a '$' prompt must be run as a non-root user.
    * 'sudo' is used when a reverence to a home directory (~) is used in the
      command line.


* Download *Passive Check Runner*::

    # curl -O https://github.com/maartenq/pcrunner/archive/master.zip


* Install python-virtualenv_::

    # yum install python-virtualenv


* Make virtual environment::

    # virtualenv /<path>/<to>/<virtualenv_dir>


* Make virtual environment active::

    # source /<path>/<to>/<virtualenv_dir>/bin/activate


* Install *Passive Check Runner*::

    (virtenv)# pip install master.zip


* Install configuration files::

    # mkdir /etc/pcrunner
    # mkdir /var/spool/pcrunner
    # install -m 640 /<path>/<to>/<virtualenv_dir>/lib/python2.6/site-packages/pcrunner/etc/pcrunner.yml /etc/pcrunner/pcrunner.yml
    # install -m 644 /<path>/<to>/<virtualenv_dir>/lib/python2.6/site-packages/pcrunner/etc/commands.yml /etc/pcrunner/commands.yml
    # install -m 755 /<path>/<to>/<virtualenv_dir>/lib/python2.6/site-packages/pcrunner/etc/pcrunner_rh_init /etc/init.d/


* Edit configuration files::

    # vim /etc/pcrunner/pcrunner.yml
    # vim /etc/pcrunner/commands.yml


* Check the config::

    # chkconfig pcrunner on


* Start the service::

    # service pcrunner start


Linux RPM
=========

.. note::

    * Commands with a '#' prompt must be run as root.
    * Commands with a '$' prompt must be run as a non-root user.
    * 'sudo' is used when a reverence to a home directory (~) is used in the
      command line.


* Install packages for RPM Build Environment::

    # yum install rpm-build
    # yum install python-devel
    # yum install python-setuptools


* Create directories for RPM Build Environment::

    $ mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}


* Create RPM macro file::

    $ echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros


* Clone the repository::

    $ cd
    $ git clone git@github.com:maartenq/pcrunner.git


* Create SRPM package::

    $ cd pcrunner/
    $ python setup.py bdist --formats=rpm


* Install Source RPM package::

    $ rpm -ivh dist/pcrunner-0.2.0-1.src.rpm


* Patch .spec file::

    $ cd ~/rpmbuild/SPECS/
    $ patch < ~/pcrunner/pcrunner.spec.patch


* Build RPM with patched .spec file::

    $ rpmbuild -ba pcrunner.spec


* Install RPM::

   $ sudo yum install ~/rpmbuild/RPMS/noarch/pcrunner-0.2.0-1.noarch.rpm


* Edit configuration files::

    # vim /etc/pcrunner/pcrunner.yml
    # vim /etc/pcrunner/commands.yml


* Check the config::

    # chkconfig pcrunner on


* Start the service::

    # service pcrunner start


.. _Python 2.7.6 Windows X86-64 Installer: http://legacy.python.org/ftp//python/2.7.6/python-2.7.6.amd64.msi

.. _pywin32-218.win-amd64-py2.7.exe: http://downloads.sourceforge.net/project/pywin32/pywin32/Build%20218/pywin32-218.win-amd64-py2.7.exe?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fpywin32%2Ffiles%2Fpywin32%2FBuild%2520218%2F&ts=1388760155&use_mirror=netcologne

.. _ez_setup.py: https://bootstrap.pypa.io/ez_setup.py

.. _master.zip: https://codeload.github.com/maartenq/pcrunner/zip/master

.. _python-virtualenv: https://virtualenv.pypa.io/
