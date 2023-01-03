# Shopfloor observability example

This self-contained example explains how to set up topology extraction configurations in order to automatically extract topology through a multi-dimensional metric data stream coming from a production plant.
Idea here is to map all incoming data into the logic groups of:
- Factory (also called production plant or site)
- Lines (a production line)
- Cells (an individual production cell within a production line)
- Machines (a single machine within a cell)

This example contains:
- A [load generator](sf-generator.py) that sends multiple machinery telemetry metrics
- A [Dynatrace Extension 2.0 yaml](extension.yaml) file that contains all necessary declarative extraction rules to generate a dynamic shop floor production topology, as it is shown below. 

# Idea is to logically map all incoming data into plants - lines - cells and machines