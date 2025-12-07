# Currency Converter 💱

A simple Python script to convert amounts between different currencies using the [ExchangeRate-API](https://www.exchangerate-api.com/).

---

## Version 🏷️

- Current version: v1.0
- Future release: Streamlit-based UI version in development

---

## Features ✨

- Converts any amount between supported currencies.
- Lists available currencies for easy selection.
- Supports continuous conversions in a loop 🔄.
- Fetches live conversion rates from ExchangeRate-API.

---

## Requirements 🛠️

- Python 3.x
- `requests` library

Install dependencies:

```bash
pip install requests
```

---

## Getting the API Key 🔑

1. Go to [ExchangeRate-API](https://www.exchangerate-api.com/).
2. Sign up for a free account.
3. After signing in, you will get a unique API key.
4. Keep this key safe — you will need it to run the script.

---

## Setting up the Environment Variable 🖥️

The script uses an environment variable to store your API key securely.

### Mac/Linux
```bash
export Exchangerate_API_KEY="your_api_key_here"
```

### Windows (CMD)
```cmd
set Exchangerate_API_KEY=your_api_key_here
```

### Windows (PowerShell)
```powershell
$env:Exchangerate_API_KEY="your_api_key_here"
```

---

## How to Run ▶️

1. Clone or download the repository.
2. Make sure your environment variable is set with your API key.
3. Run the script:

```bash
python currency_converter.py
```

4. Follow the prompts:
   - Select the “From” currency.
   - Select the “To” currency.
   - Enter the amount to convert.
   - Repeat or exit.

---

## Example 💵

```text
Select from available currencies: 
USD
EUR
AED
GBP
...
From Currency: AED
To Currency: EUR
Amount: 100
100 AED = 24.32 EUR
Do you want to convert another amount? (yes/no): no
```

---

## Notes 📝

- The API key is required and must be included in the URL for requests.
- The `params` dictionary is unnecessary because ExchangeRate-API expects the key in the URL itself:

```python
url = f"https://v6.exchangerate-api.com/v6/{API}/latest/USD"
```

- The script fetches rates only once at the start. For constantly updated rates, you would need to request the API before every conversion.

---

## License ⚖️

MIT License

## **👨‍💻Author**

💻 Built with ❤️ by Kian Kheiri N. ([@Cnized](https://github.com/Cnized))