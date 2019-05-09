---?color=#26454F
@title[Use Case]

@snap[west text-white]
### Use Case: Filtering Logging Data
@snapend

+++?color=#36454F

@snap[west text-white]
### Background

@ul[list-content-concise]
- The logs I'm after are stored in Elastic Stack (aka ELK)
- Although Elk's Kibana search UI lets me narrow down what I'm looking for, I need to extract details from specific messages
- Typically, logs are deeply nested JSON
  - verbose
  - large (10s to 100s of MB per search)
@ulend

+++?color=#36454F

### Log search on your local machine

@ul[list-content-concise]
- `% grep <pattern> log.txt`
- The log is already a file
- It's line-based
- You can use the usual shell tools (`head`, `tail`, `grep`, `wc`)
@ulend

+++?color=#36454F

### Remote distributed log search

@ul[list-content-concise]
- A user interface like Kibana
- Data comes from a network request as JSON
- It's not line-based; all one line, in fact
- Can't always refine search to get exact details needed
@ulend

+++?color=#36454F

### Remote distributed log search

@ul[list-content-concise]
- Narrow your search down with the search UI
- But pull the JSON result manually ("Copy as cURL")
- Use a tool for flattening/filtering JSON (`jq`) so you can use line-based shell tools
- What's that look like?
@ulend


+++?color=#36454F

### Example filter pipeline

```bash
curl 'https://...' \
| jq -f jq/filter.jq \
| pcre2grep -o1 '"client_ip": "([^"]*)"' \
| sort \
| uniq -c \
| sort -nr \
| less
```
@[1](data comes from a ` curl ` request)
@[2](`jq` filters, flattens, rewrites the JSON)
@[3](`--only-matching` for particular groups)
@[4-6](summary reporting/counting)
@[7]

+++?color=#36454F

### Example filter pipeline output

```text


10972  192.168.0.1
 8301  192.168.0.2
 5877  192.168.0.3
 ...
  47   192.168.0.8
```

+++?color=#36454F

### Testing your filter pipeline

@ul[list-content-concise]
- Normaly, you'd just save results as a file, then cat it out to test your pipeline
- But, I can't store any of this data on my laptop
- Goal is to extract some details (e.g., summary counts)
@ulend

+++?color=#36454F

### Testing your filter pipeline

@ul[list-content-concise]
- You end up testing and debugging the pipeline multiple times
- Can be tedious, time consuming (typos, network issues)
- Ideally, you only want to pull the data once
@ulend
