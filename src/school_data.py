import csv
import logging
import os

import coloredlogs

data_file = "data/school_data.csv"
_logger = logging.getLogger(__name__)


def get_schools_data():
    coloredlogs.install(level="INFO")

    file_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.abspath(os.path.join(file_path, os.path.pardir))
    data_path = os.path.join(project_path, data_file)

    try:
        with open(data_path, encoding="cp1252") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                yield row
    except IOError as e:
        _logger.error(e)
