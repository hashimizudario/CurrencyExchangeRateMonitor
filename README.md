# Currency Exchange Rate Monitor

This is a GitHub action aiming to notify with emails when you have a rather favourable currency exchange rate. It is schedule on a daily basis.

The finance API is provided by [CurrencyLayer](https://currencylayer.com/).  In this implementation, only free features is utilised.



## Parameters of Environment Secrets

By default, we use a environment named **default**.

| Name            | Explanation                                                  |
| --------------- | ------------------------------------------------------------ |
| ACCESS_KEY      | Access key of CurrencyLayer                                  |
| PASSWORD        | Sender email password                                        |
| RECIPIENT       | Email address to receive the notification                    |
| SENDER          | Sender email address                                         |
| SOURCE_CURRENCY | Source currency and check [here](https://currencylayer.com/currencies) |
| TARGET_CURRENCY | Target currency and check [here](https://currencylayer.com/currencies) |
| THRESHOLD       | Threshold to notify. When the ratio of one unit of target currency and one unit of source currency is lower than the threshold, the notification is triggered. |
| URL             | Url of your mail server                                      |



## Usage

1. Fork the repository
2. Update the environment secrets, according to your own case. By default, we use a environment named **default**.
3. I don't know but remember to check the actions permission. 
4. And voilà!

