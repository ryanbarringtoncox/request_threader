# Request Threader

This program is configured to query ebay for given search words via http. It simulates a browser user typing in search keyword and then writes the returned html locally. This is a testing experiment and the script will be genericized further if useful.

## Basic Usage 

If Python is already installed on your box, you should be able to run the script immediately like this:

```
./write_html_threaded.py
```

or

```
python write_html_threaded.py
```

The script will create a sub-directory named named with search word + timestamp (i.e. "aeroplane_out_files_1449163339") in your working directory and write the html files there.

## Configuration

The main configuration options are at the top of write_html_threaded.py.  Hopefully they are self-explanatory:

```
with_quotes = True # putting quotes around search keyword disables ebay thesauraus
num_threads = 100 # number of threads
hits_per_thread = 50 # how many successful requests per thread til completion
search_word = 'aeroplane' # ebay search word
```

At the time of this writing, 100 threads x 50 hits_per_thread yields 5,000 html files in a few short minutes.  Lowering the number of threads take more time overall and the html files are spread further over time.

*Note: If you query 100 threads x 50 hits_per_thread, you should get 5,000 valid html files written locally.  However, at the time of this writing you will also get about 200 empty files.  These represent failed html requests.  So the listing of the html file sub-directory will have 5,200 files. Makes sense? ; )*

## Meta, Graphing, etc

The meta_parser.py script logs some meta info such as min, max, mean of a write_html_threaded.py run.  It also graphs the results on a scatter plot.

You'll need to import a few things to run meta_parser.py so check out the import statements at the top of the script.  Or just run it and see what is missing.

meta_parser.py is a work in progress, intended to help you analyze the data.

Happy scraping and analyzing!
