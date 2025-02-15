"""
#################################################
Basic_fixtures and hooks examples taken
#################################################
"""

def pytest_addoption(parser):
    parser.addoption('--basedir',
                     action='store',
                     dest='basedir',
                     help='Base repo path')
    parser.addoption('--testbed',
                     action='store',
                     dest='testbed',
                     help='Testbed path - yml ')
    parser.addoption('--hyperscaler',
                     action='store',
                     dest='hyperscaler',
                     help='Hyperscaler aws, azure or gcp ')
    parser.addoption('--outdir',
                     action='store',
                     dest='outdir',
                     help='Dir for saving test run-logs of all types')
    parser.addoption('--projectid',
                     action='store',
                     dest='projectid',
                     help='Project id specific operations')
    parser.addoption('--token',
                     action='store',
                     dest='token',
                     help='Project id specific token')




@pytest.fixture(scope="function", autouse=True)
def get_test_id(request):
    """Get tc_id from test function pametrize and store it in request.cls.tc_id"""
    tc_id = request.node.callspec.params["tc_id"]
    request.cls.tc_id = tc_id


@pytest.hookspec()
def pytest_xdist_setupnodes(config, specs):
    """Create timestamp folder for parallel worker logs"""
    result_path = os.path.join(globals.LOGS_DIR, logs_folder_timestamp)
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    globals.TIMESTAMP = logs_folder_timestamp

# content of conftest.py
@pytest.hookimpl()
def pytest_configure(config):
    """Configure pytest to support multiple worker nodes"""
    worker_id = os.environ.get("PYTEST_XDIST_WORKER")
    run_id = os.environ.get("RUN_ID")
    logs_dir = globals.LOGS_DIR

    # if run_id is defined; the tests are running in moonstone with a unique logs folder for each run
    if run_id is not None:
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        file_name = os.path.join(logs_dir, f"tests_{run_id}.log")
        logger.set_out_file(file_name, "DEBUG")
    # if multiple worker (>= 1) nodes are found create file with worker id
    elif worker_id is not None:
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        file_name = os.path.join(logs_dir, f"tests_{worker_id}.log")
        logger.set_out_file(file_name, "DEBUG")
    # if n=0 was specified, create just default 0 worker node. It will not use xdist prallel but still will produce the same format of log
    else:
        result_path = os.path.join(logs_dir, logs_folder_timestamp)
        if not os.path.exists(result_path):
            os.makedirs(result_path)
        globals.TIMESTAMP = logs_folder_timestamp
        file_name = os.path.join(result_path, "tests_gw0.log")
        logger.set_out_file(file_name, "DEBUG")

def pytest_terminal_summary(terminalreporter, config):
    """Add info abot workers logs and path where they can be found"""
    result_logs_path = os.path.join(globals.LOGS_DIR, globals.TIMESTAMP)
    if os.path.exists(result_logs_path):
        only_files = [
            f
            for f in os.listdir(globals.LOGS_DIR)
            if os.path.isfile(os.path.join(globals.LOGS_DIR, f))
        ]
        for file_name in only_files:
            shutil.move(
                os.path.join(globals.LOGS_DIR, file_name),
                os.path.join(globals.LOGS_DIR, globals.TIMESTAMP, file_name),
            )
        print(f"Logs path: {result_logs_path}")
        print(f"Logs files: {os.listdir(result_logs_path)}")

def pytest_itemcollected(item):
    """change test name, so qTest api can consume xl report"""
    if hasattr(item._request.node, "callspec"):
        item._nodeid = item._request.node.callspec.params["tc_id"]

def pytest_exception_interact(call, report):
    """Execute on exception, if exception is raised during failed teardown, set global failed_teardown flag to True"""
    global failed_teardown  # pylint: disable=global-statement
    if call.when == "teardown":
        failed_teardown = True

def pytest_runtest_makereport(item, call):
    """Execute on test report, if exception is raised during failed teardown, set global failed_teardown flag to True"""
    if call.excinfo and call.when == "teardown":
        parent = item.parent
        parent._previousfailed = item.nodeid

def pytest_runtest_setup(item):
    """Execute on test setup, if previous test teardown failed, mark current test as xfail"""
    # global failed_teardown  # pylint: disable=global-statement
    previous_failed = getattr(item.parent, "_previousfailed", None)
    if failed_teardown:
        pytest.xfail(f"Previous test teardown failed: {previous_failed}")


def pytest_configure(config):
    sys.path.append(config.option.basedir)
    import pytest_cvs_fw.lib.init_cfg as cfg
    global cfg
    config.option.importmode = 'append'
    config.option.self_contained_html = 'True'
    run_id = gen_run_id()

    if config.option.outdir != None:
        cfg._cfg_out_dir = config.option.outdir + '/RUN_' + run_id
        os.mkdir(cfg._cfg_out_dir)

        config.option.htmlpath = cfg._cfg_out_dir + '/run.html'
        config.option.xmlpath = cfg._cfg_out_dir + '/run.xml'
        config.option.log_file = cfg._cfg_out_dir + '/run.log'
    config.option.log_format = '[%(asctime)s], %(levelname)s, %(filename)s, %(funcName)s, %(lineno)d  ::  %(message)s'
    config.option.log_level = 'INFO'
    config.option.log_date_format = '%Y-%m-%d %H:%M:%S'
    config.option.log_file_format = '[%(asctime)s], %(levelname)s, %(filename)s, %(funcName)s, %(lineno)d  ::  %(message)s'
    config.option.log_file_level = 'DEBUG'
    config.option.log_file_date_format = '%Y-%m-%d %H:%M:%S'
    config.option.log_cli = True
    config.option.log_cli_format = '[%(asctime)s], %(levelname)s, %(filename)s, %(funcName)s, %(lineno)d  ::  %(message)s'
    config.option.log_cli_date_format = '%Y-%m-%d %H:%M:%S'
    if not config.option.token:
        config.option.token = False


def pytest_report_header(config):
    st = '\n===> LOG DIR  : {0} \n'.format(config.option.log_file)
    st += '===> HTML DIR : {0}  \n'.format(config.option.htmlpath)
    st += '===> XML DIR  : {0} \n'.format(config.option.xmlpath)
    return colored(st, 'blue')


def pytest_runtest_setup(item):
    cfg._cfg_module = item.module.__name__
    mod_log = get_mod_logger(cfg._cfg_module)
    mod_log.info('{0}'.format('=' * 80))
    msg = 'STARTED : {0} '.format(item.name)
    mod_log.info('{0}'.format(msg.center(75, ' ')))
    mod_log.info('{0}'.format('=' * 80))


def pytest_unconfigure(config):
    """ called before test process is exited."""
    if config.option.log_file:
        TerminalReporter(config).write('\n')
        TerminalReporter(config).write_sep(
            '-', 'generated log file: ' + config.option.log_file)
        TerminalReporter(config).write('\n\n')


@hookspec(firstresult=True)
def pytest_report_teststatus(report):
    """ return result-category, shortletter and verbose word for reporting.
    Stops at first non-None result, see :ref:`firstresult` """
    report.toterminal


def pytest_terminal_summary(terminalreporter, exitstatus):
    """Add a section to terminal summary reporting. TBD """
    pass


@pytest.fixture(scope='session')
def pre_test(request):
    """
    Session/RUNID level configs/setup
    """
    log.info('Executing Pre-test ')
    log.info('Initialize framework!!')

    input_dict = {}
    input_dict['iniconfig'] = request.config.option
    input_dict['outdir'] = get_out_dir()
    input_dict['run_id'] = get_run_id()
    input_dict['basetemp'] = request.config.option.basedir
    input_dict['tb_path'] = request.config.option.testbed
    input_dict['user_lib'] = input_dict['basetemp'] + '/lib/'
    input_dict['hyperscaler'] = request.config.option.hyperscaler
    input_dict['projectid'] = request.config.option.projectid

    f = open(input_dict['tb_path'])
    data = json.load(f)
    f.close()

    #log.info('%s' %data)
    request.config.option.testsuite = data
    request.config.option.cvp1p_obj = cvp_1p()
    request.config.option.cvp3p_obj = cvp_3p()
    request.config.option.ccfe_obj = ccfe_1p()
    request.config.option.cvi_obj = cvi()
    request.config.option.gcloud_obj = gcloud_api()
    input_dict['testsuite'] = request.config.option.testsuite
    request.config.option.hyperscaler = [
        i for i in input_dict['testsuite'].keys()
    ][0]
    fw_init(**input_dict)

    def post_test():
        """
        Session level deconfig/cleanup/teardown
        """
        log.info('Executing Post test')

    request.addfinalizer(post_test)

def pytest_html_report_title(report):
    """Update the HTML report title."""
    report.title = "Atom Backup Restore Suite"


def pytest_configure(config):
    """Add custom markers to the pytest configuration."""
    create_markers = [
        ('create', 'All Create Tests'),
        ('create_delete', 'Create/Delete Tests'),
        ('create_negative', 'Negative create Tests')]
    volume_markers = [
        ('volume', 'Volume Tests')]
    markers = [*create_markers, *volume_markers]

    register_pytest_markers(config, custom_markers=markers)

"""Common conftest.py PyTest hooks."""
from typing import List

import datetime
import functools
import os
import pathlib
import sys
import traceback

import pytest
from py.xml import html  # pylint: disable=E0401, E0611

from cbsqa.lib import (
    keeper,
    logger,
    report as report_lib
)
from cbsqa.lib.k8smanage import k8s

# Collected Environment Variables
# HOST_FILE and LOG_DIR should be the default, but also allowing for HST_FILE and ART_DIR for Moonstone.
LOG_DIR = os.environ.get('ART_DIR') or os.environ.get('LOG_DIR') or '/tmp/pytest/'
HOST_FILE = os.environ.get('HST_FILE') or os.environ.get('HOST_FILE')
LOG_FILE = os.environ.get('LOG_FILE') or 'test.log'

# Critical Error Handling Variables
_SKIP_TESTS_ON_CRIT_ERROR = False
_CRITICAL_ERROR_TB = None

# Check to see if running in Moonstone
IN_MOONSTONE = k8s.k8s.executing_in_moonstone()
if IN_MOONSTONE:
    # This indicates that this test is being ran in Moonstone, so generate a test log file since the
    # Moonstone service doesn't currently use the --log-file option.
    # NOTE: The file must be named "tests_gw0.log" for Moonstone to correctly link the file.
    LOG_FILE = 'tests_gw0.log'

_LOG_PATH = f'{LOG_DIR}/{LOG_FILE}'
_REPORT_HTML_PATH = f'{LOG_DIR}/report.html'
_REPORT_JUNIT_PATH = f'{LOG_DIR}/junit.xml'
_CRITICAL_ERROR_PATH = f'{LOG_DIR}/critical_failure.txt'

_log = logger.get_log(__name__)
_keeper = keeper.get_keeper()


_REQUIRED_ENV_VARS = ['HOST_FILE', 'LOG_DIR', 'LOG_FILE']
"""Using environment variables since they are a bit easier to work with from a Jenkins perspective

HOST_FILE: Path to the host YAML file containing resource details. For Moonstone, HST_FILE is also
    accepted.
LOG_DIR: Path to the directory where the logs are to be store. If it doesn't exist, it will be created.
    For Moonstone, ART_DIR is also accepted. Will default to /tmp/pytest/.
LOG_FILE: Name of the log file to store in the LOG_DIR. Will default to test.log unless in Moonstone,
    which will default to test_gw0.log.
"""

LOG_PODS = ['cloud-volumes-service', 'cloud-volumes-infrastructure', 'anf-rp']
"""Pods to log on test failure."""

LOG_POD_SINCE = datetime.timedelta(minutes=10)
"""Pod logs to store since the the last 10 minutes."""

DEFAULT_TB_STYLE = 'short'
"""Default traceback style for PyTest if not specified as --tb in command."""

DEFAULT_SHOW_CAPTURE = 'no'
"""Default showcapture for PyTest if not specified as --show-capture in command."""


# NOTE: This decorator is defined here and not in _decorators.py to prevent circular imports.
def ignore_exceptions(condition: bool = None):
    """Decorator to ignore exceptions raised in the decorated method.

    This is particularly helpful when preventing PyTest INTERNALERROR from being raised.

    :param condition: If specified, the exceptions will only be ignored if the condition is True.
    """
    def decorator(func):
        if condition is not None and not condition:
            return func

        @functools.wraps(func)
        def ignore_exc_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:  # pylint: disable=broad-exception-caught
                _log.exception(f'Exception occurred in {func.__name__}: {e}')
        return ignore_exc_wrapper
    return decorator


def pytest_configure(config):
    """Set the default PyTest configurations if not already set."""
    if config.getoption('tbstyle') == 'auto':
        config.option.tbstyle = DEFAULT_TB_STYLE
    if not config.getoption('log_file'):
        config.option.log_file = _LOG_PATH
    if not config.getoption('htmlpath'):
        config.option.htmlpath = _REPORT_HTML_PATH
        config.option.self_contained_html = True
    if not config.getoption('xmlpath'):
        config.option.xmlpath = _REPORT_JUNIT_PATH
    if config.getoption('showcapture') == 'all':
        config.option.showcapture = DEFAULT_SHOW_CAPTURE


@ignore_exceptions(condition=IN_MOONSTONE)
@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session) -> None:  # pylint: disable=unused-argument
    """Ensure the host file and log directory exists, storing the values in the Keeper.

    Note: this is the earliest PyTest hook that allows for logging.
    """
    msg = [f'Execution Command: {" ".join(sys.argv)}',
           f'HOST_FILE={HOST_FILE}, LOG_DIR={LOG_DIR}, LOG_FILE={LOG_FILE}']
    _log.suite('\n'.join(msg))

    msg = (f'One or more of the following required environment variables have not been '
           f'defined: {_REQUIRED_ENV_VARS}')
    if not all([HOST_FILE, LOG_DIR, LOG_FILE]):
        _log.error(msg)
        raise ValueError(msg)

    host_file = pathlib.Path(HOST_FILE)
    log_dir = pathlib.Path(LOG_DIR)
    log_file = pathlib.Path(LOG_FILE)

    msg = (f'The HOST_FILE environment variable must be populated with a filepath of a host file that '
           f'exists: {host_file}')
    assert host_file.exists(), msg

    if not log_dir.exists():
        log_dir.mkdir(mode=0o777, parents=True)

    _keeper.host_file = host_file
    _keeper.log_dir = log_dir
    _keeper.log_file = log_file


@ignore_exceptions(condition=IN_MOONSTONE)
@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):  # pylint: disable=unused-argument
    """Generate the test summary.txt and build_version.txt if executed locally."""

    # Generate build version report if executed locally.
    k8s_fms = _keeper.k8s_fms or []
    if not k8s_fms:
        k8s_fms = [k8s_fm] if (k8s_fm := _keeper.k8s_fm) else []

    for i, k8s_fm in enumerate(k8s_fms):
        filepath = f'{LOG_DIR}/build_version.txt' if i == 0 else f'{LOG_DIR}/build_version_{i}.txt'
        report_lib.generate_build_report(
            k8s_fm=k8s_fm,
            filepath=filepath,
            log_output=True,
            raise_on_error=False)

    # Generate test summary if jUnit XML file is present.
    xmlpath = session.config.option.xmlpath
    if xmlpath:
        filepath = f'{LOG_DIR}/summary.txt'
        report_lib.generate_test_summary(
            xml_file=xmlpath,
            crit_fail_path=_CRITICAL_ERROR_PATH,
            filepath=filepath,
            log_output=True,
            raise_on_error=False)
    else:
        _log.warning('No jUnit XML file found, unable to generate summary.')


def pytest_runtest_call(item):
    """Skip remaining tests if a critical failure occurs in setup or teardown."""
    if _SKIP_TESTS_ON_CRIT_ERROR and _CRITICAL_ERROR_TB:
        pytest.skip(f"Skipping {item.name} execution due to critical failure.")


@pytest.hookimpl(hookwrapper=True)
def pytest_exception_interact(node, call, report):  # pylint: disable=unused-argument
    """Store pod logs on test failure and determine critical error."""
    yield

    k8s_fms: List[k8s.k8s]

    # Store pod logs on test failure.
    if report.failed:
        k8s_fms = _keeper.k8s_fms or []
        if not k8s_fms:
            k8s_fms = [k8s_fm] if (k8s_fm := _keeper.k8s_fm) else []

        _log.info(f'Storing the logs for the following pods due to failure in test {node.name}')
        duration = int(max(LOG_POD_SINCE.total_seconds(), call.duration))
        for i, k8s_fm in enumerate(k8s_fms):
            k8s_fm.store_pod_logs(
                pods=LOG_PODS,
                artifact_dir=_keeper.log_dir,
                since_seconds=duration,
                suffix=f'{node.name}-{i}',
                ignore_errors=True)

    # Determine if a critical error occurred, write to a file and skip remaining tests.
    global _CRITICAL_ERROR_TB  # pylint: disable=global-statement
    if report.failed and _SKIP_TESTS_ON_CRIT_ERROR:

        if (setup_report := getattr(node, 'report_setup', None)) and setup_report.failed:
            _CRITICAL_ERROR_TB = setup_report.longreprtext
        if (teardown_report := getattr(node, 'report_teardown', None)) and teardown_report.failed:
            _CRITICAL_ERROR_TB = teardown_report.longreprtext

        if _CRITICAL_ERROR_TB:
            _log.error('Skipping remaining tests due to critical failure in setup or teardown.')
            with open(_CRITICAL_ERROR_PATH, 'w', encoding='utf-8') as f:
                f.write(_CRITICAL_ERROR_TB)
            node.config.option.exitfirst = True


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):  # pylint: disable=unused-argument
    """Append log filepath to HTML report"""
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield

    report = outcome.get_result()
    setattr(item, f'report_{report.when}', report)

    extra = getattr(report, "extra", [])
    if report.when == "call":

        # always add url to report
        extra.append(pytest_html.extras.url(LOG_FILE, name="Log File"))
        report.extra = extra


def pytest_html_results_summary(prefix, summary, postfix):  # pylint: disable=unused-argument
    """Update the HTML summary."""
    prefix.extend([html.a("Show Debug Logs", href=LOG_FILE)])


def skip_tests_on_critical_error(skip: bool):
    """If True, when a critcal error is hit, any remaining test cases will be skipped."""
    global _SKIP_TESTS_ON_CRIT_ERROR  # pylint: disable=global-statement
    _SKIP_TESTS_ON_CRIT_ERROR = skip


def _hit_critical_error():
    """Call to indicate a critical error occurred."""
    global _CRITICAL_ERROR_TB  # pylint: disable=global-statement

    _CRITICAL_ERROR_TB = traceback.format_exc()
    _log.error('!!! CRITICAL ERROR !!!')
