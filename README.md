# Stock Prediction Using LSTM
Project Title:
Stock Prices Prediction Using Stacked LSTM

Overview:
Stock values is very valuable but extremely hard to predict correctly for any human being on their own. This project seeks to solve the problem of Stock Prices Prediction by utilizes Deep Learning models, Long-Short Term Memory (LSTM) Neural Network algorithm, to predict future stock values.  Historical data about the stock values that have been publicly listed by Quandl has been used in this project and I have used the stock value data of ‘Tata Global Beverages’. This can be considered as a Time series analysis is a specialized branch of statistics used extensively in fields such as Econometrics & Operation Research. This is specifically designed time series problem for you and the challenge is to forecast traffic.


Aim/Objective:
In the past decades, there is an increasing interest in predicting markets among economists, policymakers, academics and market makers. The objective of the proposed work is to study and improve the supervised learning algorithms to predict the stock price.


Technical Objective:
The technical objectives will be implemented in R. The system must be able to access a list of historical prices. It must calculate the estimated price of stock based on the historical data for the next 30 days. It must also provide an instantaneous visualization of the market index in a neatly formatted Python-Based Web App.

 

Long Short-Term Memory: (LSTM)
Long Short-Term Memory (or) LSTMs are widely used for sequence prediction problems and have proven to be extremely effective. The reason they work so well is because LSTM is able to store past information that is important and forget the information that is not. LSTM has three types of gates:
1.	The input gate: The input gate adds information to the cell state.
2.	The forget gate: It removes the information that is no longer required by the model.
3.	The output gate: Output Gate at LSTM selects the information to be shown as output.
Training was done under the following metrics and functions:
•	Number of layers = 4
•	Loss Function= Mean Square Error
•	Optimizer = Adam
•	Epochs = 100
•	Batch size = 64
 
Output:
 
Figure 1: Predicted Graph For Next 30 Days

 
Figure 2: Full Dataset + Predicted Values
 

Figure 3: Stock Prediction WebApp

Conclusion:
The proposed Stock Price Predictor has been successfully trained by using LSTM learning model on the sample datasets and the Stock value prediction process has been successfully performed by the trained LSTM model being tested on the test data set.
