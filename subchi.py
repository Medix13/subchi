import dns.resolver
import argparse
import os
import logging
import art
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor, as_completed


class SubdomainChecker:
    def __init__(self, domain, subdomains_file, output_file, record_type, output_dir):
        self.domain = domain
        self.subdomains_file = subdomains_file
        self.output_file = output_file
        self.record_type = record_type
        self.output_dir = output_dir

    def check_subdomain(self, subdomain):
        try:
            answers = dns.resolver.resolve(
                f'{subdomain}.{self.domain}', self.record_type)
            for rdata in answers:
                if rdata:
                    subdomain_with_domain = f'{subdomain}.{self.domain}'
                    print(
                        f"{subdomain_with_domain} ({self.record_type}: {rdata})")
                    return subdomain_with_domain
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass

    def run(self):

        subdomains = []
        with open(self.subdomains_file, 'r') as f:
            subdomains = [line.strip() for line in f.readlines()]

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.check_subdomain, subdomain)
                       for subdomain in subdomains]
            discovered_subdomains = [
                future.result() for future in as_completed(futures) if future.result()]

        if len(discovered_subdomains) == 0:
            print('No subdomains found.\n')
        else:
            with open(os.path.join(self.output_dir, f"{self.domain}_{self.output_file}"), 'w') as f:
                for subdomain in discovered_subdomains:
                    f.write(f'{subdomain} \n')


def main():
    parser = argparse.ArgumentParser(description='Subdomain checker')
    parser.add_argument('domain', help='the domain to check')
    parser.add_argument('-o', help='output file',
                        dest='output_file', default='output.txt')
    parser.add_argument('-s', help='subdomains file',
                        dest='subdomains_file', default='subdomains.txt')
    parser.add_argument('-c', help='compare file',
                        dest='compare_file', default=None)
    parser.add_argument(
        '-t', help='DNS record type (default is A)', dest='record_type', default='A')
    args = parser.parse_args()

    domain = args.domain
    output_file = args.output_file
    subdomains_file = args.subdomains_file
    compare_file = args.compare_file
    record_type = args.record_type
    output_dir = 'output'

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s')
    logging.info(
        f'Starting subdomain enumeration for {domain} (record type: {record_type})\n')

    checker = SubdomainChecker(
        domain, subdomains_file, output_file, record_type, output_dir)
    checker.run()

    if compare_file:
        with open(compare_file, 'r') as f:
            compare_subdomains = set(line.strip() for line in f.readlines())

        with open(os.path.join(output_dir, f"{domain}_{output_file}"), 'r') as f:
            discovered_subdomains = set(line.strip() for line in f.readlines())

        new_subdomains = discovered_subdomains - compare_subdomains
        if len(new_subdomains) != 0:
            print(
                '\n****************************\n    New Subdomains found:\n****************************\n')
            for subdomain in new_subdomains:
                print(subdomain)


if __name__ == "__main__":
    logo = art.text2art('Subchi', font='doom')
    colored_logo = colored(logo, 'red')
    print(colored_logo)

    main()
