# log-converter

Konversi log file

## Instalasi

```bash
cd log-converter

make build
```

## Usage

```bash
docker run -it -v "$PWD":/usr/src/app -w /usr/src/app --rm log-converter --help

docker run -it -v "$PWD":/usr/src/app -w /usr/src/app --rm log-converter error-connect.1000.logs -o error-connect.1000.logs.json -t json

docker run -it -v "$PWD":/usr/src/app -w /usr/src/app --rm log-converter error-connect.1000.logs.json -o error-connect.1000.logs.txt -t text

docker run -it -v "$PWD":/usr/src/app -w /usr/src/app --rm log-converter error-connect.1000.logs -o error-connect.1000.logs.default
```