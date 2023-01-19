# IoTech Coding Exercises

Please provide the completed solution to your exercise as a public Github repository. It should include:
- Your solution
- A readme instructing the user how to build and run your solution. It must build on linux, other platforms are optional
- (optional) Any addtional material e.g. tests, dockerfile
-
## Exercise 01

Please write a program in the language of your choice (C or GO prefered) to complete the following tasks:

- Parse the data in `exercise-01/data/devices.json`
- Extract the `uuid` from the `Info` field
- For each device, calculate sum of the sensor payloads
- Reformat the data so that it satisfies the schema in `exercise-01/output-schema/schema.json`
- Order the reformatted data by `Name` (ascending)
- Write the reformatted data to a new file in `JSON` format

## Exercise 02

Please write a program in the language of your choice (C or GO prefered) to complete the following tasks:

- Parse the data from `exercise-02/data/data.json`
- Discard the devices where the `timestamp` value is before the current time. The timestamps are in `UNIX` format
- Get the total of all `value` entries, values are `base64` strings containing integer values
- Parse the uuid from the `info` field of each entry
- Output the values total and the list of uuids in the format described by the JSON schema. Write this data to a file
