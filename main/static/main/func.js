function addMessagesToUI(messages){
  // messages: list. Contains all the messages to print

  const messageBlock = document.getElementById("message-block");

  for (let i =0; i < messages.length; i++) {
    const messageRow = document.createElement("div");
    const messageBox = document.createElement("div");
    const messageCard = document.createElement("div");
    const messageUsername = document.createElement("div");

    messageRow.className = "message-row primary-message-row";
    messageCard.className = "message-card";
    messageUsername.className = "message-name";
    messageUsername.textContent = "just now";

    messageBox.className = "message-box";
    messageBox.textContent = messages[i];

    messageRow.appendChild(messageCard);
    messageCard.appendChild(messageUsername);
    messageCard.appendChild(messageBox);
    messageBlock.appendChild(messageRow);
  }
}

function addResponseToUI(my_complex_json_response){
  /* 
  my_complex_json_response: the complex json response that you can find in models.py commentary.
  The variable names inside this function is the same as in room.html.
  !! NOT WORKING ANYMORE BECAUSE I EDIT THE UI OF ROOM.HTML !!
  */
  const chat_per_day = my_complex_json_response.chat_per_day;

  const messageBlock = document.getElementById("message-block");

  for (daily_message of chat_per_day) {
    const messageDay = document.createElement("div");
    messageDay.className = 'message-day';
    messageDay.textContent = daily_message.day;

    
    for (hourly_messages of daily_message.per_hour) {
      const messageHour = document.createElement("div");
      messageHour.textContent = hourly_messages.hour;

      for (message_chat of hourly_messages.chats) {
        const messageRow = document.createElement("div");
        messageRow.className = `message-row ${message_chat.class_name}`;
        messageBlock.prepend(messageRow);

        const messageCard = document.createElement("div");
        messageCard.className = 'message-card';
        messageRow.appendChild(messageCard);

        const messageName = document.createElement("div");
        messageName.className = 'message-name';
        messageName.textContent = message_chat.username;
        messageCard.appendChild(messageName);

        const messageBox = document.createElement("div");
        messageBox.className = 'message-box';
        messageBox.textContent = message_chat.message;
        messageCard.appendChild(messageBox);

      }
      messageBlock.prepend(messageHour);
    }
    messageBlock.prepend(messageDay);
  }
}

// function addMessageToDb(room, username, message, date){
//   var xhr = new XMLHttpRequest();
//   xhr.open('POST', `http://${window.location.host}/write/`, true);
//   xhr.setRequestHeader("Content-Type", "application/json");  
//   xhr.send(`room=${room}&username=${username}&message=${message}&date=${date}`);
//   xhr.onload = function(){
//     if(xhr.status === 200) {
//       // addResponseToUI(xhr.response);
//       alert("Message saved !")
//     }
//   }
// };


function handleSend(){
  const messageInputDom = document.querySelector("#chat-message-input");
  const message = messageInputDom.value;
  addMessagesToUI([message]);

  // clear input value
  messageInputDom.value = "";
}