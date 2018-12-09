**Emoji detection in a container**

This is a containerized version of MIT's Deepmoji (https://github.com/bfelbo/DeepMoji), using python and Flask.

Usage: 

```
docker build -t mydeepmoji .

docker run -it -p 5000:5000 mydeepmoji

```

Navigate to: 

http://localhost:5000


Currently deployed at http://104.42.255.66:5000/. If you want to test it out just add any text you want as query text. 

http://104.42.255.66:5000/I%20broke%20my%20leg -> shows: ["😫", "😖", "😢", "😭", "😣"]
