## Overview
This CSV file contains the calculated values of **T**, **S(T)**, and **Sae(T)** based on the soil classification and input parameters provided by the user. The calculations follow the guidelines set by the **2007 Earthquake Regulation** for local soil classes.

## Content
The CSV file includes the following columns:
- **T (s)**: Represents the period in seconds for which the seismic response is calculated.
- **S(T)**: Represents the spectral response acceleration coefficient as a function of T.
- **Sae(T)**: Represents the effective acceleration coefficient, calculated using the input parameters **A0** and **I**.

## Soil Classes
The soil classes included in the calculations are:
- **Z1**: TA = 0.10, TB = 0.30
- **Z2**: TA = 0.15, TB = 0.40
- **Z3**: TA = 0.15, TB = 0.60
- **Z4**: TA = 0.20, TB = 0.90

## Usage
1. Ensure you have Python installed along with the necessary libraries (`numpy`, `matplotlib`, `pandas`).
2. Run the provided Python script, and input the required values when prompted:
   - **Soil class** (Z1, Z2, Z3, Z4)
   - **A0 value** (default is 0.4 if left blank)
   - **I value**
3. Upon completion of the calculations, the results will be saved in the `T_S_T_and_Sae_T_values.csv` file.
4. You can open the CSV file using any spreadsheet software or a text editor to view the calculated values.

## Example
Here is an example of what the CSV file content may look like:

## Conclusion
This file serves as a valuable resource for engineers and researchers involved in seismic analysis, providing essential data for understanding soil behavior during seismic events.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


