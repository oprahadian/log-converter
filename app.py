import click
import json

def parser_nginx_error_log(r: str) -> dict:
    r_split = r.split(" ")

    result = {}

    try:
        result["date"] = r_split[0] + " " + r_split[1]
        result["status"] = r_split[2].replace("[", "").replace("]", "")
        result["file_patch"] = r_split[6].replace('"', '')
        result["ip"] = r_split[15].replace(',', '')
        result["method"] = r_split[19].replace('"', '')
        result["host"] = r_split[23].replace('"', '').replace(',', '')
        result["url"] = r_split[25].replace('"', '').replace('\n', '')
        result["_is_parsed"] = True
        result["_source"] = r
    except:
        # memberikan default value bila gagal parsing
        for f in ["data", "status", "file_patch", "ip", "method", "host", "url"]:
            result[f] = None
            result["_is_parsed"] = False

        result["_source"] = r
    return result

def text_to_json(inp_file: str, out_file: str) -> None:
    with open(out_file, 'w') as out_f:
        with open(inp_file, "r") as in_f:
            for r in in_f:
                json_str = json.dumps(parser_nginx_error_log(r)) + "\n"
                out_f.write(json_str)

def json_to_text(inp_file: str, out_file: str) -> None:
    with open(out_file, 'w') as out_f:
        with open(inp_file, "r") as in_f:
            for r in in_f:
                result = []
                try:
                    data = json.loads(r)
                    for k, v in data.items():
                        result.append(str(v))
                except:
                    result.append(r)

                
                out_f.write("|".join(result))

@click.command()
@click.argument('logfile', required=True)
@click.option('-t', required=False, help='Tipe dari output', default="text")
@click.option('-o', required=True, help='Lokasi tujuan file konversi')
def command(logfile: str, t: str, o: str) -> None:
    """
    Konversi log file

    Contoh
    
    Text to Json

    python app.py error-connect.1000.logs -o error-connect.1000.logs.json -t json

    Json to Text

    python app.py error-connect.1000.logs.json -o error-connect.1000.logs.txt -t text

    Tanpa -t
    
    python app.py error-connect.1000.logs -o error-connect.1000.logs.default
    """

    # Jika format tidak dikenali maka akan dianggap menjadi "text"
    out_type = "json" if t.lower() == "json" else "text"

    if out_type == "json":
        text_to_json(logfile, o)
    else:
        json_to_text(logfile, o)

if __name__ == '__main__':
    command()