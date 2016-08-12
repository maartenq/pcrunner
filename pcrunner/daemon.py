#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 et sw=4 sts=4 ft=python fenc=UTF-8 ai
# pcrunner/daemon.py

'''
pcrunner.daemon
---------------

Generic linux daemon base class for python 2.x/3.x.
'''

import sys
import os
import time
import atexit
import signal


class Daemon:
    '''
    A generic daemon class.
    Usage: subclass the daemon class and override the run() method.
    '''

    def __init__(self, pid_file):
        self.pid_file = pid_file

    def daemonize(self):
        '''
        Daemonize class. UNIX double fork mechanism.
        '''

        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError as err:
            sys.stderr.write('fork #1 failed: {0}\n'.format(err))
            sys.exit(1)

        # decouple from parent environment
        os.chdir('/')
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:

                # exit from second parent
                sys.exit(0)
        except OSError as err:
            sys.stderr.write('fork #2 failed: {0}\n'.format(err))
            sys.exit(1)

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(os.devnull, 'r')
        so = open(os.devnull, 'a+')
        se = open(os.devnull, 'a+')

        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pid_file
        atexit.register(self.delpid)

        pid = str(os.getpid())
        with open(self.pid_file, 'w+') as f:
            f.write(pid + '\n')

    def delpid(self):
        '''
        Remove pid file.
        '''
        os.remove(self.pid_file)

    def start(self):
        '''
        Start the daemon.
        '''

        # Check for a pid_file to see if the daemon already runs
        try:
            with open(self.pid_file, 'r') as pf:

                pid = int(pf.read().strip())
        except IOError:
            pid = None

        if pid:
            mesg = "pid file {0} already exist. " + \
                "Daemon already running?\n"
            sys.stderr.write(mesg.format(self.pid_file))
            sys.exit(1)

        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):
        '''
        Stop the daemon.
        '''

        # Get the pid from the pid file
        try:
            with open(self.pid_file, 'r') as pf:
                pid = int(pf.read().strip())
        except IOError:
            pid = None

        if not pid:
            mesg = "pid file {0} does not exist. " + \
                "Daemon not running?\n"
            sys.stderr.write(mesg.format(self.pid_file))
            sys.exit(1)

        # Try killing the daemon process
        try:
            while True:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            e = str(err.args)
            if e.find("No such process") > 0:
                if os.path.exists(self.pid_file):
                    os.remove(self.pid_file)
            else:
                print(str(err.args))
                sys.exit(1)

    def run(self):
        '''
        You should override this method when you subclass Daemon.

        It will be called after the process has been daemonized by start()
        '''
