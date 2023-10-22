# Deloitte-Opstech-Academy-Automation-Project

## StockNap: Stock Price Automation
<div align="center">
<img width="494" alt="StockSnap" src="https://github.com/Bhavyal9/Deloitte-Opstech-Academy-Automation-Project-/assets/77969476/2e595446-db50-4aa7-b0b4-eb3479cbeeb7">
</div>

This project was developed as the final presentation for the Deloitte Investment Banking Opstech Academy. The challenge was to automate the process of inputting share prices from the web into a spreadsheet for daily communication within the organization. To solve this challenge, we used web technologies such as HTML, CSS, and JavaScript to facilitate user interaction and python to fetch the relevant data, process it and finally to convert it into CSV file. The solution leverages the following steps:

- **User Interaction**: The web application allows users to input a specific date.
- **Passing Data**: The JavaScript code passes the input date to the Python code using the Eel library.
- **Data Retrieval**: Python utilizes the Yahoo yfinance API to download the relevant share price data based on the provided date.
- **Data Processing**: The retrieved data is processed and converted into a CSV file.

To execute the code and automate the share price retrieval process, please follow these steps:
- Obtain or create a spreadsheet containing the desired ticker symbols in the first column.
- Save the CSV file in the same folder as the code.
- Modify line 17 of the code to match the name of the CSV file you wish to open in Python.
- In the terminal, run the command "py server.py" (Ensure that all the required dependencies are already installed).
- A pop-up window will appear, displaying the web application. Select the desired date and click on the download button.

By following these steps, you can successfully run the code and retrieve the relevant share price data based on the chosen date. This automation solution eliminates the need for manual input from the Financial Times newspaper, saving time and reducing the chance of errors in the process.

Please note that this project was developed as part of the Deloitte Investment Banking Opstech Academy and serves as a demonstration of automation capabilities using web technologies and APIs.

