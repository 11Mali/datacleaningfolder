# Nashville housing dataset

**Uncleaned and cleaned dataset in the folder**

Dataset: Small sized dataset ( approx. 56,000 datapoints), Structured data.
         The dataset describes housing prices in Nashville, Tennessee.

--- 

**Libararies used are pandas, numpy, regex**

## Initial outlook

**Current findings:**
- 56,477 entries/rows
- catagorical values in "SoldAsVacant" vary some inputs are "No" or "N" 
- 32,333 rows include incomplete data
- 0 duplicates identified in the dataset
- Large standard deviations in "LandValue", "BuildingValue", and "TotalValue" may indicate that the entry values are more spread out
- It appears that in "LandValue", "BuildingValue", and "TotalValue" the distribution is skewed to the right due to mean being than median
- The max value in "LandValue", "BuildingValue", and "TotalValue" appears to be signifigantly bigger than 75% percentile, indicating outliers
- The min value in "LandValue", "BuildingValue", and "TotalValue" appears to be signifigantly smaller than 25% percentile, indicating outliers

- The "Bedrooms", "FullBath", "HalfBath" columns appear to have a normal distribution with their mean and median being approximatly equal
- The "Bedrooms", "FullBath", "HalfBath" columns indicate having outliers due to large max values above the 75% percentile (houses come in varied sizes)
- The "Bedrooms", "FullBath", "HalfBath" columns indicate having outliers due to small min values below the 25% percentile (houses come in varied sizes)

**The points above will be further analysed**

- Remove missing/null entries --> data cleaning
- Remove duplicate entries --> data cleaning
- Remove special characters --> data cleaning
- Remove outliers --> data cleaning
 
- Inconsistency in "OwnerName" (needs further investigation) --> data transformation
- Incorrect data format (most columns being objects or float64), creating larger file than neccesary (8.2+ MB) --> data transformation
- Sale data being in string format (data transformation)
- Convert acarage from str with , to integer with . (2,3 to 2.3) --> data transformation
- Split address fields for easier filtering (Columns : PropertyAddress, OwnerAddress) --> data transformation
- "LandUse" and "SoldAsVacant" to catagorical data types --> data transformation

---

## Final Analysis and Discussion

Initial - 
The original dataset contained 56,477 rows, but a significant portion (32,333 rows) had incomplete data. 

Final -
After data cleaning, the dataset was reduced to 15,289 rows. 

Initial -
The "SoldAsVacant" column contained inconsistent categorical values (e.g., "No" vs. "N"). These inconsistencies needed standardization to ensure accurate analysis.

Final -
These values were standardized, but further checks across other categorical columns might still be necessary to avoid any unnoticed inconsistencies.


Initial -
LandValue, BuildingValue, TotalValue: The large standard deviations and the significant differences between the mean and median indicated right-skewed distributions with potential outliers. The minimum and maximum values were far from the 25th and 75th percentiles, further suggesting the presence of outliers.
Bedrooms, FullBath, HalfBath: These columns appeared normally distributed, but with notable outliers, especially at the high and low ends.

Final - 
SalePrice, Acreage, LandValue, BuildingValue, TotalValue: The outliers were more controlled post-cleaning, with a reduction in the maximum values (e.g., TotalValue max reduced from over 13 million to 297,200). However, some variability remained, which is typical in housing data due to the diversity in property types and locations.

Bedrooms, FullBath, HalfBath: The distributions of these variables remained consistent with typical residential properties, suggesting that the data cleaning effectively removed extreme outliers while preserving the core data characteristics.
Data Quality and Integrity:

Initial - 
Inconsistencies in the "OwnerName" field, incorrect data formats (e.g., string dates, non-standardized numeric formats), and the need to validate the relationship between "LandValue," "BuildingValue," and "TotalValue" were identified as key areas for further investigation.

Final - 
These issues were addressed through data transformations, standardizing formats, and verifying the summation relationship between "LandValue" and "BuildingValue" to match "TotalValue." These steps have contributed to a more reliable and structured dataset.


The data cleaning process successfully removed inconsistencies, standardized formats, and controlled for outliers, resulting in a more manageable and accurate dataset.

The reduction in data size due to missing values and outlier removal raises concerns about potential bias or loss of important variability. The dataset, while cleaner, may now lack some of the complexity that existed in the original, larger dataset.

The cleaned dataset is now better suited for analysis, but caution should be exercised when interpreting results due to the reduced sample size. Further exploration could involve investigating the causes of missing data and considering imputation methods that might allow for retaining more of the original dataset.


**Prior readings**
title : A Review on Data Cleansing Methods for Big Data
Authors : Fakhitah Ridzuan, Wan Mohd Nazmee Wan Zainon
Source : https://www.sciencedirect.com/science/article/pii/S1877050919318885


