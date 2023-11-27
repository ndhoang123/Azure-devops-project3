resource "azurerm_network_interface" "" {
  name                = "${var.application_type}-${var.resource_type}-nic"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip}"
  }
}

resource "azurerm_linux_virtual_machine" "" {
  name                = "${var.application_type}-${var.resource_type}-vm"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS2_v2"
  admin_username      = "${var.admin_username}"
  network_interface_ids = []
  admin_ssh_key {
    username   = "admin"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCfLMh+0ElrHH2Iu2ahuw90fGOP4wYM2gS5NnzKWs5yaFAHN23fgfTaGUwpE8QKpyeoZEGFBetQaGEjOFzq3zTcyHVE0C8+bwO0wC5QroVuCbiCOeSfg806qsW8hynUsGD5qkMVtoFdC5cVogIwY7qKBmE0dR8DIcZsHGOwsv57awkyINt2dP1ySXRez/3cQsEqGkNYo9JxH2SWtiYeQEREjHiFXMw6HcVR+VK4UTMjbFhWCQAqg1rEcz4lt1EpV/+sMb7FIbMk1Yf6rQh7wXy4VbCnaV8iSY7esZG7L8Af+DinSFzMR/KdPSZbOj7UdIgxIGi98yJ+XfD/NheFhNDIt8400BB1Fdwhob//lV4Ps9XPWoYOycN4Pzlt4ojJ2cJpwlhUF1KeUqryA94a5dUN3dESR4IeIVo48CYTYm6T78wPZdgcWXXP3XkWskx69WT1M80n2KKvKpyJdYa1RvUP14h8mDiJNKpK17m0ylvI2MxX+xWIW61ToKtGzfMK1Dc= admins@Sergio-Nguyen"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
