# csv-file-splitter


```
usage: CSV Splitter [-h] [-l LINES_PER_FILE] [-o OUTPUTDIRECTORY]
                    [-hcn HAS_COLUMN_NAMES]
                    csv_file

Split a single CSV file into multiple smaller files. This was handy when the
original CSV file was too large to import into MicrosoftAzureStorageExplore
where trying to upload 500mb of DATA in 1 go would crash their tool. I'm sure
there are other use cases for this as well.

positional arguments:
  csv_file              CSV file path

optional arguments:
  -h, --help            show this help message and exit
  -l LINES_PER_FILE, --lines-per-file LINES_PER_FILE
                        The maximum lines in the resulting CSV files (Defaults
                        to 100)
  -o OUTPUTDIRECTORY, --outputdirectory OUTPUTDIRECTORY
                        The directory to output the split CSV files. Defaults
                        to a name similar to the original CSV file
  -hcn HAS_COLUMN_NAMES, --has-column-names HAS_COLUMN_NAMES
                        Specify if the first row of the CSV file are the
                        column names. If so, the column names will be included
                        in each resulting CSV file.
```
