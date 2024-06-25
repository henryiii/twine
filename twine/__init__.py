"""Top-level module for Twine.

The contents of this package are not a public API. For more details, see
https://github.com/pypa/twine/issues/194 and https://github.com/pypa/twine/issues/665.
"""

# Copyright 2018 Donald Stufft and individual contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
__all__ = (
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
)

__copyright__ = "Copyright 2019 Donald Stufft and individual contributors"

import importlib_metadata

metadata = importlib_metadata.metadata("twine")


__title__ = metadata.get("name")
__summary__ = metadata.get("summary")
__uri__ = metadata.get("home-page")
__version__ = metadata.get("version")
__author__ = metadata.get("author")
__email__ = metadata.get("author-email")
__license__ = None
