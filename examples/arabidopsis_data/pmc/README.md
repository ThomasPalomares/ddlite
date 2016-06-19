#Brief explanation parser

This parser goes from a list of PMC ids (such as round1/PMC_OA_ids_v2.txt) and outputs a json file where each line is a sentence in one of the documents.

## Download the xml files from the PMC ids list

First, unzip the PMC_OA_list.csv.zip (with 'unzip PMC_OA_list.csv.zip' or simply by double clicking on it).
Then, the following steps are:
* Create a folder in which the files will be downloaded `mkdir round-n; cd round-n`
* Run the file preproc.py which outputs a file of PMC urls, PMC_url_list.txt: `../preproc.py ../PMC_OA_list.csv pmc_list_ids.txt`
* download each file whose link is in PMC_url_list.txt: `wget -i PMC-url_list.txt`
* Unzip all the compressed downloaded file: `tar -zxvf *.tar.gz` (if this part doesn't work, it can be done manually with cmd+A and double clicking on all the files)
* Remove all the non xml files: 
`rm *.tar.gz;
find . -mindepth 2 -type f -print -exec mv {} . \;
rm !(*.nxml);
rm -rf */;
rm PMC_url_list.txt`
* Parsing the xml files to json files: this was done installing the dd-genomics repo parser folder. Then run, with ${APP_HOME} the path to the forked ddlite repo: `./run_parser.sh ${APP_HOME}/arabidopsis_data/pmc/round-n/ pmc PMC_round_n`
* The final json file you are interested in will be PMC_round_n.json ! (you can in particular delete PMC_round_n.md.tsv and PMC_round_n.om.txt)