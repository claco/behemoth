Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.ssh.forward_agent = true

  config.vm.network "private_network", type: "dhcp"

  consul_server_count = 3

  config.vm.define "bastion" do |server|
    server.vm.hostname = "bastion"
  end

  (1..consul_server_count).each do |machine_id|
    config.vm.define "consul-#{machine_id}" do |server|
      server.vm.hostname = "consul-#{machine_id}"
    end
  end
end
