#!/usr/bin/env python
# Adapted from Mark Mandel's implementation
# https://github.com/ansible/ansible/blob/devel/plugins/inventory/vagrant.py
import argparse
import json
import os
import paramiko
import subprocess
import sys

cache_file = '.inventory.json'

def parse_args():
    parser = argparse.ArgumentParser(description="Vagrant inventory script")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true')
    group.add_argument('--host')
    return parser.parse_args()


def list_running_hosts():
    hosts = get_cached_hosts()

    if hosts:
        return hosts

    cmd = "vagrant status --machine-readable"
    status = subprocess.check_output(cmd.split()).rstrip()
    hosts = {'vagrant': {'hosts':[], 'vars': {}}, '_meta': {'hostvars': {}}}
    for line in status.split('\n'):
        (_, host, key, value) = line.split(',')
        if key == 'state' and value == 'running':
            hosts['vagrant']['hosts'].append(host)
            parts = host.split('-')
            if parts:
                group = parts[0]
                if group not in hosts:
                    hosts[group] = {'hosts': [], 'vars': {}}
                hosts[group]['hosts'].append(host)
                hosts['_meta']['hostvars'][host] = get_host_details(host)

    if hosts['vagrant']['hosts']:
        cache_inventory(hosts)

    return hosts


def get_cached_hosts():
    if os.path.isfile(cache_file):
        with open(cache_file) as json_data:
            inventory = json.load(json_data)
            json_data.close()
        return inventory


def get_cached_host(host):
    inventory = get_cached_hosts()

    if inventory and inventory['_meta']['hostvars'][host]:
        return inventory['_meta']['hostvars'][host]
    else:
        return {}


def cache_inventory(inventory):
    with open(cache_file, 'w') as outfile:
        json.dump(inventory, outfile)
        outfile.close()

def get_host_details(host):
    cmd = "vagrant ssh-config {}".format(host)
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    config = paramiko.SSHConfig()
    config.parse(p.stdout)
    c = config.lookup(host)
    return {'ansible_ssh_host': c['hostname'],
            'ansible_ssh_port': c['port'],
            'ansible_ssh_user': c['user'],
            'ansible_ssh_private_key_file': c['identityfile'][0]}


def main():
    args = parse_args()
    if args.list:
        hosts = list_running_hosts()
        json.dump(hosts, sys.stdout)
    else:
        details = get_cached_host(args.host)
        json.dump(details, sys.stdout)

if __name__ == '__main__':
    main()
