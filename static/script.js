
function main() {
    var socket = new WebSocket('ws://localhost:8080/ws');

    socket.onopen = () => {
      socket.send('$register: as12he8q')
      console.log('Connected to backend');
    };

    socket.onmessage = event => {
      console.log(`Recieved data: ${event.data.size / 1024} kB`);
      console.log(event.data)
    };
    return 1
}
