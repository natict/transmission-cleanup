# transmission-cleanup
Cleanup finished downloads from transmission


## Usage

To cleanup trasmission daemon running on 127.0.0.1:

```
docker run -e USERNAME=myuser -e PASSWORD=mypass --network host natict/transmission-cleanup
```

To cleanup trasmission daemon running on another host:

```
docker run -e USERNAME=myuser -e PASSWORD=mypass -e HOST=1.2.3.4 -e PORT=9091 natict/transmission-cleanup
```