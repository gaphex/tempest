# Copyright 2014 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.common import rest_client
from tempest import config
import urllib

CONF = config.CONF


class DatabaseFlavorsClientJSON(rest_client.RestClient):

    def __init__(self, auth_provider):
        super(DatabaseFlavorsClientJSON, self).__init__(auth_provider)
        self.service = CONF.database.catalog_type

    def list_db_flavors(self, params=None):
        url = 'flavors'
        if params:
            url += '?%s' % urllib.urlencode(params)

        resp, body = self.get(url)
        return resp, self._parse_resp(body)

    def get_db_flavor_details(self, db_flavor_id):
        resp, body = self.get("flavors/%s" % str(db_flavor_id))
        return resp, self._parse_resp(body)
