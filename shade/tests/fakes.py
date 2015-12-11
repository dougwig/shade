# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.V

"""
fakes
----------------------------------

Fakes used for testing
"""


class FakeEndpoint(object):
    def __init__(self, id, service_id, region, publicurl, internalurl=None,
                 adminurl=None):
        self.id = id
        self.service_id = service_id
        self.region = region
        self.publicurl = publicurl
        self.internalurl = internalurl
        self.adminurl = adminurl


class FakeFlavor(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class FakeFloatingIP(object):
    def __init__(self, id, pool, ip, fixed_ip, instance_id):
        self.id = id
        self.pool = pool
        self.ip = ip
        self.fixed_ip = fixed_ip
        self.instance_id = instance_id


class FakeFloatingIPPool(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class FakeImage(object):
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status


class FakeProject(object):
    def __init__(self, id):
        self.id = id


class FakeServer(object):
    def __init__(
            self, id, name, status, addresses=None,
            accessIPv4='', accessIPv6='', flavor=None, image=None):
        self.id = id
        self.name = name
        self.status = status
        self.addresses = addresses
        self.flavor = flavor
        self.image = image
        self.accessIPv4 = accessIPv4
        self.accessIPv6 = accessIPv6


class FakeService(object):
    def __init__(self, id, name, type, service_type, description=''):
        self.id = id
        self.name = name
        self.type = type
        self.service_type = service_type
        self.description = description


class FakeUser(object):
    def __init__(self, id, email, name):
        self.id = id
        self.email = email
        self.name = name


class FakeVolume(object):
    def __init__(
            self, id, status, name, attachments=[],
            size=75):
        self.id = id
        self.status = status
        self.name = name
        self.attachments = attachments
        self.size = size
        self.snapshot_id = 'id:snapshot'
        self.description = 'description'
        self.volume_type = 'type:volume'
        self.availability_zone = 'az1'
        self.created_at = '1900-01-01 12:34:56'
        self.source_volid = '12345'
        self.metadata = {}


class FakeVolumeSnapshot(object):
    def __init__(
            self, id, status, name, description, size=75):
        self.id = id
        self.status = status
        self.name = name
        self.description = description
        self.size = size
        self.created_at = '1900-01-01 12:34:56'
        self.volume_id = '12345'
        self.metadata = {}


class FakeMachine(object):
    def __init__(self, id, name=None, driver=None, driver_info=None,
                 chassis_uuid=None, instance_info=None, instance_uuid=None,
                 properties=None):
        self.id = id
        self.name = name
        self.driver = driver
        self.driver_info = driver_info
        self.chassis_uuid = chassis_uuid
        self.instance_info = instance_info
        self.instance_uuid = instance_uuid
        self.properties = properties


class FakeMachinePort(object):
    def __init__(self, id, address, node_id):
        self.id = id
        self.address = address
        self.node_id = node_id


class FakeSecgroup(object):
    def __init__(self, id, name, description='', rules=None):
        self.id = id
        self.name = name
        self.description = description
        self.rules = rules


class FakeNovaSecgroupRule(object):
    def __init__(self, id, from_port=None, to_port=None, ip_protocol=None,
                 cidr=None, parent_group_id=None):
        self.id = id
        self.from_port = from_port
        self.to_port = to_port
        self.ip_protocol = ip_protocol
        if cidr:
            self.ip_range = {'cidr': cidr}
        self.parent_group_id = parent_group_id


class FakeKeypair(object):
    def __init__(self, id, name, public_key):
        self.id = id
        self.name = name
        self.public_key = public_key


class FakeDomain(object):
    def __init__(self, id, name, description, enabled):
        self.id = id
        self.name = name
        self.description = description
        self.enabled = enabled


class FakeRole(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class FakeGroup(object):
    def __init__(self, id, name, description, domain=None):
        self.id = id
        self.name = name
        self.description = description
        self.domain = domain


class FakeHypervisor(object):
    def __init__(self, id, hostname):
        self.id = id
        self.hypervisor_hostname = hostname


class FakeStack(object):
    def __init__(self, id, name, description=None, status=None):
        self.id = id
        self.stack_name = name
        self.stack_description = description
        self.stack_status = status
