import os
import Quandl
import urllib2
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


def loadSoup(url):
    return BeautifulSoup(urllib2.urlopen(url).read())


def load_yahoo_opinions_for_ticker(ticker):
    print 'Downloading analyst opinions for', ticker
    soup = loadSoup('http://finance.yahoo.com/q/ud?s=' + ticker)
    table = soup.select('.yfnc_datamodoutline1 table')[0]
    data = pd.read_html(str(table), flavor='bs4', header=0, index_col=0)[0]
    data.index = pd.to_datetime(data.index)
    data['Ticker'] = ticker
    return data


def load_yahoo_opinions(dataset):
    cache_file = '../data/opinions-cache.csv'
    if os.path.exists(cache_file):
        print 'Loading opinions from cache'
        return pd.read_csv(cache_file, index_col=0, parse_dates=True)
    else:
        raw_opinions = pd.DataFrame()
        for ticker in dataset['Ticker']:
            raw_opinions = raw_opinions.append(
                load_yahoo_opinions_for_ticker(ticker))
        raw_opinions.index.name = 'Date'
        raw_opinions.to_csv(cache_file)
        return raw_opinions


def determine_opinion_sentiment(opinion):
    negitive = [u'Sell', u'Underperform', u'Underweight', u'Reduce', u'Sector Underperform',
                u'Mkt Underperform', u'Below Average', u'Avoid', u'Avoi', u'Strong Sell']
    neutral = [u'Hold', u'Equal Weight', u'Perform', u'Neutral', u'Mkt Perform', u'Equal-weight', u'In-Line', u'Sector Perform', u'Market Perform', u'Maintain Position', u'Perform-In-Line', u'Maintain', u'NT Neutral', u'NT Accumulate', u'ST Mkt Perform',
               u'ST Buy', u'LT Mkt Performer', u'Mkt Performer', u'NT Mkt Performer', u'Average', u'ST Neutral', u'Perform In Line', u'LT Neutral', u'ST Mkt Perform/LT Buy', u'In-line', u'NT/LT Mkt Performer', u'In Line', u'LT Mkt Perform', u'Equal-Weight']
    positive = [u'Buy', u'Outperform', u'Overweight', u'Sector Outperform', u'NT Buy/LT Buy', u'Strong Buy', u'NT Buy', u'Attractive', u'Recommended List', u'Accumulate', u'NT Accum/LT Buy', u'Top Pick', u'Peer Perform', u'NT Strong Buy', u'Recomm List', u'NT Accum', u'Mkt Outperform', u'Add', u'Market Outperform', u'Positive', u'Above Average',
                u'Buy Aggressive', u'NT/LT Outperformer', u'Outperf. Signif.', u'Buy-Focus List', u'Trading Buy', u'Mkt Outperformer', u'ST Accumulate', u'Long-term Buy', u'US Recomm. List', u'Net Positive', u'Buy $100', u'NT Outperformer', u'NT/LT Buy', u'Outperform/Buy', u'NT Mkt Outperformer', u'NT Acc/LT Buy', u'Buy/Core', u'Recomm. List', u'NT Strong Buy/LT Strong Buy']

    opinion['Negative'] = 0.0
    opinion['Positive'] = 0.0

    if opinion['Action'] == 'Downgrade' or (opinion['Action'] == 'Initiated' and opinion['To'] in negitive):
        opinion['Negative'] = 1.0

    if opinion['Action'] == 'Upgrade' or (opinion['Action'] == 'Initiated' and opinion['To'] in positive):
        opinion['Positive'] = 1.0

    return opinion


def determine_opinion_sentiments(opinions):
    opinion_sentiments = opinions.apply(determine_opinion_sentiment, axis=1)
    opinion_sentiments = opinion_sentiments.groupby(
        [opinions.index, 'Ticker']).sum()
    return opinion_sentiments


def load_quandl_prices(dataset, start, transform='rdiff'):
    cache_file = '../data/prices-cache.csv'
    if os.path.exists(cache_file):
        print 'Loading prices from cache'
        return pd.read_csv(cache_file, index_col=[0, 1], parse_dates=True)
    else:
        prices = pd.DataFrame()
        quandl_auth = 'pdRRzNygCjs_YY5Y2MVe'
        for index, row in dataset.iterrows():
            print 'Downloading prices for', row['Ticker']
            all_price_data = Quandl.get(
                row['Code'], trim_start=start, transformation=transform, authtoken=quandl_auth)
            close_price_data = all_price_data[['Close']]
            close_price_data['Ticker'] = row['Ticker']

            close_price_data['CloseClass'] = 'Neutral'
            close_price_data.loc[
                close_price_data['Close'] > 0, 'CloseClass'] = 'Gain'
            close_price_data.loc[
                close_price_data['Close'] < 0, 'CloseClass'] = 'Loss'

            prices = prices.append(close_price_data)
        prices.index = pd.MultiIndex.from_arrays(
            [prices.index, prices['Ticker']])
        prices.drop('Ticker', axis=1, inplace=True)
        prices.to_csv(cache_file)
        return prices


def encode_opinions(opinions):
    one_hot = pd.get_dummies(opinions['To'], 'opinion', '_')
    opinions = opinions.drop('To', axis=1)
    opinions = pd.concat([opinions, one_hot], axis=1)
    opinions = opinions.groupby([opinions.index, 'Ticker']).sum()
    return opinions