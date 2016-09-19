# Get started
virtualenv recommended to isolate python bin and pip packages


From within the project folder, call:

```
virtualenv . && source bin/activate && pip3 install -r requirements.txt
```



## Usage

```
python3 main.py --file ./mkg_lido--mkgddb-sub-cd-profil_20160913.xml -fc "Porträtfotografie" -v -o ./downloads
```


## TODO
- [x] filter for classification terms
- [ ] filter for several classification terms
- [ ] fuzzy filtering
- [ ] threaded downloads
- [ ] progress bar
- [ ] option for getting all images for a record
- [ ] download via resourceWrap urls
- [ ] idle indicator
- [ ] option: create output_directory if not existant
- [ ] fix empty image bug