#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import url, patterns


urlpatterns = patterns('filebrowser.views',
  # Base view
  url(r'^$', 'index', name='index'),

  # Catch-all for viewing a file (display) or a directory (listdir)
  url(r'^view=(?P<path>[\s\S.]*)$', 'view', name='view'),

  url(r'^listdir=(?P<path>[\s\S.]*)$', 'listdir', name='listdir'),
  url(r'^display=(?P<path>[\s\S.]*)$', 'display', name='display'),
  url(r'^stat=(?P<path>[\s\S.]*)$', 'stat', name='stat'),
  url(r'^content_summary=(?P<path>[\s\S.]*)$', 'content_summary', name='content_summary'),
  url(r'^download=(?P<path>[\s\S.]*)$', 'download', name='download'),
  url(r'^status$', 'status', name='status'),
  url(r'^home_relative_view=(?P<path>[\s\S.]*)$', 'home_relative_view', name='home_relative_view'),
  url(r'^edit=(?P<path>[\s\S.]*)$', 'edit', name='edit'),

  # POST operations
  url(r'^save$', 'save_file'),
  url(r'^upload/file$', 'upload_file', name='upload_file'),
  url(r'^extract_archive', 'extract_archive_using_batch_job', name='extract_archive_using_batch_job'),
  url(r'^compress_files', 'compress_files_using_batch_job', name='compress_files_using_batch_job'),
  url(r'^trash/restore$', 'trash_restore', name='trash_restore'),
  url(r'^trash/purge$', 'trash_purge', name='trash_purge'),
  url(r'^rename$', 'rename', name='rename'),
  url(r'^mkdir$', 'mkdir', name='mkdir'),
  url(r'^touch$', 'touch', name='touch'),
  url(r'^move$', 'move', name='move'),
  url(r'^copy$', 'copy', name='copy'),
  url(r'^set_replication$', 'set_replication', name='set_replication'),
  url(r'^rmtree$', 'rmtree', name='rmtree'),
  url(r'^chmod$', 'chmod', name='chmod'),
  url(r'^chown$', 'chown', name='chown'),
)

# API
urlpatterns += patterns('filebrowser.api',
  url(r'^api/get_filesystems/?', 'get_filesystems', name='get_filesystems'),
)
