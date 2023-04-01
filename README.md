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

Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

To run the script, use the following command:

```bash
python subchi.py <domain> [-o output_file] [-s subdomains_file] [-c compare_file]
```

where:

- <domain>: the domain to check for subdomains
- output_file: (optional) the file to output discovered subdomains to (default is output.txt)
- subdomains_file: (optional) the file containing a list of subdomains to check (default is subdomains.txt)
- compare_file: (optional) the file containing a list of previously discovered subdomains to compare against and print new subdomains found

## Example

To check for subdomains of example.com using the default subdomains.txt file and output to output.txt, run:

```bash
python subchi.py example.com
```

To output to a different file and use a different list of subdomains, run:

```bash
python subchi.py example.com -o subdomains.txt -s output.txt
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
