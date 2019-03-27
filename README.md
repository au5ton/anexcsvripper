# anexcsvripper


## Dependencies
- requires python 3.6+
- `pip3 install -r requirements.txt`

## Running
`./script.py example.txt`

outputs in csv format to: `grades-{dept}-{number}.csv`

## Using csv files
if using the csv files where it is necessary to import individually (Google Sheets), use `merge.sh` to combine all csv files with `grades-*.csv`
