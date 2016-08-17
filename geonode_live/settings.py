# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
import geonode
from geonode.settings import *
#
# General Django development settings
#

SITENAME = 'geonode_live'

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
GEONODE_ROOT = os.path.abspath(os.path.abspath(geonode.__file__))
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "geonode_live.wsgi.application"


# Load more settings from a file called local_settings.py if it exists
try:
    from local_settings import *
except ImportError:
    pass

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

# Location of url mappings
ROOT_URLCONF = 'geonode_live.urls'

# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

INSTALLED_APPS += ("osgeo_importer","polls")
DJMP_AUTHORIZATION_CLASS = 'djmp.guardian_auth.GuardianAuthorization'
TILESET_CACHE_DIRECTORY = os.path.join(LOCAL_ROOT, 'cache/layers')
USE_DISK_CACHE=True
LAYER_PREVIEW_LIBRARY = 'geoext'
