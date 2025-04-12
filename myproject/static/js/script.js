function togglePassword() {
    const pw = document.getElementById('password');
    pw.type = pw.type === 'password' ? 'text' : 'password';
  }

  
  // home page
  function toggleChat() {
    const chat = document.getElementById("chatWindow");
    chat.style.display = chat.style.display === "flex" ? "none" : "flex";
  }
  
  function openPostModal() {
    alert("Open modal to submit a story/post/photo/video.");
  }
  