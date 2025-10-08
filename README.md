# Ex.05 Design a Website for Server Side Processing
# Date:8.10.25
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Power of Lamp Bulb Calculator</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background-color: #171616;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  .calculator {
    background-color: #aaef09;
    border: 2px dotted #0080ff;
    padding: 20px;
    width: 300px;
    text-align: center;
    color: #0c0c0c;
  }
  h2 {
    font-family: "Arial Black", Arial, sans-serif;
    font-weight: bold;
    color: #cc0000;
    margin-bottom: 20px;
  }
  label {
    font-weight: bold;
    display: block;
    margin: 10px 0 5px;
  }
  input[type="text"] {
    width: 70%;
    padding: 5px;
    font-size: 1rem;
  }
  button {
    margin: 15px 0;
    padding: 5px 15px;
    font-size: 1rem;
    cursor: pointer;
  }
  .result {
    margin-top: 10px;
    font-weight: bold;
  }
</style>
</head>
<body>
  <div class="calculator">
    <h2>Power of Lamp Bulb</h2>

    <label for="intensity">Intensity:</label>
    <input type="text" id="intensity" placeholder="Enter current (I)" />

    <label for="resistance">Resistance (in Ω):</label>
    <input type="text" id="resistance" placeholder="Enter resistance (R)" />

    <button onclick="calculatePower()">Calculator</button>

    <div class="result" id="powerResult">Power: </div>
  </div>

<script>
  function calculatePower() {
    const intensity = parseFloat(document.getElementById('intensity').value);
    const resistance = parseFloat(document.getElementById('resistance').value);
    if (isNaN(intensity) || isNaN(resistance)) {
      alert('Please enter valid numerical values for Intensity and Resistance');
      return;
    }
    // Power P = I^2 * R
    const power = intensity * intensity * resistance;
    document.getElementById('powerResult').textContent = 'Power: ' + power.toFixed(2) + ' watts';
  }
</script>
</body>
</html>


```
# SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-10-08 210010-1.png>)
# HOMEPAGE:
# RESULT:
The program for performing server side processing is completed successfully.
