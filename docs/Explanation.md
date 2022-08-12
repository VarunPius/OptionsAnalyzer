
---
https://pastebin.com/ZjuGntnh
https://docs.google.com/document/d/1fARnvjykmCjnGNZ8pq6zBaXzVhl291vK3bp_hZpT8Vk/edit
https://www.amazon.com/dp/0071818774/ref=cm_sw_r_cp_api_glt_fabc_0NJKZ5FGQZF0ZQJEPK63
---
Here are some of the important links which are under the hood:

Robinhood API: https://github.com/jmfernandes/robin_stocks

Documentation of Robinhood API: https://robin-stocks.readthedocs.io/en/latest/functions.html#getting-positions-and-account-information

Scrapy in python: https://scrapy.org/

Finviz settings: https://www.finviz.com/screener.ashx?v=111&f=cap_small,geo_usa,sh_avgvol_o300,sh_opt_option,sh_short_low&ft=4&o=-change

Yahoo endpoint: https://query2.finance.yahoo.com/v7/finance/options/ivr

-----------------------
How do you get BB, RSI, and SMA on the option since those all require historical options prices, when the yahoo endpoint only gives you current data? Did you filter the tickers in finviz on day 0 and then watch them (collect data) for 5 days to calculate those indicators?

You have to customize the end point based on your epoch periods, strike, expiry, ticker.

https://query1.finance.yahoo.com/v8/finance/chart/IVR220121C00003000?symbol=IVR220121C00003000&period1=1605796787&period2=1606228787&useYfid=true&interval=5m&includePrePost=false&lang=en-US&region=US

------------------------
Are you pulling your tickers from finviz into pandas library? How are you using yahoo endpoints and robin_stocks to enrich data? Are you using all 3 sources in your program to get your B-score?

pandas df are required for ta-lib so yeah the fetch data is converted to pd df. yahoo end-point data is used for TA only. RH real time data is used in other computations. There is no enrichment anywhere, I am not mixing the data streams. Yes, every piece of info is used in B-score in one way or another.

I have been using this since November and made around $2,000 from just $100. I will try to explain things here briefly. The whole motivation behind this was to spend less time finding good options to trade. I usually run this code manually, look at the top 3 choices, and place a buy order straight away under less than 1 minute and go back to work.

This is written in python. Tickers are obtained using scrapy on Finviz. I use the Yahoo options endpoint to fetch the data. The TA is performed on the daily data. B-score is a set of checks that I have in place, e.g., if RSI is less than 35 then it gets 1 B-score. Similarly, I have other checks on IV, Bollinger bands, etc., which worked well and are tested over time. You don't have to put in too many checks. Some simple ones just work great.

The ideal buy sell column is the price you want to get a call and sell it. This is derived again using all the TA factors. I have never seen a call rated 8/8 so far. Any score >=6 will end up in profit with a very high success rate. I usually don't hold calls for more than 3-4 days. I don't have enough money to start this on calls like AAPL, TSLA, etc. but yes maybe in the future hopefully.

-----------
If it involves buying calls and selling for profit you might be benefiting from the bull market instead of simply your strategy.

What configuration and time frame you use for bollinger bands?

I've found lots of strategies give insane returns for 2019-now but you wouldn't trade them given performance in earlier years. I would advise anyone who thinks they have cracked it based on results 2019 onwards that it is very important to look at performance on data before this.

I'll just counter back by saying that I've been focused on math based methods since 2003, and I've been bitten, humbled, and taken real, significant losses on numerous occasions because I thought I had it licked, like at the end of 2007 when I had been successful for four years straight, only to be crushed by 50% during the Great Recession when I devotedly followed my indicators down an unforeseen rabbit hole. IMO, to assume long term success by modeling any algo only during bull periods is a dangerous game. The duration of your trade type really does not change that, because a short term trade can be initiated during any market condition. And while you are 100% correct that past performance is no guarantee of future performance, the less data you use for any modeling endeavor, the higher your probability of erroneous conclusion. I am in no way knocking DJ's approach. Perhaps, by its nature and design, loss control is built in. It's working great now, it may work beautifully in all market conditions, I hope so, and time will tell. I'm just sharing some hard learned, expensive life lessons, food for thought. You're fully entitled to dismiss at will.

May be, may be not. Don't know but the strategy works. It picks up those calls which just drops for unknown reasons and next day they are up 50% and I sell. For BB I use 5 days data with 2 SD because I don't hold calls for too long.

Well the calls are cheap because the price drops, im guessing if the underlying keeps falling you lose.
That's why leap calls, they don't just fall for no reason. And as you said they are cheap and I don't go all in on one call. Its more like scalping you can say.

----------
Here are all the checks for B-Score. If they are True, the counter gets increased by 1.

    RSI <=40

    Volume >=100

    Filled price <= Lower Bollinger band

    SMA ( 5 days) <= VWAP

    Spread >=0.05 (This might change in future)

    Filled price = Current Bid

    IV<=40

    Today gain <= 0

Hope this helps. Check out my other replies for more information.
---------
Why do you increase B score for spread being high? Would that equate less liquidity?

Higher spread usually leads to higher chances of profit. This conclusion was obtained with trial and error. Again, there are several checks in B-score, some of them works on one day, some of the other works on another day. So far I have never seen 8/8 on any call.

--------------
Are the sma, bollinngers, etc on the underlying or the derivative?
They are derived from the daily ohlc historical options data for the ticker, strike, and expiry obtained using Yahoo endpoint.

---------------------
I'm trying to figure out what data you're capturing for Filled Price and how the Sr. No #1 TWO received a B-score of 7/8. It doesn't have a RSI < 40, It's filled price of 0.17 is not < the Lower BB of 15, and the filled price of 0.17 isn't equal to the current bid of 0.15.

Also, I don't think I understand your ideal buy/sell. For the Sr. No #1 TWR example you have an ideal buy of 0.15 and sell of 0.20. But the bid is 0.15 and the offer is 0.20. Are you just taking whatever the offer is or do you work a limit at the filled price (mid-point) of 0.17? Then, you just sell it at the mid-point the following day, and hope the option popp'd off the lower BB?

The B-score factors are the recent ones that I copy pasted from the code. They do need some fine tuning as this is a work is progress. I fix different things everyday in my free time. If you look at the table current time stamp on top left, it's back dated. But you get the idea of how score is computed.

Your point is valid. Robinhood won't accept the bid of 0.17 on a call which has 0.05 increment. Those ideal buy sell values are raw computed and are not rounded of based on the call incremental value. I will fix that, it's in my To-Do list. When I see 0.17 as ideal buy I round it off to 0.15 or 0.20 based on bid or ask size so that my order goes through, again a manual decision has to be made there.

---------------------------
I'm new to algo trading. Any reason you're looking at SMA instead of VWMA? Since you're comparing it to VWAP I'm wondering if it's deliberate that you're not accounting for volume on one side of the condition but you are on the other.

Edit: Also which settings are you using for your bollinger bands, RSI etc? And which period graph are you looking at, 1 minute candles?

Comparing SMA and VWAP works well on low volume calls and yes this was done on purpose.

------------------
The stuff that OP mentions are quite profitable even on stock trading. I have backtested similar type of TA-combos (bollinger percent B is one of my favorites in combination with very simple SMAs and RSI) on long stock positions during 2007-2009 and some other chaotic time periods and the strategies still work. You just have to compound 1% or so on the stocks that the machine tells you to buy and keep taking profits out during those kinds of chaotic time periods (aka dont be greedy and take profits as soon as they come to you). In bull markets you can be a bit more greedy.

Also, I would look into doing similar types of analysis on intraday and interday vix-related etfs... you would be surprised to see how high the winning percentages are. I have a large account (trading around 250k between three or so accounts) so I can make a lot of money just trading these simple strats with stock positions.

Also, when people here are like "oh but what about the great recession or what about the dot com bubble etc or what about the roaring 20's or what about the titanic or whatnot", just instead of going all scrooge on someone who is sharing a strat please just be encouraging in your diction and energy. Most of this subforum is either a) desperate traders looking for some intro to strategy finding or b) coders who dont know any strategy but can code or (very few) c) algo traders who are profitable who are holding their cards to the chest.



---------
pastebin link comments:

I'd be interested to see your screener and util modules. I am especially interested in your screener module because it seems to be doing a lot of work behind the scenes and might be more efficient than my own. I also rebuilt the method as DJ described it, but used a rather different (more complicated) code structure.

Since I'm making a request, I figured I should give something back via a review of the code you provided. Here are some issues I noticed that you may (or may not) want to adjust if you are planning to continue with this project:

    VWAP is not supposed to be calculated on daily data. This means you also need to pull 1min or 2min data from Yahoo (depending on your range) for each stock to calculate it properly.

    You don't seem to have the right settings for some of the TA indicators (e.g., RSI, SMA) based on what DJ has posted here.

    BBand Lower is supposed to be compared to the last filled price in the B-Score calc, not the prior close price.

    You're definitely not supposed to be summing the Volume numbers across several days. If you want to factor in more than one day I guess you could average, but I am pretty sure DJ is just taking the volume from either the prior day or the current day (probably the latter).

    The spread between his ideal buy/sell was on average 68% of the ask-bid spread from the data I examined, so using 60% for the value (as you do in your function) is a bit off. There is also contract-to-contract variation in how the spread is allocated that I have not been able to model, but this variation may not matter much given its small effect size.

    For calculating historical spread, we don't know the range he uses to calculate it. I settled on 3 days, but your guess of 5 is probably just as good.

    For the implied volatility, DJ is pretty clearly using Robinhood's IV because Yahoo's IV is way off compared to the numbers he has shown in screenshots. If you are going to use Yahoo's IV, you probably do not want to use 40 as your test in the B-Score given the differences.

    Similarly, you'll probably want to get current contract data (e.g., bid, ask, last, etc.) from your broker, rather than Yahoo since that is who you will be buying from.

    Finally, you do not seem to be filtering out options contracts with incomplete data (e.g., having no values for Bid, Ask, or IV), which needs to be done for the tests to apply properly.


    **
    Not to discourage you, but what you posted is what I had in July 2020. There are a lot of things that you need to work on.

    Your ideal buy-sell is very simple for now. You need to work for a better approximation that captures the maximum probability of profits. This is the secret sauce which I won't tell here and has not been discussed so far. Getting these ideal ranges corresponds to roughly 15% of my whole work, and that includes testing and implementing different strategies to get it.

    You have to test TA parameters for RSI, SMA, VWAP. You are using 5, 5, etc. but I don't use 5. I use 10, 14, etc. which worked well for me. Read this discussion as I have mentioned what exactly I am using for what purpose.

    I am sure that if we run our versions on the same tickers with the same strikes and expiries, our tables won't match at all. I have posted many screenshots, try to reproduce them if you can. This will serve as a testing and benchmarking for you.

    I won't bet real money with what you have so far. So do a lot of testing and paper trading during market hours to get more confidence in your code.

    There are plenty of other things that I have in place: multiple scanners (look at barchart, stockbeep, liomaster, swingtradingbot, I do have premium fool so that's also baked in, finscreener, I have 8 different sets of finviz filters targeting different things), plotters, parallel processing, level 2 data to get current support and resistance, caching and hybrid modes, candlestick pattern recognition, fake user agents with batch fetch, SEC parser to exclude tickers with insider selling, notification/logs, swing signals, and tones of other stuff that I can't even recall. I don't see any of that in your code and it's not your fault because it has not been discussed before. And of course, I won't discuss those things here. A lot happens inside and it is not just table printing. My most well-put thoughts are buried in the code and only auxiliary things are discussed here in these threads.

As I said earlier, a great heads-up for anyone looking to start from ground zero. You have done a great job to put all things together in few hours so that people can have a head start. Thanks for sharing your code with others too.

Please don't take this as a discouragement. I hope you have success in your project, do test different things, and build something powerful over time that can generate unrealistic profits. I guarantee you, it definitely can. Everything is right in front of your eyes. Also, we are not in any competition and there are no dead-lines :)

***
So I am curious about your comment that those of us in the thread would have completely different tables from you. Conceptually it seems like there are three steps to what you are doing with your code:

    Gather a validated list of tickers

    Perform TA on those tickers

    Score them according to those values

The majority of the previously unmentioned aspects of your code seem to apply to step 1 or are best practices/QoL features. The various scanners all increase the number and variety of tickers, the insider trading data rules out tickers with bad signs. Those impact which tickers get processed, but not the values generated on them.

Many of the features are just smart choices (batch processing, fake headers) or quality of life features (notifications, caching), which don't impact the generated values.

All that is left is the candlestick pattern recognition, swing signals, and support/resistance data. Those could be impacting step 2 where you actually generate your numbers, but I am not sure how you are using them (beyond impacting the ideal buy/sell).

If I am right in everything I have said so far, my question is: If we both processed the same contract symbol (e.g., IVR220121C00004000) would we get the same results? Assuming, of course, that I actually closely followed everything you said here and didn't make any of the obvious mistakes that the code on Pastebin is making.

It seems to me that the main points of divergence would be on 'Ideal Buy/Sell' (because I have yet to be able to model the exact parameters you are using) and 'Spread' (because I don't know the time range you're using to pick the local highs and lows).

But everything else should be the same, even given all the previously unmentioned features you just posted about, right? We'd have the same values for Bid, Filled, Ask, Volume, OI, the BBands, RSI, VWAP, SMA, Change, and IV (assuming we were using the same data sources - Yahoo + Robinhood - and the TA settings discussed on this thread). Or do some of the unmentioned code differences generate differences in some of these values as well?
***
BB(S/R) will be different because it also considers support and resistance from level 2. S/R stands for support and resistance.

Assuming we have same candlesticks input (range and interval) and TA parameters for IVR call then OI, Vol, RSI, VWAP, today's gain, SMA, IV will match because they are straight forward. BB(S/R), Spread, Ideal buy sell probably won't match. If BB(S/R) is different then the derived B score will not match.

Smart choices which you mentioned are performance related and one will observe that they are necessary once your list of tickers grow large. Otherwise it will take forever for just 1 run not to mention rate limits with your brokerage and api endpoints. Imagine scanning tickers like AAPL and TSLA for all strikes and expiries. But yes they don't effect the numbers in the table. The other guy asked for 95% so it is included in that 😬

-----------
I am very interested about how you place/exit order. 1/ what is DTE? Only calls? How to choose strike price? 2/ what is your exit plan? Stop at 30%? Sell at 100% gain? 3/ you have bscore max 8. Does that mean you have total 8 rules? 4/ how do you calculate TA? On your own or some lib? Billinger band calculation was confusing to me:(

  Exit orders are usually 10-20 cents up from buy order. Yep, only calls for now. First, I only look at B-Score then other details like strike, bid etc. based on available money in account. I usually sell at around 30% quick gains. I have seen calls doing 400% if I hold a bit longer but I don't do that. There are plenty of options available to make profit from. Yes, total 8 rules which worked so far. I use ta-lib in python for doing TA on 1 month range ohlc data.
