# Redis Clone

Implementing Redis ( Im Memory Cache ) using Python


## Design

![https://github.com/AbhishekPowar/redis_clone/blob/master/assests/redis_clone.png](https://github.com/AbhishekPowar/redis_clone/blob/master/assests/redis_clone.png)

## Explanation
* Redis+ Server maintains keys and values passed 
* User can use both Redis+ Client to interact with Redis Server
* User can also user Redis+ API to interact with Redis Server
* Data can be perisited into File System or Key Value Store

## Features 
* API support for CRUD
* Key Expiry/ TTL (Time to live)
    * Currently Supports Passive key expiry
* Perisistance to File System 
* Read data from from File System
* Support for multiple data structures 
    * Currently Supports : Integer, String, List, Set, HashMap/Dictionary

## TODO 
- Currently Working on
    - Support multiple index/namespace/database
    - Swagger UI for API

- Up next
    - Improving Persistance Logic 
    - Active Key Expiry / TTL
    - Validation during loading data to Cache
    - Persistance to Key value store / DB
    - Load data from KV Store
    - Multithread Support

