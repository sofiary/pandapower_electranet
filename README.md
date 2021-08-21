# PandaPower ElectraNet
An attempt at implementing the ElectraNet transmission system with pandapower<br>
This repository is publicly provided under the MIT license.
Users are urged to note the data disclaimers & requirements provided by external data sources (ElectraNet, AEMO).

# Data Sources
## ElectraNet
### Qualitative
- <a href="https://www.electranet.com.au/wp-content/uploads/2020/11/2020-ENet-TAPR.pdf">ElectraNet Transmission Annual Planning Report 2020

### Quantitative
- <a href="https://www.electranet.com.au/wp-content/uploads/2020/05/Connection-Point-Data-20052020.xlsx">ElectraNet 2019 Connection Point Data</a>

## AEMO
### Qualitative
- <a href="https://aemo.com.au/energy-systems/electricity/national-electricity-market-nem/data-nem/network-data/transmission-equipment-ratings/alternative-value-application-ratings">Alternative Value Application Ratings</a>
- <a href="https://aemo.com.au/energy-systems/electricity/national-electricity-market-nem/data-nem/network-data/transmission-equipment-ratings/equipment-identifiers">Equipment Identifiers</a>
- <a href="https://aemo.com.au/energy-systems/electricity/national-electricity-market-nem/data-nem/network-data/transmission-equipment-ratings/rating-application-levels">Rating Application Levels</a>

### Quantitative
<a href="https://aemo.com.au/energy-systems/electricity/national-electricity-market-nem/data-nem">Data (NEM)</a>
Includes info on:
- Planned Outages
- 

## Other
None

# Steps
This program takes a number of sequential steps to build a replica ElectraNet network.

## Model Creation
We need to create:
- buses with appropriate names and voltages;
- lines with appropriate bus connections, names, lengths and types;
- high voltage transformers with appropriate bus connections, names and types;
- network shunts (where known) at an appropriate bus with a name and Q value;
- network load elements (representing substation loads, in aggregate), with an appropriate bus connection, name and P,Q value;
- network generation with an appropriate bus connection, name, size, type and capability curve info; and
- external grid object(s) to represent the reference node (slack bus) generator.

### Buses
Bus data can be sourced from the ElectraNet 2019 Connection Point Data excel spreadsheet.

### Transmission Lines
#### Lengths
Conductor lengths can be parsed directly from the <a href="https://www.aemo.com.au/aemo/data/map/layers/transmission.json">transmission.json</a> file publicly sourcable from AEMO.

#### Conductor Types
Transmission lines <a href="https://www.electranet.com.au/wp-content/uploads/2018/06/1-03-FR-09-Transmission-Line-General-Requirements-Including-Typical-Overhead-Line-Structures.pdf">are either</a> ACSR, AAAC or AAC. They are either 275kV, 132kV or 66kV. 

#### HVDC
To do

#### Transformers
To do

#### Shunts
To do

#### Loads
To do

#### Generation
To do

#### External Grid
To do

## Model Tuning
To do

## Model Verification
To do