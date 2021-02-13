# Data_Projects

Welcome to my Respository!

Everything part of this repository is either a research project or a personal project of mine. 

# 1. Predicting Investor Sentiments to IPOs

When a firm is preparing to release an IPO, they must first submit their Prospectus to SEBI. Of the various sections of the Prospectus, we are taking a look at the Risk Factors section, one that details every risk/uncertainty the company is exposed to. According to previously conducted research, the tone or sentiment associated with the section can directly affect the investor's perception of the IPO and impact the book building process which can then directly affect the performance of the IPO on its first day of trading.  
Using the above knowledge, this program uses the help of VADER (Valence Aware Dictionary and sEntiment Reasoner) and a custom-made sentiment score dictionary to evaluate the sentiment associated with the section. The output is given in the form of a positive, negative, neutral and compound score. The compound score is obtained after normalizing the three prior scores. 
An extremely positive text would return a compound score of +1.0, an extremely negative text would return a compound score of -1.0 and neutral text would return 0.0.

## List of Requirements

* nltk: https://www.nltk.org/install.html
* VADER: https://pypi.org/project/vaderSentiment/

The Risk Factors section of the IPO Prospectus you're interested in must be inputted into the program as a text file. Please refer to the repo for the list of positive and negative words. 

In case you're curious to know how this list came about, feel free to check out: https://sraf.nd.edu/textual-analysis/resources/


# 2. Market Index Volatility Forecasting Model 
As a result of the Covid-19 pandemic, India was thrown into a technical recession. To better understand the impact of this event on the stock market, we can reasonably look to the Bombay Stock Exchange's Market Index, known as Sensex, and its volatility. The Sensex is composed of the 30 largest and most actively traded stocks on the exchange and is considered to be one of the broadest market indices in the country. 

For this implementation of a volatility prediction model, we have adopted two types of the Generalized AutoRegressive Conditional Heteroskedasticity (GARCH) Model: Standard GARCH and the GJR-GARCH model. 

## List of Requirements

* arch: https://pypi.org/project/arch/ 
* pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

You can download the past n days worth of Sensex data from here: https://www.bseindia.com/Indices/IndexArchiveData.html
Convert the downloaded csv to xlsx if you're facing issues.


