## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required libraries:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   bazel run //:compile_requirements.update
   ```

## Usage

Run the script by executing:

```bash
python scraper.py

# Export ENDOR_TOKEN. //:main is a py_binary rule and //:test_py3_image is py3_image rule
endorctl scan -n somak_test.amylraj-test --enable git,analytics --languages=python -a https://api.staging.endorlabs.com -p /Users/aswinmylraj/Endor/test_repos/bazel/integration-test-bazel-python --use-bazel=true --bazel-include-targets="//:test_py3_image,//:main" --log-level=debug --token=$ENDOR_TOKEN --verbose --rescan-code


```
