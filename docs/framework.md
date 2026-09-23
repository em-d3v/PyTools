# Framework

This document is for documenting the base framework for the application

```
directory layout:
project/
├─dist/    --for final product
├─data/    -- for data
├─test/    --for testing (does not exist)
├─config/  -- stores configurations for the scripts/
├─build/   --for dumping files when building
├─log/     --stores logs created by scripts
├─scripts/ --for the builder and runner script
│
└─src/
│	├─lib/ --stores packages used by both gui & logic
│	├─gui/ -- stores gui packages (front-end)
│	│	└─comp/ --components
│	├─logic/ -- stores back-end code of application
│	├─resources/ 
│	└─main.py --
└─template/ --stores template files for project

```
