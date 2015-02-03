# Copyright 2015 Red Hat, Inc.
#
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
# under the License.

import blivet

from os_disk_config import impl_base

class BlivetDiskConfig(impl_base.DiskConfigBase):
    def __init__(self):
        super(BlivetDiskConfig, self).__init__()
        self._blivet = blivet.Blivet()
        self._blivet.reset()

    def disks(self):
        return [i.path for i in self._blivet.devices if len(i.parents) == 0]

    def apply(self, noop):
        if not noop:
            self._blivet.doIt()
