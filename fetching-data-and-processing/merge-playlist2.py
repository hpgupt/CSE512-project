def compare_and_write_unique_urls(file1, file2, output_file):
    # Read URLs from the first file
    with open(file1, 'r') as f1:
        urls_file1 = set(f1.read().splitlines())

    # Read URLs from the second file
    with open(file2, 'r') as f2:
        urls_file2 = set(f2.read().splitlines())

    # Find URLs that are in file1 but not in file2
    unique_urls = urls_file1 - urls_file2

    # Write these unique URLs to the output file
    with open(output_file, 'w') as out:
        for url in unique_urls:
            out.write(url + '\n')

# Example usage:
compare_and_write_unique_urls("D:\\workspace\\MLProject\\merged_urls_2.txt", "D:\\workspace\\MLProject\\merge-all-1.txt", 'unique_urls.txt')
