"""
Test support harness for doing setup.py test.
See http://ericholscher.com/blog/2009/jun/29/enable-setuppy-test-your-django-apps/.
"""
import sys

# Bootstrap Django's settings.
from django.conf import settings
settings.configure(
    DATABASES = {
        'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory;'}
    },
    INSTALLED_APPS = ['django_storymarket'],
    TEST_RUNNER = "django_nose.NoseTestSuiteRunner",
    STORYMARKET_API_KEY = 'APIKEY',
)

def runtests():
    """Test runner for setup.py test."""
    # Run you some tests.
    import django.test.utils
    runner_class = django.test.utils.get_runner(settings)
    test_runner = runner_class(verbosity=0, interactive=True)
    failures = test_runner.run_tests(['django_storymarket'])
    
    # Okay, so this is a nasty hack. If this isn't here, `setup.py test` craps out
    # when generating a coverage report via Nose. I have no idea why, or what's
    # supposed to be going on here, but this seems to fix the problem, and I
    # *really* want coverage, so, unless someone can tell me *why* I shouldn't
    # do this, I'm going to just whistle innocently and keep on doing this.
    sys.exitfunc = lambda: 0
    
    sys.exit(failures)