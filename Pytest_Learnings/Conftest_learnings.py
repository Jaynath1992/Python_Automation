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

