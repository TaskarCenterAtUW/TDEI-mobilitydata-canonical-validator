# TDEI-mobility-canonical-validator

This package is used to validate the canonical data. This library is used to validate all the GTFS datasets that are compatible with [Mobility Data](https://gtfs-validator.mobilitydata.org/)

The library pushes the dataset `zip` file to [Mobility Data](https://gtfs-validator.mobilitydata.org/) and fetches the report.

The reference for GTFS is available [here](https://gtfs.org/documentation/schedule/reference/)

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
  
  `python -m unittest test_sample.MyTestCase.test_function`  - To run a single test case

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

#### Running validation on Local files
- Use the code in [example.py](./src/example.py) to replace the dataset sources and run the code to get the validation report.
- An example report can be found at [example-report.json](./src/assets/example-report.json)
- The report explanation can be found [here](https://gtfs-validator.mobilitydata.org/rules.html)


## Deployment:

- The library can be pushed to [TestPy](https://test.pypi.org/project/gtfs-canonical-validator/) or [PYPI](https://pypi.org/project/gtfs-canonical-validator/)
### Deploy to TestPy
- On every push to `dev` branch, a workflow is triggered which publishes the updated version to TestPy

### Deploy to PyPI
- This happens whenever a tag/release is created with `*.*.*` notation (eg. 0.0.8)
- To change the version, change the version at [version.py](./src/gtfs_canonical_validator/version.py)
- To release a new version:
  - Go to Github link of this repository
  - Under [releases](https://github.com/TaskarCenterAtUW/TDEI-mobilitydata-canonical-validator/releases), click on `Draft a new release`
  - Under `choose a new tag`, add a new tag `v*.*.*` , Generate Release notes
  - Choose `main` branch for release
  - Publish the release.
- This release triggers a workflow to generate the new version of the Package.
- The new package will be available at https://pypi.org/project/gtfs-canonical-validator/