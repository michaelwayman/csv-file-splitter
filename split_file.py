import os
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='CSV Splitter',
        description=(
            'Split a single CSV file into multiple smaller files.\n'
             'This was handy when the original CSV file was too large to import into '
             'MicrosoftAzureStorageExplore where trying to upload 500mb of DATA in 1 go would '
             'crash their tool. I\'m sure there are other use cases for this as well.'
        ),
    )

    # Positional mandatory arguments
    parser.add_argument('csv_file', help='CSV file path', type=str)

    # Optional arguments
    parser.add_argument(
        '-l', '--lines-per-file',
        help='The maximum lines in the resulting CSV files (Defaults to 100)',
        type=int, default=100,
    )

    parser.add_argument(
        '-o', '--outputdirectory',
        help='The directory to output the split CSV files. Defaults to a name similar to the original CSV file',
        type=str, default='',
    )

    parser.add_argument(
        '-hcn', '--has-column-names',
        help=(
            'Specify if the first row of the CSV file are the column names. '
            'If so, the column names will be included in each resulting CSV file.'
        ),

        type=bool, default=True,
    )

    args = parser.parse_args()
    return args


def write_new_file(filename, output_directory, csv_data):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    filepath = os.path.join(output_directory, filename)
    with open(filepath, 'w') as f:
        f.writelines(csv_data)


def split_csv_into_multiple_files(file_path, output_directory, lines_per_file=100, has_column_names=True):
    with open(file_path, 'r', newline='') as csv_file:
        csv_rows = []
        file_number = 1
        for i, row in enumerate(csv_file, start=1):
            if i is 1 and has_column_names:
                first_row_columns_names = row
                csv_rows.append(first_row_columns_names)
                continue

            csv_rows.append(row)

            if i % lines_per_file is 0:
                write_new_file(f'{file_number}_{file_path}', output_directory, '\n'.join(csv_rows))
                file_number += 1
                csv_rows = []
                if has_column_names:
                    csv_rows.append(first_row_columns_names)
        else:
            if len(csv_rows) > 0:
                write_new_file(f'{file_number}_{file_path}', output_directory, '\n'.join(csv_rows))


if __name__ == '__main__':
    arguments = parse_arguments()
    directory = arguments.output_directory
    if not directory:
        directory = os.path.join('.', f'{arguments.csv_file.replace(".", "_")}s')
    split_csv_into_multiple_files(
        arguments.csv_file,
        output_directory=directory,
        lines_per_file=arguments.lines_per_file,
        has_column_names=arguments.has_column_names,
    )
