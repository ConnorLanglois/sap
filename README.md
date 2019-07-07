# SAP : Stock Analyst and Predictor

A bot that automatically scrapes news articles from the web and parses them if they contain company/stock names.
Eventually will incorporate machine learning with this data alongside daily historical data to predict movement of stock.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Python
newspaper
googletrans
nltk
```

### Installing

Clone the repo.

### Running

Steps:

1. Place each news source on a new line in file:

	```
	resources/sources.txt
	```

2. Place each stock as "symbol:name,name,..." on a new line in file:

	```
	resources/sources.txt
	```

3. Run the main file:

	```
	src/sap.py
	```

## Authors

* **Connor Langlois** - [ConnorLanglois](https://github.com/ConnorLanglois)

## License

This project is not licensed.
