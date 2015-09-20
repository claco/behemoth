apt_cachier_ng
==============

Install and configure apt-cachier-ng

Requirements
------------

Ubuntu or Debian

Role Variables
--------------

* `apt_cacher_ng_port: 3142` The default apt-cachier-ng port
* `apt_cacher_ng_cache_dir: /var/cache/apt-cacher-ng` The apt-cachir-ng cache directory

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: apt_cachier_ng }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
