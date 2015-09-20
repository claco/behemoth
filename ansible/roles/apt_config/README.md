apt_config
==========

Configure various apt related settings.

Requirements
------------

Ubuntu or Debian

Role Variables
--------------

* `apt_config_proxy_enable: true` Enable or disable apt proxy support
* `apt_config_proxy_host: localhost` The apt cache proxy host
* `apt_config_proxy_path: /etc/apt/apt.conf.d/01proxy` The apt proxy config file name
* `apt_config_proxy_port: 3142` The apt cache proxy port
* `apt_config_proxy_http: https://localhost:3128` The default apt proxy address for http
* `apt_config_proxy_https:` The default apt proxy address for https

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: apt_config, apt_config_proxy_enable: true, apt_config_proxy_host: somehost }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
