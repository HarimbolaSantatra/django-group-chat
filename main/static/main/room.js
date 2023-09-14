// ====== ON DOCUMENT LOAD
document.querySelector("#chat-message-input").focus();


 /* Add a list of messages to the UI
  * Parameters
    * messages: list of object. Each object should contains the following keys: room, username, message, date
    * username: current username. Used to change the color of each message
    * mode: str: 'first' or 'last' (default). Add to the head or to the tail of the block
  * Remark: make sure to update this code if you update the html layout in the room
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
console.log(`CSRF Token is ${csrftoken}`)

// ==== ON SEND NEW MESSAGE
const sendBtn = document.querySelector("#chat-message-submit");
sendBtn.addEventListener('click', (event) => {
  console.log("Sending new message ....")
  event.preventDefault();
  const addMessageEndpoint = `//${window.location.host}/write/`;
  const roomName = document.querySelector("#chat-message-room").value;
  const uName = document.querySelector("#chat-message-user").value;
  const mess = document.querySelector("#chat-message-input").value;
  let formData = new FormData();
  formData.append('username', uName);
  formData.append('room', roomName);
  formData.append('message', mess);
  const options = {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken
    },
    mode: 'same-origin',
    body: formData
  }
  fetch(addMessageEndpoint, options)
  .then( () => {
    addMessagesToUI([ {
      "room": roomName, 
      'username': uName, 
      'message': mess,
      'data': Date.now()
    } ], uName);
    // clear input value
    document.querySelector("#chat-message-input").value = '';
  })
});

// ====== LOAD MORE MESSAGE BTN
const loadingBtn = document.querySelector('#load-more-btn');
const roomName = document.querySelector("#chat-message-room").value;
const username = document.querySelector("#chat-message-user").value;
const loadMessageEndpoint =  `//${window.location.host}/load/${roomName}/`;
loadingBtn.addEventListener('click', () => {
  fetch(loadMessageEndpoint)
    .then(resp => resp.json())
    .then(resp => {
      addMessagesToUI(resp["data"], username, mode='first');
    })
})

