#### Run this script before running CoreNLP.ipynb ####
#### https://pypi.python.org/pypi/corenlp-python ####
sudo pip install pexpect unidecode jsonrpclib
sudo pip install simplejson
sudo pip install wikipedia
git clone https://bitbucket.org/torotoki/corenlp-python.git
cd corenlp-python
wget http://nlp.stanford.edu/software/stanford-corenlp-full-2014-08-27.zip
unzip stanford-corenlp-full-2014-08-27.zip
python corenlp/corenlp.py