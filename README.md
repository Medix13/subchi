# Subchi

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

This script is a tool that checks for subdomains of a given domain by brute-forcing through a list of subdomains in a specified file. It uses the dns.resolver and argparse Python modules.

## Run Locally

Clone the project

```bash
git clone git@github.com:Medix13/subchi.git
```

Go to the project directory

```bash
cd subchi
```

Install Setup

```bash
python setup.py install
```

## Usage

To run the script, use the following command:

```bash
python subchi.py <domain> [-o output_file] [-s subdomains_file] [-c compare_file]
```

The domain argument is the domain to check for subdomains.

Optional arguments:

- -o, --output-file: The name of the output file where the discovered subdomains will be written. Default is output.txt.
- -s, --subdomains-file: The name of the file containing the list of subdomains to check. Default is subdomains.txt.
- -c, --compare-file: The name of the file containing the list of previously discovered subdomains. If provided, the script will compare the new discoveries with the subdomains in this file and only output the new ones.

## Example

To check for subdomains of example.com using the default subdomains.txt file and output to ~/output/example.com_output.txt, run:

```bash
python subchi.py example.com
```

To output to a different file name and use a different list of subdomains, run:

```bash
python subchi.py example.com -o example_output.txt -s custom_subdomains.txt
```

To compare against a previously discovered list of subdomains, run:

```bash
python subchi.py example.com -c previously_discovered.txt
```

## Syntax Error

If you run the script with no arguments, it will output a syntax error message:

```bash
Syntax Error - usage: subchi.py [-h] [-o OUTPUT_FILE] [-s SUBDOMAINS_FILE] [-c COMPARE_FILE] domain
```

## Contributing

Contributions are welcome! If you have a feature request or a bug to report, please open an issue on GitHub. If you'd like to contribute code, please fork the repository and submit a pull request.

## Contributing

Contributions are welcome! If you have a feature request or a bug to report, please open an issue on GitHub. If you'd like to contribute code, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE ](LICENSE.md) file for details.
