# Copyright (c) 2013 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

import multiprocessing
from wsgiref import simple_server

from falcon import testing as ftest

from marconi.proxy import bootstrap
from tests.unit.queues.transport.wsgi import base


class TestBase(base.TestBase):

    def setUp(self):
        super(base.TestBase, self).setUp()

        self.proxy = bootstrap.Bootstrap()
        self.app = self.proxy.transport.app
        self.srmock = ftest.StartResponseMock()


def make_app_daemon(host, port, app):
    httpd = simple_server.make_server(host, port, app)
    process = multiprocessing.Process(target=httpd.serve_forever,
                                      name='marconi_' + str(port))
    process.daemon = True
    process.start()

    return process
