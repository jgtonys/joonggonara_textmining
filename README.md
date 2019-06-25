# joonggonara_textmining
Selenium Cralwer + Konlpy(twitter) + Mallet LDA



### Run Dependency & Results

Dependency : venv 



---

### Structure

- driver.py (selenium crawler starter)

- vectorize.py (preprocessing, tokenizing, LDA)

- word_cloud.py (word counting)

- source
  - location_data.json (target crawling data)
  - selenium_cralwer (main crawler)
  - mallet-2.0.8 (for mallet LDA)

- preprocess
  - dictionary.txt (new words adding twitter)

- postprocess
  - ngrams.txt
  - passtags.txt
  - passwords.txt
  - replace.txt
  - stopwords.txt

- outputs (crawling outputs)

- wordclouds (word frequency visualization)

- gephi (co-occurence network csv files)

- LDAresult (mallet LDA result html)

- venv (python dependency environment)



---

### Description



**driver.py** Data Crawling

- Recognize source – location_data.json 

- Execute source – selenium_crawler

- Result data stored to outputs folder 



**word_cloud.py** Word Counting

- Recognize preprocess,postprocess

- Visualization stored to wordclouds folder



**vectorize.py** Analyzing LDA

- Recognize preprocess, postprocess 

- Using source – mallet LDA

- Co-occurrence matrix csv stored to gephi  folder

- LDA result stored to LDAresult folder