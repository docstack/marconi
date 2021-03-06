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
# See the License for the specific language governing permissions and
# limitations under the License.

"""
In-memory reference Storage Driver for Marconi.

Useful for automated testing and for prototyping storage driver concepts.
"""

from marconi.queues.storage.sqlite import driver

# Hoist classes into package namespace
ControlDriver = driver.ControlDriver
DataDriver = driver.DataDriver
