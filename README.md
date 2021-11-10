# King County Real Estate Sale Prices
![house image](https://ncinj.com/wp-content/uploads/Multi-Family.jpg)

## Table of Contents
* [Project Overview](#project-overview)
* [Data Overview](#data-overview)
* [Methodology](#methodology)
* [Project Results](#project-results)
* [Next Steps](#next-steps)
* [Navigating the Repository](#navigating-the-repository)

## Project Overview
For the second phase of Flatiron’s Live Data Science program, we were tasked with developing a multiple linear regression model. This model would predict the price of houses in King County, Washington using data from the King County reality dataset. We decided to develop this model for a small realty business named Mom and Pop Realty. The goal is to provide an accurate prediction for the price of their client’s home before putting it on the market. Clients will always want to get the most money for their home possible. However, realty firms will quickly find themselves with a poor reputation and out of business if they are misleading or dishonest in their assessed target price. Assuming the firm is acting in good faith and wants to provide an accurate assessment, their prediction model must be flexible to the market to continue being competitive in the marketplace. With these concerns in mind, we set out to explore the features in the data set to design our model, explore correlations between different features and the sale price of the home, and use the features with strong correlations to develop a model to achieve our goal. We made sure to normalize our data using a log transformation and scale our data for consistent analysis. As we concluded our analysis, we discovered the most important features to predicting sale price was the size of the home and lot, the condition and grade of the home, and whether there's a basement. We recommend Mom & Pop Realty take these features into consideration when assessing the values of client's homes.

## Data Overview
This dataset contains house sale prices for King County, Washington. It includes homes sold between May 2014 and May 2015. The data was gathered from King County GIS Open Data. The data represents different features of homes in King County. The data is widely varied, as is to be expected. The data states when the house was built and if it was renovated as well as the date of sale. The data includes counts on floors, bathrooms, and bedrooms. Also included in grade and condition of the home. The data also includes waterfront property designation and data on view on different landmarks from the property. The data includes information on the basement, living, and lot area. The data also includes information regarding living and lot areas of the closest 15 properties. Additionally, there is also locational data including zip code and latitude and longitude of the property. Using these features our target variable will be the sale price of the home. We are targeting categorical data in the grade and condition of the home. We have ordinal data in the number of bedrooms and continuous data in the home and lot size.

Here is the distribution of home prices in King County
21,419 home sales --> Median: $450,000

![Price Correlations](https://user-images.githubusercontent.com/74070082/136581794-651ff990-3744-47be-91ad-f493929fd2ad.png)
- These are independent correlations to price

![House values in King County](https://github.com/Nindorph/KingCountyHousingSaleModel/raw/main/images/House_prices.png)
- Location information not included because we wanted the model to only take house characteristics into account

![Grade and Condition v Price](https://github.com/Nindorph/KingCountyHousingSaleModel/raw/main/images/Grade_Condition.png)
- Home price increases as grade improves, condition improves, and condition improves within grade

![Bathrooms v Price](https://github.com/Nindorph/KingCountyHousingSaleModel/raw/main/images/bathrooms.png)
- Home price increases as number of bathrooms increases



## Methodology
### Let's build models.
#### Test, Train, Split the data


Here we split the data into a test and train set. We will fit and transform the training data and later fit the training data for analysis. We will be using the log-transformed data to utilize the more normative distribution of the data. We will additionally be scaling our data to allow the model to weigh the features equally because they will be on the same scale, and we will be able to compare the feature coefficients

This very simple model will predict the average of the training data set prices and will not utilize any independent variable. This will result in the residuals being the same. As you can see the training and test residuals are almost directly over laid on one another. Which is predictable based on the parameters of our current model. This is not a practical model for the scope of our project.

## Project Results

Our final model resulted in a $152,7285.76 average variation from observed sales prices and ended with a R squared value of .555 meaning our model accounts for a 55.5\% variance in sales price. All of the features have a pvalue of less than 0.05, which implies all features are significant to the model. Our condition number is less than a 5, meaning there is little multicollinearity issues. The scatter plot of the residuals does display some heteroskedasticity. Based on the QQ plot, the residuals are slightly skewed to the right. Our model does therefore violate the assumptions of linear regression, but only slightly, and maybe not enough to make it not valuable. It is interesting to note that none of the engineered features and the number of bathrooms made it into the final model.

## Conclusion & Next Steps
- One: 
Including location data 
- Two:
Consider separating high/low cost housing differently

We recommend Mom & Pop Realty use the size of the house and property, grade and condition of the house, and whether the house has a basement to understand the potential sale price of the a clients home. The strongest predictors are House Square Footage, where a 1% increase in Home square footage translates to an increase in 0.22% sale price. The next strongest predictor is the grade of the house, specifically, where the house has an excellent grade. Homes with an excellent grade has a 20.1% higher sales price than that of a home with an average grade. We understand this model is incomplete and the level of bias in the model reduces the overall effectiveness.

Especially given the average error is ~$\150,000, the price of some homes in the dataset, we would not recommend Mom & Pop Realty use the model to give an accurate numerical estimate for the sale price of a home. Rather, it is effective as a view into what features are important determinants of sale price.

Critically, our final model does not include location data and does not differentiate between high and low cost housing. Adding those features to the model may help the model's bias, heteroskedasticity issues, and overall predictive power.

## Navigating the Repository

```
├── data
│           ├── Zipcodes_for_King_County_and_Surrounding_Area__
│           ├──column_names.md
│           ├──home.JPG
│           └── kc_house_data.csv
├── notebook
│          ├──Dave
│          ├──Mellissa
│          └── Nick
├── images
│          ├──bathrooms.png
│          ├──Grade_Condition.png
│          ├──House_prices.png
│          ├──sqft_house_v_price.png
├── README.md
└── HousingSalesModel.ipynb
```
