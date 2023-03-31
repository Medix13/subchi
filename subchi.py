import dns.resolver
import sys
import argparse


def print_syntax_error():
    parser = argparse.ArgumentParser(description='Subdomain checker')
    syntax = parser.format_usage()
    print(f'Syntax Error - {syntax}')


def main():
    parser = argparse.ArgumentParser(description='Subdomain checker')
    parser.add_argument('domain', help='the domain to check')
    parser.add_argument('-o', help='output file',
                        dest='output_file', default='output.txt')
    parser.add_argument('-s', help='subdomains file',
                        dest='subdomains_file', default='subdomains.txt')
    parser.add_argument('-c', help='compare file',
                        dest='compare_file', default=None)
    args = parser.parse_args()

    domain = args.domain
    output_file = args.output_file
    subdomains_file = args.subdomains_file
    compare_file = args.compare_file

    subdomains = []
    with open(subdomains_file, 'r') as f:
        subdomains = [line.strip() for line in f.readlines()]

    discovered_subdomains = []
    with open(output_file, 'w') as f:
        for subdomain in subdomains:
            try:
                ip_value = dns.resolver.resolve(f'{subdomain}.{domain}', 'A')
                if ip_value:
                    subdomain_with_domain = f'{subdomain}.{domain}'
                    discovered_subdomains.append(subdomain_with_domain)
                    f.write(f'{subdomain_with_domain} \n')
            except dns.resolver.NXDOMAIN:
                pass
            except dns.resolver.NoAnswer:
                pass
            except KeyboardInterrupt:
                sys.exit(1)

    if compare_file:
        with open(compare_file, 'r') as f:
            compare_subdomains = set(line.strip() for line in f.readlines())
            new_subdomains = set(discovered_subdomains) - compare_subdomains
            print("New Subdomains found: ")
            for subdomain in new_subdomains:
                print(subdomain)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_syntax_error()
    else:
        main()
