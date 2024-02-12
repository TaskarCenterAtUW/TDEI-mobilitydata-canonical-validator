import os
from mobility_canonical_validator import CanonicalValidator

if __name__ == "__main__":
    canonical_validator = CanonicalValidator(zip_file='./src/assets/valid.zip')
    report = canonical_validator.validate()
    # print(report)
