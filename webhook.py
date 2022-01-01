import requests as r
from sys import argv
tunnel = r.get("http://127.0.0.1:4040/api/tunnels/command_line").json()
embed = {
    'title':"Server IP",
    'description': tunnel['public_url'][6:]
}
r.post(argv[1], json={'content':'','embeds':[embed]})