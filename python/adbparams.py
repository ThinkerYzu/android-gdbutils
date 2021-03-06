# vi: set tabstop=4 shiftwidth=4 expandtab:
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla Corporation code.
#
# The Initial Developer of the Original Code is the Mozilla Corporation.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Jim Chen <jimnchen@gmail.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import gdb

class ADBPath(gdb.Parameter):
    '''When set, use the specified path when launching ADB instead of "adb"'''
    set_doc = 'Set path of Android ADB tool'
    show_doc = 'Show path of Android ADB tool'

    def __init__(self):
        super(ADBPath, self).__init__('adb-path',
                gdb.COMMAND_SUPPORT, gdb.PARAM_OPTIONAL_FILENAME)
        self.value = None
        self.get_set_string()

    def get_set_string(self):
        self.value = self.value.strip() if self.value else 'adb'
        return 'New Android ADB tool is "' + self.value + '"'

    def get_show_string(self, svalue):
        return 'Android ADB tool is "' + svalue + '"'

path = ADBPath()

class ADBDevice(gdb.Parameter):
    '''When set, use the specified device when launching ADB'''
    set_doc = 'Set device used by ADB'
    show_doc = 'Show device used by ADB'

    def __init__(self):
        super(ADBDevice, self).__init__('adb-device',
                gdb.COMMAND_SUPPORT, gdb.PARAM_STRING)
        self.value = None

    def get_set_string(self):
        self.value = self.value if self.value else ''
        return 'New ADB device is "' + self.value + '"'

    def get_show_string(self, svalue):
        return 'ADB device is "' + svalue + '"'

device = ADBDevice()

