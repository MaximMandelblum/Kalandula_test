# Age To Bucket Parser


* [people.json](../blob/master/assignments/coding/age_to_bucket/people.json) is a file that contains names of people along with their ages
* [age_buckets.json](../blob/master/assignments/coding/age_to_bucket/age_buckets.json) is file that contains a list of people age ranges

### Write a script that:
1. Reads the two json files (File names should be hardcoded, not dynamic).
1. Place the people names and age into age buckets based on the given age range from age 0 to <oldest person>
1. Outputs to a `.yaml` file (in yaml format) within the same directory as the `.json` files. file name should be `people_by_age_range.yaml` 
1. Yaml file should be sorted as follows:
    1. Age buckets are sorted from youngest range to oldest
    1. Within each age buckets the people should be sorted by age as well from youngest to oldest

### Simplified example:

For a given data of 5 people:
    George which is aged 40
    Michelle which is aged 30
    Judy which is aged 20
    Aaron which is aged 10
    
And for a given list of age buckets [20,30]

A `.yaml` file should look as follows:

```yaml
---
0 - 20:
  Aaron: 10
20 - 30:
  Judy: 20 
30 - 40:
  Michelle: 30
  George: 40
```    

> NOTE: Notice that that a person at an age of an actual range number will belong to the next range of people. for example: a 20 year old person (Judy in our example) is at the 20-30 bucket
> and NOT at the 0 - 20 bucket 
