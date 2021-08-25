import os


bind = '0.0.0.0:' + str(os.getenv('FLASK_PORT', 80))
proc_name = 'Practice-Graphql'
logconfig = 'config/logging.ini'
