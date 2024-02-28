import os
from gtfs_canonical_validator import CanonicalValidator


def success_case():
    canonical_validator = CanonicalValidator(zip_file='./src/assets/success.zip')
    report = canonical_validator.validate()
    print(report.status)


def failure_case():
    canonical_validator = CanonicalValidator(zip_file='./src/assets/failure.zip')
    report = canonical_validator.validate()
    print(report.status)


if __name__ == "__main__":
    success_case()
    failure_case()
