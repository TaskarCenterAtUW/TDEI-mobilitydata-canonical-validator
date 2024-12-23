# TDEI-mobility-canonical-validator

This package is used to validate the canonical data.


## System requirements

| Software | Version |
|----------|---------|
| Python   | 3.10.x  |

## What this package does?

This package is used to validate the canonical data.


## Starting a new project with template

- Add `gtfs-canonical-validator` package as dependency in your `requirements.txt`
- or `pip install gtfs-canonical-validator`
- Start using the packages in your code.

## Initialize and Configuration

```python
from gtfs_canonical_validator import CanonicalValidator

canonical_validator = CanonicalValidator(zip_file=<CANONICAL_ZIP_FILE_PATH>)
report = canonical_validator.validate()
print(report)

```

### Testing

The project is configured with `python` to figure out the coverage of the unit tests. All the tests are in `tests`
folder.

- To execute the tests, please follow the commands:

  `pip install -r requirements.txt`

  `python -m unittest discover -v tests/unit_tests`

- To execute the code coverage, please follow the commands:

  `python -m coverage run --source=src/gtfs_canonical_validator -m unittest discover -s tests/unit_tests`

  `coverage html` // Can be run after 1st command

  `coverage report` // Can be run after 1st command

- After the commands are run, you can check the coverage report in `htmlcov/index.html`. Open the file in any browser,
  and it shows complete coverage details
- The terminal will show the output of coverage like this

```shell

>  python -m unittest discover -v tests/unit_tests
test_validate_failed_upload (test_canonical_validator.TestCanonicalValidator) ... ok
test_validate_successful_upload (test_canonical_validator.TestCanonicalValidator) ... ok
test_validate_successful_upload (test_canonical_validator.TestCanonicalValidatorSuccessWithDatasets) ... ok
test_get_result_url (test_constants.TestConstants) ... ok
test_get_info_failure (test_mobility_data.TestMobilityData) ... ok
test_get_info_success (test_mobility_data.TestMobilityData) ... ok
test_get_mobility_data_failure (test_mobility_data.TestMobilityData) ... ok
test_get_mobility_data_success (test_mobility_data.TestMobilityData) ... ok
test_upload_failure (test_mobility_data.TestMobilityData) ... ok
test_upload_success (test_mobility_data.TestMobilityData) ... ok

----------------------------------------------------------------------
Ran 10 tests in 69.643s

OK
```

### Coverage Report

```shell

>  coverage report
Name                                                Stmts   Miss  Cover
-----------------------------------------------------------------------
src/example.py                                          5      5     0%
src/gtfs_canonical_validator/__init__.py           20      0   100%
src/gtfs_canonical_validator/constants.py           5      0   100%
src/gtfs_canonical_validator/gtfs_validator.py      44      0   100%
src/gtfs_canonical_validator/version.py             1      0   100%
-----------------------------------------------------------------------
TOTAL                                                  75      5    93%

```