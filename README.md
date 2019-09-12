## **Background:**

Machine learning tools, both logistic and regressor methods work on the assumption that features are provided in a numeric format.
When data are passed from marketing tools analytics like FB or Google, the data are in such a format that features (qualitative characteristics connected to the campaign and to the users who performed certain actions) are in a categorical and badly structured format and cannot be understood for machine learning purposes.
Sometimes also if the data are in a numeric format, it can result difficult to find a linear connection between features and deliver predictions so classical linear and regression model cannot be used. 
In this case it can be useful to apply logistic classification and split up the characteristics of each single user who visited the website from the campaign aggregation level to understand if he/she is suitable to convert and became a paying customer.

Project goals:
The idea is to create a set of functions to simplify the communications and the exchanges of data between Marketing and BI-Data Science so to avoid errors in the creation of the models.

## **What it does?**

### **Data transformation:**

Cleaning data from not needed characters:

* Rename columns if needed so to avoid mismatching and confusion

* Turning numerical data columns into python integer or floating so to avoid errors when modelling happens

* Transforming categorical data into hot encoding to ensure machine understanding of qualitative features

Indexing and data reorganization:

In the case in which linear regression cannot be applicable, or for any reason categorization better suits the scope of the project, more work on data needs to be applied.
First of all data from marketing comes in a campaigns or ads grouping format while to apply a logistic analysis of any kind user based grouping is needed. In order for this process to work a unique identifier column for the element taken into consideration needs to be given or alternatively created (it can be campaign+date, ad ID +date or a mixture so to identify what it is defined in BI usually as the last aggregation step).
Based on this, the initial table is going to be reshaped so that every visit from a campaign results as a unique user and campaign features are going to be reattributed to this user. The same process is going to be applied for further website steps so to create different grouped tables with the right events to then be remerged having a complete table fully reshaped and with the right number of events attributed.
