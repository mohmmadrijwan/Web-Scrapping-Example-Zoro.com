# Web-Scrapping-Example-Zoro.com

This project demonstrates how to scrape data from the gloves category of Zoro.com using Python. The script downloads product data such as product titles, prices, brand names, and links to each product page, then converts the data into a CSV file for easy analysis.

### Prerequisites

Before running the scripts, ensure you have the following:

- Python 3.x
- Required Python libraries (requests, BeautifulSoup, pandas, etc.)
  
To install the necessary libraries, you can use the following command:

```bash
pip install -r requirements.txt
```

### Steps to Run the Project

#### Step 1: Download HTML Pages

Run the following command to initiate the process of downloading the HTML pages for the gloves products:

```bash
python getHTMLPages.py
```

This will:

- Create a folder called `Gloves` in your project directory.
- Download HTML pages (1 to 20) containing gloves product information from Zoro.com into this folder.

#### Step 2: Convert Product Data to CSV

Once all the HTML pages have been downloaded, run the following command to convert the product data into a CSV file:

```bash
python convertProductToCSV.py
```

This will:

- Parse the downloaded HTML files.
- Extract the product title, price, brand name, and product link.
- Generate a CSV file named `gloves.csv` containing the extracted product data.

### File Structure

```
.
├── getHTMLPages.py
├── convertProductToCSV.py
├── requirements.txt
├── Gloves/
│   ├── page_1.html
│   ├── page_2.html
│   ├── ...
├── gloves.csv
```

### Example CSV Output

The resulting CSV (`gloves.csv`) will have the following columns:

| Title                     | Price   | Brand    | Link                             |
|---------------------------|---------|----------|----------------------------------|
| Example Product 1          | $10.99  | Brand A  | https://www.zoro.com/product1     |
| Example Product 2          | $15.49  | Brand B  | https://www.zoro.com/product2     |
| ...                        | ...     | ...      | ...                              |

### Notes

- The scripts use the `requests` library to fetch the HTML content of the pages and `BeautifulSoup` for parsing the HTML.
- The product data is saved in a structured CSV format, which can be easily analyzed or used for further processing.

---
