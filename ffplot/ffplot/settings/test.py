"""
settings to use for testing
"""
from .local import *
from .base import *

## Test settings
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = PROJECT_ROOT
TEST_DISCOVER_ROOT = PROJECT_ROOT
TEST_DISCOVER_PATTERN = "test_*"

## In memory test database
DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": ":memory:",
		"USER": "",
		"PASSWORD": "",
		"HOST": "",
		"PORT": "",
		},
	}
	