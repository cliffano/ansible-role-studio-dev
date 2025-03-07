<img align="right" src="https://raw.github.com/cliffano/ansible-role-studio-dev/main/avatar.jpg" alt="Avatar"/>

[![Build Status](https://github.com/cliffano/ansible-role-studio-dev/workflows/CI/badge.svg)](https://github.com/cliffano/ansible-role-studio-dev/actions?query=workflow%3ACI)
[![Security Status](https://snyk.io/test/github/cliffano/ansible-role-studio-dev/badge.svg)](https://snyk.io/test/github/cliffano/ansible-role-studio-dev)
<br/>

Ansible Role Studio Dev Tools
-----------------------------

Studio Dev Tools is a Ansible role for provisioning dev tools for Studio projects .

Usage
-----

Use the role in your playbook:

    - hosts: all

      vars:
        ans_reverse: true
        ans_transformation: 'upper'

      roles:
        - cliffano.studio_dev