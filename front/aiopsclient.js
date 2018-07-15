class AioPubSubClient {
  constructor(host, client_id) {
    this.socket = new WebSocket(host);
    this.socket.onopen = () => {
      this.socket.send(`$register: ${client_id}`)
      this.onOpen()
    };
    this.socket.onmessage = event => {
      if(event.data instanceof Blob) {
        this.onBinaryMessage(event.data)
      } else {
        this.onMessage(event.data)
      }
    }
  }
  onOpen() {
    console.log('Connected to backend.')
  }
  onMessage(msg) {
    console.log(msg)
  }
  onBinaryMessage(msg) {
    console.log(`Recieved data: ${msg.size / 1024} kB`);
  }
};
