function generateIDS(max) {
    var random = document.getElementById("random");
    while (true) {
            id1 = Math.floor(Math.random() *  max + 1);
            id2 = Math.floor(Math.random() *  max + 1);
            if (id1 != id2 ) {
                document.getElementById("id1").value = id1;
                document.getElementById("id2").value = id2;
                break;
            }
    }
    random.submit();
}

function sendWinner(winnerID, loserID) {
    var send = document.getElementById("send");

    document.getElementById("winnerField").value = winnerID;
    document.getElementById("loserField").value = loserID;

    send.submit();
}
