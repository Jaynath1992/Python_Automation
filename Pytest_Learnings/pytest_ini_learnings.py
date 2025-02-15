[pytest]
log_cli = true
log_cli_level = 22
log_format = %(asctime)s.%(msecs)03d [%(levelname)s] [%(filename)s:%(funcName)s:%(lineno)d] %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
log_file_format = %(asctime)s.%(msecs)03d [%(levelname)s] [%(threadName)s] [%(filename)s:%(funcName)s:%(lineno)d] %(message)s
log_file_date_format = %Y-%m-%d %H:%M:%S

filterwarnings =
    ignore:.*Call to deprecated function .*(fields|_options|_valid_input_keys|validator_functions).*:DeprecationWarning
    ignore:^Could not append AuthInteractivePassword, not allowed auth type keyboard-interactive$
    ignore:.*imp:DeprecationWarning
    ignore:.*(notifyAll|setDaemon):DeprecationWarning
    ignore:.*coroutine:RuntimeWarning
    ignore::pytest.PytestCacheWarning
    ignore:.*invalid escape sequence.*:DeprecationWarning
    ignore:.*is deprecated and slated for removal.*:DeprecationWarning
    ignore:.*"is" with a literal.*:SyntaxWarning
    ignore::DeprecationWarning
    ignore:.*Unknown option directConnection.*:UserWarning
    ignore:.*TripleDES has been moved to.*
