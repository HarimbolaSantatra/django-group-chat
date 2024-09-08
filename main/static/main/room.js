// ====== ON DOCUMENT LOAD
const messageInputDom = document.querySelector("#chat-message-input");
const loadingBtn = document.querySelector('#load-more-btn');
const roomName = document.querySelector("#chat-message-room").value;
const username = document.querySelector("#chat-message-user").value;
const loadMessageEndpoint =  `//${window.location.host}/load/${roomName}/`;

messageInputDom.focus();

// create a new WebSocket
const chatSocket = new WebSocket(
  'wss://' + window.location.host + '/ws/chat/' + roomName + '/'
  )

// When receiving a new message
chatSocket.onmessage = function(e) {
  console.log(`New websocket message from server: ${e.data}`);
  const data = JSON.parse(e.data);
  let messageObject = {
    'room': roomName,
    'username': username,
    'message': data.message
  }
  addMessagesToUI([messageObject], username);
};

chatSocket.onclose = function(e) {
  console.error('Chat socket closed unexpectedly');
};

 /* Add a list of messages to the UI
  * Parameters
    * messages: list of object. Each object should contains the following keys: room, username, message, date
    * username: current username. Used to change the color of each message
    * mode: str: 'first' or 'last' (default). Add to the head or to the tail of the block
  * Remark: make sure to update this code if you update the html layout in the room!
  */
function addMessagesToUI(messages, username, mode='last'){

  const messageBlock = document.getElementById("message-block");

  if ( mode === 'first' ) {
    // reverse the order of the messages
    messages.reverse();
  } 

  for (let i =0; i < messages.length; i++) {
    const messageRow = document.createElement("div");
    const messageBox = document.createElement("div");
    const messageCard = document.createElement("div");
    const messageUsername = document.createElement("div");

    messageRow.className = "message-row";
    if (username == messages[i].username ) {
      messageRow.className += " primary-message-row";
    }
    else {
     messageRow.className += " secondary-message-row" ;
    }

    messageCard.className = "message-card";
    messageUsername.className = "message-name";
    messageUsername.textContent = messages[i].username;

    messageBox.className = "message-box";
    messageBox.textContent = messages[i].message;

    messageRow.appendChild(messageCard);
    messageCard.appendChild(messageUsername);
    messageCard.appendChild(messageBox);

    switch(mode) {
      case 'first':
        messageBlock.prepend(messageRow);
        break;
      case 'last':
        messageBlock.appendChild(messageRow);
        break;
      default:
        messageBlock.appendChild(messageRow);
        break;
    }

  }
}


// ON DOCUMENT READY, MAKE FIRST AJAX REQUEST TO LOAD THE FIRST PAGE
document.addEventListener("DOMContentLoaded", function() {
  fetch(loadMessageEndpoint)
    .then(resp => resp.json())
    .then(res => {
      addMessagesToUI(res["data"], username);
    })
});


// ==== GET CSRF TOKEN 
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// ==== ON SEND NEW MESSAGE
const sendBtn = document.querySelector("#chat-message-submit");
sendBtn.addEventListener('click', (event) => {
  console.log("Sending new message thought WebSocket....")
  event.preventDefault();
  const roomName = document.querySelector("#chat-message-room").value;
  const mess = messageInputDom.value;

  // send JSON data with the following key: room, username, message, date
  // this is required because that's the format conventionally accepted by the backend and the front-end.
  // Codes from both needs this!
  chatSocket.send(JSON.stringify({
    'room': roomName,
    'username': username,
    'message': mess,
    'date': new Date()
  }));

  messageInputDom.value = ''; // clear input value
});

// ====== Load more message btn
loadingBtn.addEventListener('click', () => {
  fetch(loadMessageEndpoint)
    .then(resp => resp.json())
    .then(resp => {
      addMessagesToUI(resp["data"], username, mode='first');
    })
})

