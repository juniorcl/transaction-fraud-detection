# Transaction Fraud Detection

A data science project to predict whether a transaction is a fraud or not.

<div align="center">
    <img alt="churn" src="https://www.finance-monthly.com/Finance-Monthly/wp-content/uploads/2018/07/Fraud-Epidemic-Costs-%C2%A33.2-Trillion-Globally.jpg" width="100%" height="300">
</div>

<br>

## Context

> The following context is completely fictional. All information was taken from the Data Science project proposal on the website [Seja um Data scientist](https://sejaumdatascientist.com/crie-uma-solucao-para-fraudes-em-transacoes-financeiras-usando-machine-learning/).

The Blocker Fraud Company is a company specialized in detecting fraud in financial transactions made through mobile devices. The company has a service called "Blocker Fraud" which guarantees the blocking of fraudulent transactions.

The business model of the company is of the Service type with the monetization made by the performance of the service provided, in other words, the user pays a fixed fee on the success in detecting fraud in the customer's transactions.

However, the Blocker Fraud Company is expanding in Brazil and to acquire customers more quickly, it has adopted a very aggressive strategy. The strategy works as follows:

1. The company will receive 25% of the value of each transaction truly detected as fraud;

1. The company will receive 5% of the value of each transaction detected as fraud, but the transaction is truly legitimate.

1. The company will return 100% of the value to the customer, for each transaction detected as legitimate, however the transaction is truly a fraud.

With this aggressive strategy, the company assumes the risks of failing to detect fraud and is remunerated for assertive fraud detection.

For the client, it is an excellent business to hire the Blocker Fraud Company. Although the fee charged is very high on success, 25%, the company reduces its costs with fraudulent transactions detected correctly and even the damage caused by an error in the anti-fraud service will be covered by the Blocker Fraud Company itself.

For the company, in addition to getting many customers with this risky strategy to guarantee reimbursement in the event of a failure to detect customer fraud, it depends only on the precision and accuracy of the models built by its Data Scientists, in other words, how much the more accurate the “Blocker Fraud” model, the greater the company's revenue. However, if the model has low accuracy, the company could have a huge loss.

### The Challenge

You have been hired as a Data Science Consultant to create a model of high precision and accuracy in detecting fraud of transactions made through mobile devices.

At the end of your consultancy, you need to deliver to the CEO of Blocker Fraud Company a model in production in which your access will be made via API, that is, customers will send their transactions via API so that your model classifies them as fraudulent or legitimate.

In addition, you will need to submit a report reporting your model's performance and results in relation to the profit and loss that the company will have when using the model you produced. Your report should contain the answers for the following questions:

1. What is the model's precision and accuracy?

1. How reliable is the model in classifying transactions as legitimate or fraudulent?

1. What is the revenue expected by the company if we classify 100% of transactions with the model?

1. What is the loss expected by the company in case of model failure?

1. What is the profit expected by the Blocker Fraud Company when using the model?

### About the Data

The data used in this project was taken from the [Synthetic Financial Datasets For Fraud Detection](https://www.kaggle.com/ntnu-testimon/paysim1). The database is very large, therefore, for this project I used a stratified sample to get 1% from original data.

Each row represents a transaction and each column is:

* **Step** - maps a unit of time in the real world. In this case 1 step is 1 hour of time. Total steps 744 (30 days simulation).

* **type** - CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER.

* **amount** -
amount of the transaction in local currency.

* **nameOrig** - customer who started the transaction

* **oldbalanceOrg** - initial balance before the transaction

* **newbalanceOrig** - new balance after the transaction

* **nameDest** - customer who is the recipient of the transaction

* **oldbalanceDest** - initial balance recipient before the transaction. Note that there is not information for customers that start with M (Merchants).

* **newbalanceDest** - new balance recipient after the transaction. Note that there is not information for customers that start with M (Merchants).

* **isFraud** - This is the transactions made by the fraudulent agents inside the simulation. In this specific dataset the fraudulent behavior of the agents aims to profit by taking control or customers accounts and try to empty the funds by transferring to another account and then cashing out of the system.

* **isFlaggedFraud** - The business model aims to control massive transfers from one account to another and flags illegal attempts. An illegal attempt in this dataset is an attempt to transfer more than 200.000 in a single transaction.

## Methodology

This project will be based on Cross-industry standard process for data mining (CRISP-DM). A standard idea about data science project may be linear: data preparation, modeling, evaluation and deployment. However, when we use CRISP-DM methodology a data science project become circle-like form. Even when it ends in Deployment, the project can restart again by Business Understanding. How might it help? It may help to avoid the data scietist to stop in one specific step and wast time on it. When all the project is completed the data scientist can return to initial step and do every step again. Therefore, the main goal it is to follow circles as it needs.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/b/b9/CRISP-DM_Process_Diagram.png" alt="Kitten" title="A cute kitten" width="430" height="430" />
</div>

## Results

### Model Results

Some models have been tested to obtain the best model for this project. 